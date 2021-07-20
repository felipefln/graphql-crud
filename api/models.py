from app import db

class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)
  description = db.Column(db.String)
  quantity = db.Column(db.Integer)
  price = db.Column(db.Float)

  def to_dict(self):
    return {
      "id": self.id,
      "title": self.title,
      "description": self.description,
      "quantity": self.quantity,
      "price": self.price
    }