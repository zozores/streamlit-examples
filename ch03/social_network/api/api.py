from models import Post
import datetime

posts = []


class API:
    def __init__(self, config=None):
        self.config = config

    def add_post(self, post: Post):
        posts_before = len(posts)
        posts.append(post)
        if posts_before < len(posts):
            return True
        else:
            return False

    def get_posts(self, start_date: datetime.datetime, end_date: datetime.datetime):
        return posts
