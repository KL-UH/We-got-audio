import React from 'react';
import NavBar from '../NavBar/NavBar';
import { Outlet, Link } from "react-router-dom";
import Button from "react-bootstrap/Button";

function File() {
  return (
    <div className='File'>
        <NavBar />

        {/* Navigate to URL and File */}
      <div className='toggle'>
        <li>
          <Link className='LinkTag' to='/'>
            <Button>URL</Button>
          </Link>
        </li>
        <li>
          <Link className='LinkTag' to='/file'>
            <Button>File</Button>
          </Link>
        </li>
      </div>


      <Outlet />
    </div>
  )
}

export default File