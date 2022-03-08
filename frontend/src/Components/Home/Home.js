import React from 'react';
import NavBar from '../NavBar/NavBar';
import InputBar from '../InputBar/InputBar';
import { Outlet, Link } from "react-router-dom";
import './Home.css';
import Button from "react-bootstrap/Button";

function Home() {
  return (
    <div className='Home'>
      <NavBar />
      <InputBar />

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

export default Home;