import React from 'react';
import Home from '../Home/Home';
import File from '../File/File';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';


function Navigate() {
  return (
    <div className='Navigation'>
      <Router>
        <Routes>
          <Route path="/" exact element={<Home />} />
          <Route path='/file' exact element={<File />} />
        </Routes>
      </Router>
    </div>
  )
}

export default Navigate