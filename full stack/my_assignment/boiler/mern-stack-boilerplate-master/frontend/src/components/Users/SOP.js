import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import axios from 'axios';
export default class sop extends Component {
    
    constructor(props) {
        super(props);
        this.state = {temp:'',flag:'0',usrmail:'',sup:'jjj',sop:'',psh:''};
        this.onChangesop = this.onChangesop.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    }
    onChangesop(event) {
        const obj2 = this.state.usrmail
        const obj1 = event.target.value
        this.setState({sop:obj1})
    }

    componentDidMount() {
        let abc=JSON.parse(localStorage.getItem("id"))
        let abd=JSON.parse(localStorage.getItem("forsop"))
        this.setState({flag:1})
        this.setState({temp:abd})
        this.setState({usrmail:abc.email})
    }
    onSubmit(e) {
        e.preventDefault();
        const newUser = {
            id:this.state.temp._id,
            email: this.state.usrmail,
            sop:this.state.sop
        }
        axios.post('http://localhost:4000/user/update', newUser)
             .then(res => {alert("You Successfully Applied for the job");console.log(res.data)})
             .catch(err => { alert("Invalid Credentials")
              })

        this.setState({
           id:this.state.temp._id,
           sup:''
        });
    }
    render()
    {
        console.log("inside",this.state.flag)
        if(this.state.flag!=='0')
        {
            console.log("enter if")
            var obj1 = this.state.temp
            console.log(obj1.email)
            return(
                <div>
                    <h1 style = {{color:"yellow",textAlign:"center"}}>You need to enter SOP to apply for the job.</h1>
                    <style>{'.tab{margin-left:40px;}'}
                </style>
                <br></br><br></br>
                <style>{'body { background-color: #303030; }'}</style>
                   <form onSubmit={this.onSubmit}>
                   <div >
                        <label style = {{color:"yellow", font:"120%"}}>Enter SOP here <span class="tab"></span><span class="tab"></span></label>
                        <input placeholder = "Write the SOP here" style = {{color:"yellow", backgroundColor:"#505050", borderBlockColor:"yellow",width:"50%"}}type="text" 
                               value={this.setState.sup}
                               onChange={this.onChangesop}
                               />  
                    </div>
                    <br></br>
                    <div>
                        <input style = {{backgroundColor:"yellow", color:"black"}}type="submit" value="Submit" className="btn btn-primary"/>
                    </div></form>
                </div>
            )       
        
        }
        else{
            console.log("enter else")
            return(
                <div>
                    <p>Loading Please wait..</p>
                </div>
            )
        }
    }
}
