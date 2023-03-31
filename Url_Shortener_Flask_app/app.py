from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, redirect, request, render_template, url_for
import string
import random
from pyshorteners import Shortener

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
migrate = Migrate(app, db)

db.init_app(app)

class Url(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    original_url = db.Column(db.String, nullable=False)
    short_url = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=["GET","POST"])
def home():
    if request.method == 'POST':
       original = request.form['my_url']
       short = Shortener().tinyurl.short(original)
       link = Url(original_url=original, short_url=short)
       db.session.add(link)
       db.session.commit()
       return redirect("/")
    
    track_url = Url.query.all()
    return render_template("index.html", urls = track_url)


#Herethe deletion takes place
@app.route('/delete/<int:sno>')
def delete(sno):
    link = Url.query.filter_by(id = sno).first()
    db.session.delete(link)
    db.session.commit()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
           
    