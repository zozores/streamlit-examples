from api import api_instance
from models import Post


def add_post(post: Post):
    if post is None or len(post.creator_name) == 0 or len(post.content) == 0:
        return None
    did_add = api_instance.add_post(post)
    return did_add
