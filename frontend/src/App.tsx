import React from 'react';
import logo from './logo.svg';
import './App.css';
import CreateSupplierForm from './CreateSupplierForm';

function App() {
  return (
    <div className="App">
      <div className="title">
        <h1>Rundoo</h1>
      </div>
      <div className="formContainer">
        <CreateSupplierForm/>
      </div>
    </div>
  );
}

export default App;
