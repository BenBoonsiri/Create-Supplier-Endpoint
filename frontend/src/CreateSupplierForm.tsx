import React from 'react';
import logo from './logo.svg';
import { FormControl, InputLabel, TextField, FormHelperText } from '@mui/material';

import './CreateSupplierForm.css';

function CreateSupplierForm() {
  return (
    <div className="createSupplierForm">
      <form>
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
                  sx={{ width: '100%' }}
                />
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
                />
            </div>
            <div className="formInput">
              <div className="formLabel">City</div>
                <TextField
                  id="supplierCity"
                  placeholder="Redwood City"
                  sx={{ width: '100%' }}
                />
            </div>
            <div className="formInput">
              <div className="formLabel">Province/State</div>
                <TextField
                  id="supplierProvinceState"
                  placeholder="California"
                  sx={{ width: '100%' }}
                />
            </div>
            <div className="formInput">
              <div className="formLabel">Country</div>
                <TextField
                  id="supplierCountry"
                  placeholder="USA"
                  sx={{ width: '100%' }}
                />
            </div>
            <div className="formInput">
              <div className="formLabel">Postal/Zip Code</div>
                <TextField
                  id="postalZipCode"
                  placeholder="94063"
                  sx={{ width: '100%' }}
                />
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
