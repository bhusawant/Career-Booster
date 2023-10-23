import React from "react";
import { Routes, Route } from "react-router-dom";
import "../styles/RegiserStyles.css";
import { Form, Input, message } from "antd";
import { useDispatch } from "react-redux";
import { showLoading, hideLoading } from "../redux/features/alertSlice";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";

const Login = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  //form handler
  const onfinishHandler = async (values) => {
    // try {
      dispatch(showLoading());
      // const res = await axios.post("/api/v1/user/login", values);
      const res = await axios.post("http://127.0.0.1:5000/login", values)
      
      if (res.data.login){
        dispatch(hideLoading());
        sessionStorage.setItem("token",res.data.token);
        message.success("Login Successfully");
        navigate("/");
      }
      else{
      dispatch(hideLoading());
      // console.log(res.data.error);
      message.error(res.data.error);
      }
    //   if (res.data.success) {
    //     localStorage.setItem("token", res.data.token);
    //     message.success("Login Successfully");
    //     navigate("/");
    //   } else {
    //     message.error(res.data.message);
    //   }
    // } catch (error) {
    //   dispatch(hideLoading());
    //   console.log(error);
    //   message.error("something went wrong");
    // }


  };
  return (
    <div className="form-container ">
    <Form
      layout="vertical"
      onFinish={onfinishHandler}
      className="register-form"
    >
      <h3 className="text-center">Login From</h3>

      <Form.Item label="Email" name="email">
        <Input type="email" required />
      </Form.Item>
      <Form.Item label="Password" name="password">
        <Input type="password" required />
      </Form.Item>
      <Link to="/register" className="m-2">
        Not a user Register here
      </Link>
      <button className="btn btn-primary" id="b2" type="submit">
        Login
      </button>
    </Form>
  </div>
  );
};

export default Login;