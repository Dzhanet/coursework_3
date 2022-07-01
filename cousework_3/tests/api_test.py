import pytest
from bp_api import views



post_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


def test_posts_have_correct_keys(post):
    pass