from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Item, Category, Supplier, Order, Sale
from app.forms import AddItemForm

@app.route('/')
def index():
    items = Item.query.all()
    # Add more logic as needed
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = AddItemForm()
    if form.validate_on_submit():
        category = Category.query.get(form.category_id.data)
        supplier = Supplier.query.get(form.supplier_id.data)
        item = Item(name=form.name.data,
                    description=form.description.data,
                    category=category,
                    supplier=supplier,
                    price=form.price.data,
                    quantity=form.quantity.data)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_item.html', form=form)

# Define other routes and views as needed