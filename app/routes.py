from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Item, Category, Supplier, Order, Sale

@app.route('/')
def index():
    items = Item.query.all()
    # Add more logic as needed
    return render_template('index.html', items=items)

# Define other routes and views as needed