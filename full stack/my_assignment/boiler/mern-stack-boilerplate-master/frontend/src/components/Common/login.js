import React, {Component} from 'react';
import { Redirect } from 'react-router-dom';
import axios from 'axios';
var varia=0;
export default class login extends Component
{
    constructor(props) {
        super(props);

        this.state = {
            email: '',
            Password: '',
            Register_as: 'Recruiter',
            errorm: ''
        }

        this.onChangeEmail = this.onChangeEmail.bind(this);
        this.onChangePassword = this.onChangePassword.bind(this);
        this.onChangeRegister_as = this.onChangeRegister_as.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    }
    
    onChangeEmail(event) {
        this.setState({ email: event.target.value });
    }
    onChangePassword(event) {
        this.setState({ Password: event.target.value });
    }
    onChangeRegister_as(event) {
        this.setState({ Register_as: event.target.value });
    }
    onSubmit(e) {
        e.preventDefault();

        const newUser = {
            email: this.state.email,        
            Password: this.state.Password,
            Register_as: this.state.Register_as
        }
        console.log(newUser)
        axios.post('http://localhost:4000/user/login', newUser)
             .then(res => {alert("Login Successful");
              console.log(res.data);
            /*   axios.get('http://localhost:4000/user')
             .then(res=>{
                res.findOne({newUser}).then(user=>{
                    console.log("entering")
                    varia = user
                })
             })*/
             localStorage.setItem("id",JSON.stringify(newUser))
             if(newUser.Register_as==='Applicant')
             {
             this.props.history.push({
                pathname: '/profile'
               // data: newUser
                });
            }
            else
            {
                this.props.history.push({
                    pathname: '/recruiterprofile'
                   // data: newUser
                    });

            }
             varia=1;})
             .catch(err => { 

                alert("Invalid Credentials")
               // alert(err.error)
              })

        this.setState({
            email: '',
            Password: '',
            Register_as: "Recruiter",
            errorm: ''
        });
        if(varia==1)
        {
            console.log("enter inside this")
           // return <Redirect to='/login' />
        }
    }
    render() {
        const my_style = {backgroundColor:"#505050",color:"yellow", width:"50%", 
        borderBlockColor:"yellow", borderBlockEndStyle:"groove"};
        const my_style2 = {backgroundColor:"#505050",color:"yellow", widht: "155%", margin:"0%"};
        
        return (
            <div>
                <style>{'.tab{margin-left:40px;}'}
                </style>
                <style>{'.tab2{margin-left:10px;}'}
                </style>
                <style>{'select {width: 2500px;margin: 10px;width:200px;margin: 100px;fontsize:130%}'}
                </style>
                <style>{'.tab{margin-left:40px;}'}
                </style>
                <style>{'body { background-color: #202020; }'}</style>
                <form onSubmit={this.onSubmit}>
                <div >
                    <label style = {{color:"Yellow", fontSize:"130%"}} className = "tab4">
                        You want to login as a Recruiter or an Applicant? Select one option.  
                        <span class="tab"></span></label>
                   <select style = {my_style2}value={this.state.Register_as} 
                   onChange={this.onChangeRegister_as} >
                   <option style = {my_style2}name="Recruiter">Recruiter</option>
                   <option style = {my_style2}name="Applicant">Applicant</option>
                   </select> 
                   </div>
                   <br></br>
                    <div >
                        <label style = {{color:"Yellow"}}>Email:  <span class="tab"></span> 
                        <span class="tab"></span></label>
                        <input placeholder = "Enter your registered email-id here"style = {my_style}
                        type="text"  value={this.state.email} onChange={this.onChangeEmail} />
                    </div>
                    <br></br>
                    <div >
                        <label style = {{color:"Yellow"}}>Password:  <span class="tab"></span></label>
                        <input placeholder = "Enter your password here" style = {my_style}
                        type="password" value={this.state.Password}  onChange={this.onChangePassword} />  
                    </div>
                    <br></br>
                    <div >
                        <input style = {{backgroundColor:"Yellow",color:"black"}}type="submit"
                         value="Login" className="btn btn-primary"/>
                    </div>
                    
                </form>
            </div>
        )
    }
}