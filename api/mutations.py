# mutations.py
from datetime import date
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Product

@convert_kwargs_to_snake_case
def create_product_resolver(obj, info, title, description, quantity, price):
    try:
        product = Product(
            title=title, description=description, quantity=quantity, price=price)
        db.session.add(product)
        db.session.commit()
        payload = {
            "success": True,
            "product": product.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Error create product"]
        }
    return payload

@convert_kwargs_to_snake_case
def update_product_resolver(obj, info, id, title, description, quantity, price):
    try:
        product = Product.query.get(id)
        if product:
            product.title = title
            product.description = description
            product.quantity = quantity
            product.price = price
        db.session.add(product)
        db.session.commit()
        payload = {
            "success": True,
            "product": product.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def delete_product_resolver(obj, info, id):
    try:
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        payload = {"success": True, "product": product.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload