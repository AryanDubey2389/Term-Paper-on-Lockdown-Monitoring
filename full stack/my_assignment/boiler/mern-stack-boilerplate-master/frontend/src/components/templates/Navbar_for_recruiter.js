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
            fontSize : "100%"
        }
        return (
            <div>                
                <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                    <div className="collapse navbar-collapse">
                        <ul className="navbar-nav mr-auto">
                        <li className="navbaritem">
                                <Link to="/" className="nav-link" style = {my_style} >Home</Link>
                            </li>
                            <li className="navbaritem">
                                <a><Link to="/recruiterprofile/recruiterjobs/users" className="nav-link" activeClassName = "nav-link-active" style = {my_style} >Users List</Link>
                                </a></li>
                            <li className="navbaritem">
                                <Link to="/recruiterprofile" className="nav-link" style = {my_style}>Create Jobs</Link>
                            </li>
                            <li className="navbaritem">
                                <Link to="/recruiterprofile/recruiterjobs" className="nav-link" style = {my_style}>My active jobs</Link>
                            </li>
                            <li className="navbaritem">
                                <Link to="/login" className="nav-link" style = {my_style}>Logout</Link>
                            </li>            
                            <li className="navbaritem">
                                <Link to="/recruiterprofile/recruiterjobs/contact" className="nav-link" style = {my_style}>Contact_us</Link>
                            </li>                            
                        </ul>
                    </div>
                </nav>
            </div>
        )
    }
}