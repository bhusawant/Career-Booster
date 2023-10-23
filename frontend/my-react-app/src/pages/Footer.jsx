import React from "react";

const Footer = () => {
    // const pagelinks = [
    //   { id: 1, href: "#home", text: "home" },
    //   { id: 2, href: "#about", text: "about" },
    //   { id: 3, href: "#services", text: "services" },
    //   { id: 41, href: "#tours", text: "tours" },
    // ];
    // const socialLinks = [
    //   { id: 1, href: "https://www.twitter.com", icon: "fab fa-facebook" },
    //   { id: 2, href: "https://www.twitter.com", icon: "fab fa-twitter" },
    //   { id: 3, href: "https://www.twitter.com", icon: "fab fa-squarespace" },
    // ];
  return (
    <footer class="section footer">
      {/* <ul class="footer-links">
        {pagelinks.map(({ id, href, text }) => {
          return (
            <li key={id}>
              <a href={href} class="footer-link">
                {text}
              </a>
            </li>
          );
        })}
      </ul> */}
    
      <p class="copyright">
        copyright &copy; Xplorer company
        <span id="date">{new Date().getFullYear()}</span> all rights reserved
      </p>
    </footer>
  );
};

export default Footer;