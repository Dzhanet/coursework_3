import pytest
from utils import search_for_posts, load_data_json, load_comments_json


class TestUtils:

    def test_posts(self):

        posts_data = load_data_json()
        assert len(posts_data) != 0

    def test_check_keys(self):
        posts_data = load_data_json()
        keys_post = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
        for key in keys_post:
            assert key in keys_post

    def test_comments(self):
        comments_data = load_comments_json()
        assert len(comments_data) != 0

    def test_check_keys_comments(self):
        comments_data = load_comments_json()
        keys_comments = ['post_id', 'commenter_name', 'comment', 'pk']
        for key in keys_comments:
            assert key in keys_comments








