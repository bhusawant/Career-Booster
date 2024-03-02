import React, { useState, useEffect } from 'react';
import axios from 'axios'; // You can also use 'fetch' if preferred
import "../styles/joblist.css"

function DisplayListFromBackend() {
  const [jobRoles, setJobRoles] = useState([]);
  const [error, setError] = useState(null);


  useEffect(() => {
    // Retrieve the dictionary from local storage
    const storedDictionary = localStorage.getItem('data');
    if (storedDictionary) {
      const dictionary = JSON.parse(storedDictionary);
      // Check if "arr" key exists and contains an array
      if (dictionary && dictionary.arr && Array.isArray(dictionary.arr)) {
        // Set the job roles state with the values of "arr"
        setJobRoles(dictionary.arr);
      }
    }
  }, []);

  return (
    <div className='job'>
      {/* <h1 className='jobHeading'>List from Flask Backend</h1> */}
      <h1 className='jobHeading'>Recommended job roles</h1>
      {/* <div className='dataOfJob'>
        <h2 className='job'>{data2}</h2>
      </div> */}


      {jobRoles.map((jobRole, index) => (
        <div className='jobsdata'>
          <p className='jobroles' key={index}>{jobRole}</p>
        </div>
      ))}

    </div>
  );
}

export default DisplayListFromBackend;

