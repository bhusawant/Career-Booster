import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import store from './redux/store'
import { Provider } from 'react-redux'
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import { useSelector } from "react-redux";
import Spinner from "./components/Spinner";
import ProtectedRoute from "./components/ProtectedRoute";
import PublicRoute from "./components/PublicRoute";

import Header from "./pages/Header";
import DashboardTemplate from "./pages/DashboardTemplate";
import Application from "./pages/Application";

import Apply from "./pages/Apply";
import Difficulties from "./pages/Difficulties";
import Address from "./pages/Address";
import Resources from "./pages/ResourcePage";
import About from './pages/About'
import Home from './pages/Home'
import Contact from './pages/Contact'
import Footer from './pages/Footer'
import Chatbot from './pages/Chatbot'
import JobList from './pages/JobList'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Provider store={store}>

      <BrowserRouter>
        { (
          <Routes>
            <Route
              path="/"
              element={
                <><Header /><DashboardTemplate /></>
              }
              />
            <Route
              path="/chatbot"
              element={
                <><Header /><Chatbot/><DashboardTemplate /></>
              }
              />
            <Route
              path="/login"
              element={
                <PublicRoute>
                {/* <ProtectedRoute> */}
                  <Login />
                  {/* </ProtectedRoute> */}
                </PublicRoute>
              }
              />
            <Route
              path="/register"
              element={
                <PublicRoute>
                {/* <ProtectedRoute> */}
                  <Register />
                {/* </ProtectedRoute> */}
                </PublicRoute>
              }
              />
            <Route
              path="/application"
              element={
                <><Header /><Application /><DashboardTemplate /></>
                
              }
              />
            <Route
              path="/resources"
              element={
                <><Header /><Resources /><DashboardTemplate /></>
                
              }
              />
            <Route
              path="/diff"
              element={
                <><Header /><Difficulties /><DashboardTemplate /></>
              }
              />
            <Route
              path="/address"
              element={
                <><Header /><Address /><DashboardTemplate /></>
              }
              />
            <Route
              path="/about"
              element={
                <><Header /><About/><Footer/></>
              }
              />
            <Route
              path="/home1"
              element={
                <><Header /><Home/><About/><Contact/><Footer/></>
              }
              />
            <Route
              path="/contact"
              element={
                <><Header /><Contact/><Footer/></>
              }
              />
            <Route
              path="/joblist"
              element={
                <><Header /><JobList/><DashboardTemplate /></>
              }
              />
          </Routes>
        )}
      </BrowserRouter>
      </Provider>
    </>
  )
}

export default App
