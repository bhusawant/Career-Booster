import React from "react";
import aboutImg from "../assets/home-img.jpg";  

const Home = () => {
  return (
    <section className="home">
      <img src={aboutImg} className="home-img" />
      <div className="home-img-text">Career Counselling</div>
    </section>
  );
};

export default Home;