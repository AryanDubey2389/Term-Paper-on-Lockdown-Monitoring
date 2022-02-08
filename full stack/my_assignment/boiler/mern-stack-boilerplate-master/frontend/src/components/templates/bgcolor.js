import React, {Component} from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
export default class Home extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            name:'',
            email:''
        }
    }

    componentDidMount() {

    }
    
    render() {
        const my_style = {
            color:"yellow", 
            position:"absolute", 
        }
          return (
            <div>
                <style>{'body { background-color: #202020; }'}</style>
                <p style = {my_style}>
                    <a style = {{fontSize:"40px", textAlign:"center",fontWeight:"bold"}}>Thanks for visiting the website</a> 
                    <br></br><br></br>If you are facing any problem or need any help please share with us.
                    <br></br>  Our contact details are given below. <br></br> <br></br>
                    Email_id - aryandubey@research.iiit.ac.in<br></br>
                    Contact number - 6204000406
                </p>
            </div>
          );
    }
}