import React, { useState } from "react";
import "../diff.css"
import { questions } from "../Data/data";
import { useDispatch } from "react-redux";
import axios from "axios";
// import { trackForMutations } from "@reduxjs/toolkit/dist/immutableStateInvariantMiddleware";


// async function onfinishHandler(e) {
//     const dispatch = useDispatch()
//     e.preventDefault();
//     console.log(e);
//     const [var1, setVar1] = useState([]);
    
//     // const formDataObject = {};
//     // formData.forEach((value, key) => {
//     //     formDataObject[key] = value;
//     // });

//     try {
//         // dispatch(showLoading());
        

//         dispatch(hideLoading());
//         // Handle the response as needed
//     } catch (error) {
//         dispatch(hideLoading());
//         console.log(error);
//         message.error("Something Went Wrong");
//     }
// }




export default function Difficulties(){
    const [var1, setVar1]=useState([])

    const handleChange = (e) => {
        setVar1({ ...var1, [e.target.name]: e.target.value});
        console.log(var1);
      };

    function Handleclick(e) {
        e.preventDefault();
        // const formData = new FormData(e.target);
        // console.log(formData);
      var inputbox1 = document.getElementById('ans1');
      var input1 = inputbox1.value;
      console.log(input1);
      var inputbox2 = document.getElementById('ans2');
      var input2 = inputbox2.value;
      console.log(input2);
      var inputbox3 = document.getElementById('ans3');
      var input3 = inputbox3.value;
      console.log(input3);
      var inputbox4 = document.getElementById('ans4');
      var input4 = inputbox4.value;
      console.log(input4);
      var inputbox5 = document.getElementById('ans5');
      var input5 = inputbox5.value;
      console.log(input5);
      var inputbox6 = document.getElementById('ans6');
      var input6 = inputbox6.value;
      console.log(input6);
      var inputbox7 = document.getElementById('ans7');
      var input7 = inputbox7.value;
      console.log(input7);
      var inputbox8 = document.getElementById('ans8');
      var input8 = inputbox8.value;
      console.log(input8);
      var inputbox9 = document.getElementById('ans9');
      var input9 = inputbox9.value;
      console.log(input9);
      var inputbox10 = document.getElementById('ans10');
      var input10 = inputbox10.value;
      console.log(input10);
      const res = axios.post("http://127.0.0.1:5000/diff", {"ans1":input1,"ans2":input2,"ans3":input3,"ans4":input4,"ans5":input5,"ans6":input6,"ans7":input7,"ans8":input8,"ans9":input9,"ans10":input10,
    })
        .then((res)=> {
            // console.log(res.data)
            const data1 = JSON.stringify(res.data)
            localStorage.setItem("data",data1)
            
            
        })
        .catch((err)=> {
            console.log(err)
        })
    // console.log(res.data)

    
    }
    return ( 
        <>
        

        <form onSubmit={Handleclick} id="form-diff">

        <h1 className="title2">Assessment</h1>
        {questions.map(({id, question, idx, name})=>{
            return(
            <div className="form_control" key={id}>
            <label className="question" >
            {id}. {question} (Rate from 1-5)
            </label> 
            <input type="text" value={var1[name]} id={idx} name={name} onChange={handleChange} ></input>
            {/* <button type="submit" onClick={Handleclick}>Submit</button> */}
        </div>
            )
        })}


        <button className="btn btn-primary" id="b1" type="submit" onClick={Handleclick}>
            Submit
          </button>

        </form>
    </>
    )
}

