import React, { useState, useEffect } from 'react';
import axios from 'axios'; // You can also use 'fetch' if preferred
import "../styles/joblist.css"

function DisplayListFromBackend() {
    const [data, setData] = useState([]);
    const [error, setError] = useState(null);
    const data2 = localStorage.getItem("data")
    console.log(data2)
  return (
    <div>
      <h1 className='job'>List from Flask Backend</h1>
        <h2 className='job'>{data2}</h2>


    </div>
  );
}

export default DisplayListFromBackend;

