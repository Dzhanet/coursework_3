from flask import Blueprint, jsonify
from utils import load_data_json, single_post
import logging


api_blueprint = Blueprint('api_blueprint', __name__)

logger = logging.getLogger("api_logs")

@api_blueprint.route('/api/posts/')
def api_posts():
    """Возвращает джейсон со всеми постами"""

    posts = load_data_json()
    logger.info("Запрошены все посты")
    return jsonify(posts)

@api_blueprint.route('/api/posts/<int:id>')
def api_posts_id(id):
    """Возвращает джейсон с  одним постом"""

    post = single_post(id)
    logger.info("Запрошен один пост")
    return jsonify(post)
