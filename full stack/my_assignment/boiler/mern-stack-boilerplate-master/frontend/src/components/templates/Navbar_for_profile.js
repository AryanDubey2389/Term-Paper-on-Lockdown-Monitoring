import React, {Component} from 'react';
import { BrowserRouter as Route, Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css"
import "./style.css"
export default class NavBar extends Component {
    
    constructor(props) {
        super(props);
    }

    render() {
        const my_style = {
            color: "yellow",
            margine : "100px",
            fontSize : "36"
        }
        return (
            <div>                
                <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                    <div className="collapse navbar-collapse">
                        <ul className="navbar-nav mr-auto">
                        <li className="navbaritem">
                            <a><Link to="/" className="nav-link" style = {my_style} >Home</Link>
                            </a>  </li>
                            <li className="navbaritem">
                                <a><Link to="/recruiterprofile/recruiterjobs/users" className="nav-link" activeClassName = "nav-link-active" style = {my_style} >Users List</Link>
                                </a></li>
                        <li className="navbaritem">
                            <a> <Link to="/profile/edit" className="nav-link" style = {my_style}>Edit Profile</Link>
                             </a>  </li>
                        <li className="navbaritem">
                           <a> <Link to="/profile" className="nav-link" style = {my_style}>Dashboard</Link>
                            </a>  </li>
                        <li className="navbaritem">
                           <a> <Link to="/profile/myapplications" className="nav-link" style = {my_style}>My Applications</Link>
                           </a></li>
                        <li className="navbaritem">
                            <a> <Link to="/login" className="nav-link" style = {my_style}>Logout</Link>
                             </a>   </li>     
                             <li className="navbaritem">
                            <a> <Link to="/profile/contact" className="nav-link" style = {my_style}>Contact_us</Link>
                             </a>   </li>               
                        </ul>
                    </div>
                </nav>
            </div>
        )
    }
}