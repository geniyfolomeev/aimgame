import flask
from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)

class Article(database.Model):
    num = database.Column(database.Integer, primary_key=True, autoincrement=True)
    row = database.Column(database.String(50))

    def __repr__(self):
        return '<Article %r>' % self.num

@app.route('/', methods=["GET"])
def hello():
    # if request.method == "POST":
    #     text = request.form['chat-box-tray']
    #
    #     article = Article(row=text)
    #
    #     try:
    #         database.session.add(article)
    #         database.session.commit()
    #         return redirect('/')
    #     except:
    #         return "Shit happens"
    # text = request.form["primary"]
    # print(text)
    return flask.render_template("index.html")


if __name__ == '__main__':
    app.run()
