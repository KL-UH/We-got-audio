import React from 'react';
import './FileUpload.css';

function FileUpload() {
  return (
    <div className='FileUpload'>

<div className='upload'>
  <input type="file" id="file" />
  <label for="file" class="btn-1">upload file</label>
  </div>

    </div>
  )
}

export default FileUpload