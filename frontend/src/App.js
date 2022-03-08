import React from 'react';
import './App.css';
import Home from './Components/Home/Home';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import File from './Components/File/File';


function App() {
  return (
    <div className="App">

      <BrowserRouter>
        <Routes>
          <Route path="/" exact element={<Home />} />
          <Route path="file" exact element={<File />} />
        </Routes>
      </BrowserRouter>

    </div>
  );
}

export default App;