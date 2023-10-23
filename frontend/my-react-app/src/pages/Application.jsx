import React from "react";
import "../Application.css"

export default function Application(){
    return ( 
        <>
        
        <h1 className="title">Personal Details</h1>
        <div className="container">

        <div className="userdetails">

        <div className="inputfield">
        <label>Applicant First Name</label>
        <input type="text" placeholder="Enter your first name" required/>
        </div>


        <div className="inputfield">
        <label>Applicant Middle Name </label>
        <input type="text" placeholder="Enter your name" required/>
        </div>

        <div className="inputfield">
        <label>Applicant Surname</label>
        <input type="text" placeholder="Enter your name" required/>
        </div>

        <div className="inputfield">
        <label>Applicant Father's Name</label>
        <input type="text" placeholder="Enter your name" required/>
        </div>

        <div className="inputfield">
        <label>Applicant Mother's Name</label>
        <input type="text" placeholder="Enter your name" required/>
        </div>

        <div className="inputfield">
        <label>Date of Birth </label>
        <input type="date" placeholder="Enter your name" required/>
        </div>

        <div className="inputfield">
        <label>Gender</label>
        <input type="text" placeholder="Please select gender" required/>
        </div>

        <div className="inputfield">
        <label>Mobile Number</label>
        <input type="text" placeholder="+91" required/>
        </div>

        <div className="inputfield">
        <label>E-mail Id</label>
        <input type="text" placeholder="Enter your name" required/>
        </div>


        
        <div className="inputfield">
        <input type="Submit" placeholder="Enter your UDID" required/>
        </div>

        
        </div>

        </div>




        
    </>
    )
}

