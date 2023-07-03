from flask import Blueprint, jsonify, request, Response
from werkzeug.utils import secure_filename
from .models import Supplier, Address, Img, db

main = Blueprint('main', __name__)

# Main endpoint for created a supplier. Remaining endpoints extra and for testing.
@main.route('/add_supplier', methods=['POST'])
def add_supplier():

    # Create new address
    newAddress = Address(
        street=request.form['street'], 
        city=request.form['city'], 
        province_state=request.form['province_state'], 
        country=request.form['country'], 
        postal_zip_code=request.form['postal_zip_code']
    )
    db.session.add(newAddress)

    # Parse logo
    logo = request.files['logo']
    print("logo is", logo)
    if not logo:
        return "Error: No Logo Uploaded", 400
    print("logo is", logo)
    filename = secure_filename(logo.filename)
    mimetype = logo.mimetype
    newImg = Img(img=logo.read(), mimetype=mimetype, name=filename)
    db.session.add(newImg)

    # Create supplier
    newSupplier = Supplier(supplier_name=request.form['supplier_name'],logo=newImg, address=newAddress)
    db.session.add(newSupplier)
    
    db.session.commit()
    return 'Supplier has been created', 200

# Endpoint returns all suppliers, with address_id's and logo_id's to access address and logos
@main.route('/suppliers', methods=['GET'])
def getSuppliers():
    suppliersList = Supplier.query.all()
    suppliers = []

    for supplier in suppliersList:
        suppliers.append({'supplier_name': supplier.supplier_name, 'address_id' : supplier.address_id, 'logo_id' : supplier.logo_id})

    return jsonify({'suppliers': suppliers})

# Endpoint returns logo based on id which can be accessed from /suppliers endpoint
@main.route('/image/<int:id>', methods=['GET'])
def getImage(id):
    img = Img.query.filter_by(image_id = id).first()
    if not img:
        return "Image with id not found", 404
    
    return Response(img.img, mimetype=img.mimetype)

# Endpoint returns address based on id which can be accessed from /suppliers endpoint
@main.route('/address/<int:id>', methods=['GET'])
def getAddress(id):
    img = Img.query.filter_by(image_id = id).first()
    address = Address.query.filter_by(address_id = id).first()
    if not address:
        return "Address with id not found", 404
    
    return ({'street': address.street, 
             'city': address.city, 
             'province_state': address.province_state, 
             'country': address.country, 
             'postal_zip_code': address.postal_zip_code})