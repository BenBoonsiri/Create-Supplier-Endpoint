from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Address(db.Model):
    __tablename__ = "addresses"
    address_id = db.Column(Integer, primary_key=True)
    street = db.Column(String)
    city = db.Column(String)
    province_state = db.Column(String)
    country = db.Column(String)
    postal_zip_code = db.Column(String)
    
class Img(db.Model):
    __tablename__ = "images"
    image_id = db.Column(Integer, primary_key = True)
    img = db.Column(Text, nullable = False)
    name = db.Column(Text, nullable = False)
    mimetype = db.Column(Text, nullable=False)

class Supplier(db.Model):
    __tablename__ = "suppliers"
    supplier_id = db.Column(Integer, primary_key=True)
    supplier_name = db.Column(String)
    logo_id = db.Column(Integer, ForeignKey("images.image_id", ondelete="SET NULL"), nullable=True)
    address_id = db.Column(Integer, ForeignKey("addresses.address_id", ondelete="SET NULL"), nullable=True)
    logo = relationship(Img)
    address = relationship(Address)