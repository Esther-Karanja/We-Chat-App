import React from "react";
import {Link} from 'react-router-dom'


const NavBar =() =>{
    return(
        <nav className="navbar navbar-expand-lg fixed-top navbar-light bg-light">
  <div className="container-fluid">
    <a className="navbar-brand" href="/#">Navbar</a>
    
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>

    <div className="collapse navbar-collapse" id="navbarNav">
      <ul className="navbar-nav ">
        <li className="nav-item">
          <Link className="nav-link" to="/">Home</Link>
        </li>
        <li className="nav-item">
          <Link className="nav-link" to="/create_article">CreateArticles</Link>
        </li>
        <li className="nav-item">
          <Link className="nav-link" to="/contact_us">Contact</Link>
        </li> 
      </ul>
    </div>
  </div>
</nav>
    )
}
export default NavBar