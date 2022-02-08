import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import axios from 'axios';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import "bootstrap/dist/css/bootstrap.min.css"
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Slider from '@material-ui/core/Slider';
export default class editprof extends Component {
    constructor(props) {
        super(props);

        this.state = {
            id:'',
            name: '',
            email: '',
            Password: '',
            Register_as: "Recruiter",
            Education: [
                {
                    institutename:'',
                    startyear:'',
                    endyear:''
                }
            ],
            temp:'0',
            date:null
        }

        this.onChangeUsername = this.onChangeUsername.bind(this);
        this.onChangeEmail = this.onChangeEmail.bind(this);
        this.onChangePassword = this.onChangePassword.bind(this);
        this.onChangeRegister_as = this.onChangeRegister_as.bind(this);
      //  this.onChangeEducation = this.onChangeEducation(this);
        this.onSubmit = this.onSubmit.bind(this);
    }
    componentDidMount() {
        var abc=JSON.parse(localStorage.getItem("id"))
        this.setState({temp:'1'})
    }
    handleInputChange = (index, e) => {

        console.log(e.target.value);
        const { name, value } = e.target;
        const Education = [...this.state.Education];
        console.log("inside handleinput")
        console.log(name,value)
        Education[index][name] = value;
        this.setState({ Education });
        for(var i=0;i<Education.length;i++)
        {
            console.log(Education[i])
        }
    }
    handleAddRow = () => {
        const item = {
            institutename: '',
            startyear: '',
            endyear: ''

        }
        this.setState({
            Education: [...this.state.Education, item]
        });
    }
    handleRemoveRow = (id) => {
        let Education = [...this.state.Education]
        Education.splice(id, 1);
        this.setState({
            Education
        });
    }
    onChangeUsername(event) {
        this.setState({ name: event.target.value });
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
        var abc=JSON.parse(localStorage.getItem("id"))
        console.log("checking abc")
        console.log(abc)
        const newUser = {
            name: this.state.name,
            email: abc.email,        
            date: Date.now(),
            Register_as: this.state.Register_as,
            Password: this.state.Password,
            Education: this.state.Education
        }
        console.log("before submit")
        console.log(newUser.email)
        axios.post('http://localhost:4000/user/updateapplicant', newUser)
             .then(res => {alert("Created\t" + res.data.name+res.data.Register_as+res.data.Password);console.log(res.data)})
             .catch(err => { alert("Invalid Credentials")
              })

        this.setState({
            name: '',
            email: '',
            date:null,
            Register_as: "Recruiter",
            Password: ''
        });
    }
    render() {
       // console.log("register")
        const reg=this.state.temp
        if(this.state.temp==1)
        {
            const my_style = {backgroundColor:"#505050",color:"yellow", width:"50%", borderBlockColor:"yellow", borderBlockEndStyle:"groove"};
            const my_style2 = {backgroundColor:"#505050",color:"yellow", widht: "155%", margin:"0%"};
        return (
            <div>
                <style>{'.tab{margin-left:40px;}'}
                </style>
                <style>{'.tab2{margin-left:10px;}'}
                </style>
                <style>{'.tab3{margin-left:5px;}'}
                </style>
                <style>{'.tab4{margin-left:1px;}'}
                </style>
                <style>{'body { background-color: #202020; }'}</style>
                <style>{'body { background-color: #202020; }'}</style>
                <p style = {{color:"Yellow", fontSize:"130%"}} >Fill only those fields which you want to edit.</p>
                    <div>
                <form onSubmit={this.onSubmit}>
                    <div >
                        <label style = {{color:"Yellow", fontSize:"120%"}}>Username:  <span class="tab"></span></label>
                        <input style = {my_style} type="text"   
                               value={this.state.name}
                               onChange={this.onChangeUsername}
                               />
                    </div>
                    <br></br>
                    <div >
                        <label style = {{color:"Yellow", fontSize:"120%"}}>Education: </label>
                        {
                                this.state.Education.map((x, i) => {
                                    return (
                                        <div className="box">
                                            <input style = {{backgroundColor:"#505050",color:"yellow",width:"24%"}} name="institutename" placeholder="institutename" 
                                            value={x.institutename} onChange={this.handleInputChange.bind(this, i)} />
                                            <input style = {{backgroundColor:"#505050",color:"yellow",width:"12%"}}name="startyear" placeholder="startyear" 
                                            value={x.startyear} onChange={this.handleInputChange.bind(this, i)} />
                                            <input style = {{backgroundColor:"#505050",color:"yellow",width:"12%"}}name="endyear" placeholder="endyear" 
                                            value={x.endyear} onChange={this.handleInputChange.bind(this, i)} />
                                            {this.state.Education.length !== 1 && <input  style={{ backgroundColor:"yellow",color:"black",width:"10%"}}
                                            type='button' value='Delete this row' onClick={this.handleRemoveRow.bind(this, i)} />}
                                            <div className="btn-box">
                                                {this.state.Education.length - 1 === i && <input type='button' value='Add' 
                                                onClick={this.handleAddRow.bind(this)} style={{ backgroundColor:"yellow",color:"black",width:"5%"}} />}
                                            </div>
                                        </div>
                                    );
                                })
                            }
                    </div>
                    <br></br>
                    <div >
                        <label style = {{color:"Yellow", fontSize:"120%"}}>Skills:  <span class="tab"></span>
                        <span class="tab"></span> <span class="tab3"> </span><span class="tab3"></span>
                        <span class="tab3"> </span></label>
                        <input style = {my_style} type="text" 
                                
                               value={this.state.skill}
                               onChange={this.onChangeSkill}
                               />
                    </div>
                    <br></br>
                    <div >
                        <label style = {{color:"Yellow", fontSize:"120%"}}>Password:  <span class="tab"></span></label>
                        <input style = {my_style} type="password" 
                                
                               value={this.state.Password}
                               onChange={this.onChangePassword}
                               />  
                    </div>
                    <br></br>
                    <div >
                        <input style = {{backgroundColor:"yellow",color:"black",width:"100px"}} type="submit" value="Edit" className="btn btn-primary"/>
                    </div>
                    
                </form>
            </div>
                 
                  )
            </div>
    
    )}
    else{
        return(
            <div><p>Fetching info..</p></div>
        )
    }
    }

}