from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)



class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)


#Creates the database allegedly 
from app import db
with app.app_context():
    db.create_all()
    

    def __reper__(self):
        return '<Task %r>' % self.id
    


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "main":
    app.run(debug=True)