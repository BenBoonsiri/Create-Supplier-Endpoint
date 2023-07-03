from flask import Blueprint, jsonify, request, Response
from werkzeug.utils import secure_filename
from models import Supplier, Address, Img, db

main = Blueprint('main', __name__)

# Main endpoint for created a supplier. Remaining endpoints extra and for testing.
@main.route('/add_supplier', methods=['POST'])
def add_supplier():
    try:
        # Handle address. Make new or assign existing id if address already inputed.
        newStreet = request.form['street']
        newCity = request.form['city']
        newProvinceState = request.form['province_state']
        newCountry = request.form['country']
        newPostalZip = request.form['postal_zip_code']

        newAddress = None
        existingAddress = Address.query.filter_by(street = newStreet, 
                                                  city=newCity, 
                                                  province_state=newProvinceState, 
                                                  country = newCountry, postal_zip_code = 
                                                  newPostalZip).first()
        if existingAddress:
            newAddress = existingAddress
        else:
            newAddress = Address(
                street=newStreet, 
                city=newCity, 
                province_state=newProvinceState, 
                country=newCountry, 
                postal_zip_code=newPostalZip
            )
            db.session.add(newAddress)

        # Handle logo. Make new or assign existing id if duplicate photo already uploaded.
        logo = request.files['logo']
        if not logo:
            return "Error: No Logo Uploaded", 400
        actualImage = logo.read()
        newImg = None
        existingImg = Img.query.filter_by(img = actualImage).first()
        if existingImg:
            newImg = existingImg
        else:
            filename = secure_filename(logo.filename)
            mimetype = logo.mimetype
            newImg = Img(img=actualImage, mimetype=mimetype, name=filename)
            db.session.add(newImg)

        # Handle supplier.
        existingSupplier = Supplier.query.filter_by(supplier_name = request.form['supplier_name'], 
                                                    logo_id = newImg.image_id, 
                                                    address_id=newAddress.address_id).first()
        if not existingSupplier:
            newSupplier = Supplier(supplier_name=request.form['supplier_name'],logo=newImg, address=newAddress)
            db.session.add(newSupplier)
        else:
            return "Supplier already exists", 400
        
        db.session.commit()
        return "Supplier has been created", 200
    except Exception as e:
        return str(e), 400

# Endpoint returns all suppliers, with address_id's and logo_id's to access address and logos
@main.route('/suppliers', methods=['GET'])
def getSuppliers():
    suppliersList = Supplier.query.all()
    suppliers = []

    for supplier in suppliersList:
        suppliers.append({'supplier_id': supplier.supplier_id , 'supplier_name': supplier.supplier_name, 'address_id' : supplier.address_id, 'logo_id' : supplier.logo_id})

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
    address = Address.query.filter_by(address_id = id).first()
    if not address:
        return "Address with id not found", 404
    
    return ({'address_id': address.address_id,
             'street': address.street, 
             'city': address.city, 
             'province_state': address.province_state, 
             'country': address.country, 
             'postal_zip_code': address.postal_zip_code})