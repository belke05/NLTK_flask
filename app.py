from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)
# db = SQLAlchemy()
# app.config.from_object(os.environ['APP_SETTINGS'])
# change the env variable app settings to switch from environment 
# as object it will use our config module
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)
# SQL alchemy is our Object relational mapper
# import models

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/<name>")
def hello(name=None):
    return render_template("index.html", name=name)



if __name__ == '__main__':
    app.run(debug=True)