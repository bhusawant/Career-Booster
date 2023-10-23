import React from "react";
import aboutImg from "../assets/home-img.jpg";
import '../styles/home.css'

const About = () => {
  return (
    <section class="section" id="about">
      <h2>About <span>Us</span></h2>

      <div class="section-center about-center">
        <div class="about-img">
          <img src={aboutImg} class="about-photo" alt="awesome beach" />
        </div>
        <article class="about-info">
          <h2>explore the difference</h2>
          <p>
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aspernatur
            quisquam harum nam cumque temporibus explicabo dolorum sapiente odio
            unde dolor?
          </p>
          <p>
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aspernatur
            quisquam harum nam cumque temporibus explicabo dolorum sapiente odio
            unde dolor?
          </p>
          <a href="" class="btn">
            read more
          </a>
        </article>
      </div>
    </section>
  );
};

export default About;