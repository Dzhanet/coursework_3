import random
from app import app
from utils import load_data_json
import pytest

class TestApi:

    def test_api_posts(self):
        resp = app.test_client().get("/api/posts/", follow_redirects=True)
        assert resp.status_code == 200
        assert type(resp.json) == list

    def test_api_post(self):
        posts_data = load_data_json()
        random_post = random.choice(posts_data)
        resp = app.test_client().get(f"/api/posts/{random_post['pk']}", follow_redirects=True)
        assert resp.status_code == 200
        assert type(resp.json) == dict
        post_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
        assert resp.json.keys() == post_keys

