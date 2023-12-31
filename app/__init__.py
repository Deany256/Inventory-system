from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use your preferred database URL
db = SQLAlchemy(app)

from app import models, routes  # Import routes and models to avoid circular imports

# Create the database tables
with app.app_context():
    db.create_all()