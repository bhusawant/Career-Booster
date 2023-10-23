import React from "react";

const Contact = () => {
  return (
    <section className="contact" id="contact">
    <div id="contact-footer">
      <h1>
        Contact <span>Me!</span>
      </h1>
      <form action="#">
        <div className="inputbox">
          <input type="text" placeholder="Name" required />
          <input type="email" placeholder="Email Address" required />
        </div>
        <div className="inputbox">
          <input type="number" placeholder="Mobile no." required />
          <input type="text" placeholder="Subject" />
        </div>
        <textarea id="message" cols="30" rows="10" placeholder="Your Message" />
        <br />
        <a href="mailto:sujalgandhi786@gmail.com" className="email-btn">
          Send Email <span></span>
        </a>
      </form>
    </div>
    </section>
  );
};

export default Contact;