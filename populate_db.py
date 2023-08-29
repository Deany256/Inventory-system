from app import db
from app.models import Category, Supplier

# Create instances of Category
category1 = Category(name='Electronics')
category2 = Category(name='Clothing')
category3 = Category(name='Furniture')

# Add instances to the database session
db.session.add(category1)
db.session.add(category2)
db.session.add(category3)

# Commit the changes to the database
db.session.commit()

# Create instances of Supplier
supplier1 = Supplier(name='TechCorp', contact_email='tech@example.com', phone_number='123-456-7890')
supplier2 = Supplier(name='FashionHub', contact_email='fashion@example.com', phone_number='987-654-3210')
supplier3 = Supplier(name='FurnishNow', contact_email='furniture@example.com', phone_number='555-123-4567')

# Add instances to the database session
db.session.add(supplier1)
db.session.add(supplier2)
db.session.add(supplier3)

# Commit the changes to the database
db.session.commit()

print("Database populated successfully!")
