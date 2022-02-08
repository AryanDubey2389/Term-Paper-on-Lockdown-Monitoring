import React, {Component} from 'react';
import { BrowserRouter as  Route, Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css"
import "./style.css"
export default class NavBar extends Component {
    
    constructor(props) {
        super(props);
    }

    render() {
        const my_style = {
            color: "yellow",
            fontSize : "100%"
        }
        return (     
            <div>             
                <nav className="navbaSr navbar-expand-lg navbar-dark bg-dark">
                    <div className="collapse navbar-collapse">
                        <ul className="navbar-nav">
                        <li className="navbaritem">
                                <Link to="/" className="nav-link" style = {my_style} >Home</Link>
                            </li>
                            <li className="navbaritem">
                                <a><Link to="/users" className="nav-link" activeClassName = "nav-link-active" style = {my_style} >Users</Link>
                                </a></li>
                                <li className="navbaritem">
                               <a> <Link to="/login" className="nav-link" style = {my_style}>Login</Link>
                               </a></li>
                            <li className="navbaritem">
                            <a> <Link to="/register" className="nav-link" style = {my_style}>Register</Link>
                                </a></li> 
                               <li className="navbaritem">
                                <a><Link to="/profile" className="nav-link" style = {my_style}>Profile</Link>
                                </a></li>                            
                        </ul>
                    </div>
                </nav>
            </div>
        )
    }
}