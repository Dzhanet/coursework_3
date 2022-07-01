from flask import Flask, render_template
from bp_posts.views import posts_blueprint
from bp_api.views import api_blueprint

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)

@app.errorhandler(404)
def pageNotFound(error):
    """ Возвращает обратно если ошибка 404"""

    return render_template('error_404.html')



if __name__ == "__main__":
    app.run(debug=True)