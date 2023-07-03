import React, { useState } from 'react';
import logo from './logo.svg';
import { Button, TextField} from '@mui/material';

import './CreateSupplierForm.css';


function CreateSupplierForm() {
  // Set state for supplier object
  const [supplierName, setSupplierName] = useState("");

  // Set state for address
  const [street, setStreet] = useState("");
  const [city, setCity] = useState("");
  const [provinceState, setProvinceState] = useState("");
  const [country, setCountry] = useState("");
  const [postalZip, setPostalZip] = useState("");

  // Set state for logo
  const [logo, setLogo] = useState<File>();

  // On logo upload
  const handleLogo = (event: React.FormEvent) => {
    const files = (event.target as HTMLInputElement).files

    if (files && files.length > 0) {
        setLogo(files[0])
    }
  }

  return (
    <div className="createSupplierForm">

      <form onSubmit={async() => {
        const formData = new FormData();
        formData.append("supplier_name", supplierName)

        formData.append("street", street)
        formData.append("city", city)
        formData.append("province_state", provinceState)
        formData.append("country", country)
        formData.append("postal_zip_code", postalZip)

        if (logo) {
          formData.append("logo", logo, logo.name)
        }

        const response = await fetch('/add_supplier', {
          method: 'POST',
          body: formData
        })

        if (response.ok){
          console.log('response success')
        } else {
          console.log('error')
        }
      }}>

        <div className="borderSection">
          <div className="formTitle">Create Supplier</div>
        </div>

        <div className="borderSection">
          <div className="formInputGroup">
            <div className="sectionTitle">Brand</div>
            <div className="formInput">
              <div className="formLabel">Supplier Name</div>
                <TextField
                  id="supplierName"
                  placeholder="Rundoo Depot"
                  value={supplierName}
                  onChange={e=> setSupplierName(e.target.value)}
                  sx={{ width: '100%' }}
                />
            </div>
            <div className="formInput">
              <div className="formLabel">Logo</div>
              <div className="submitGroup">
                <Button id='upload' variant="contained" component="label">
                  Upload Image
                  <input
                    type="file"
                    hidden
                    onChange={handleLogo}
                  />
                </Button>
                <div className="fileName">{logo?.name}</div>
              </div>
            </div>
          </div>
        </div>
        <div>
          <div className="formInputGroup">
            <div className="sectionTitle">Address</div>
            <div className="formInput">
              <div className="formLabel">Street</div>
                <TextField
                  id="supplierStreet"
                  placeholder="Convention Way"
                  sx={{ width: '100%' }}
                  value={street}
                  onChange={e=> setStreet(e.target.value)}
                />
            </div>
            <div className="formInput">
              <div className="formLabel">City</div>
                <TextField
                  id="supplierCity"
                  placeholder="370 Convention Way #102"
                  sx={{ width: '100%' }}
                  value={city}
                  onChange={e=> setCity(e.target.value)}
                />
            </div>
            <div className="formInput">
              <div className="formLabel">Province/State</div>
                <TextField
                  id="supplierProvinceState"
                  placeholder="California"
                  sx={{ width: '100%' }}
                  value={provinceState}
                  onChange={e=> setProvinceState(e.target.value)}
                />
            </div>
            <div className="formInput">
              <div className="formLabel">Country</div>
                <TextField
                  id="supplierCountry"
                  placeholder="United States"
                  sx={{ width: '100%' }}
                  value={country}
                  onChange={e=> setCountry(e.target.value)}
                />
            </div>
            <div className="formInput">
              <div className="formLabel">Postal/Zip Code</div>
                <TextField
                  id="postalZipCode"
                  placeholder="94063"
                  sx={{ width: '100%' }}
                  value={postalZip}
                  onChange={e=> setPostalZip(e.target.value)}
                />
            </div>

            <div className="buttonWrapper">
                <Button className="button" type="submit" variant="contained">Submit</Button>
            </div>
          </div>
        </div>
        <div>
        </div>
      </form>
    </div>
  );
}

export default CreateSupplierForm;
