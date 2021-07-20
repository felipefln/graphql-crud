from .models import Product
from ariadne import convert_kwargs_to_snake_case

def listProducts_resolver(obj, info):
    try:
        products = [product.to_dict() for product in Product.query.all()]
        print(products)
        payload = {
            "success": True,
            "products": products
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]

        }
    return payload

@convert_kwargs_to_snake_case
def getProduct_resolver(obj, info, id):
    try:
        product = Product.query.get(id)
        payload = {
            "success": True,
            "product": product.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Product item matching {id} not found"]
        }
    return payload