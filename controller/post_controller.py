from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from model import Post 
from cachetools import TTLCache

# Create an in-memory cache with a max size of 100 and a TTL (time-to-live) of 5 minutes (300 seconds)
cache = TTLCache(maxsize=100, ttl=300)


def add_new_post(request, post_request, get_logged_user, db, MAX_PAYLOAD_SIZE_BYTES):
    content_length = request.headers.get("content-length")
    if content_length and int(content_length) > MAX_PAYLOAD_SIZE_BYTES:
        raise HTTPException(
            status_code=413,  # Payload Too Large
            detail="Payload size exceeds the maximum allowed size.",
        )
    current_user = get_logged_user
    new_post = Post(title=post_request.title, content=post_request.content, user_id=current_user["user_id"])
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_posts_of_user(get_logged_user, db):
    current_user = get_logged_user
    user_id = current_user["user_id"]
    # Check if the response is cached
    cached_response = cache.get(user_id)
    if cached_response:
        print("retrieving cached response!!")
        return cached_response
    posts = db.query(Post).filter(Post.user_id==user_id).all()
    #storing the json response here, user_id will be the key and list of post is the value
    cache[user_id] = [post.to_json() for post in posts]
    return posts

def get_post(post_id, db):
    post = db.query(Post).filter(Post.id==post_id).first()
    if not post:
        raise HTTPException(status_code=400, detail=f"No post found with this id: {post_id}")
    return post

def delete_your_post(get_logged_user, post_id, db):
    current_user = get_logged_user
    post = db.query(Post).filter(Post.id==post_id).first()
    if not post:
        raise HTTPException(status_code=400, detail=f"No post found with this id: {post_id}")
    if current_user['user_id'] == post.user_id:
        db.delete(post)
        db.commit()
        return {"message": "Post deleted successfully"}
    raise HTTPException(status_code=403, detail=f"Not authorized to delete this post.")