import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import axios from 'axios';
export default class editjob extends Component {
    
    constructor(props) {
        super(props);
        this.state = {id:'',maxpost:'',maxposition:'',deadline:''};
        this.onSubmit = this.onSubmit.bind(this);
        this.onChangemaxapp = this.onChangemaxapp.bind(this);
        this.onChangemaxpos = this.onChangemaxpos.bind(this);
        
    }
    componentDidMount() {
       // console.log("reomve error")
       var abc = JSON.parse(localStorage.getItem("jobrecruid"))
       this.setState({id:abc})
    
    }
    onChangemaxpos(event) {
        this.setState({ maxpost: event.target.value });
    }
    onChangemaxapp(event) {
        this.setState({ maxposition: event.target.value });
    }
    onChangesop(event) {
   
    }
    onSubmit(e) {
        e.preventDefault();
       // console.log(appleuser)
        const newUser = {
            id:this.state.id,
            maxposition: this.state.maxposition,
            maxpost:this.state.maxpost,
            deadline:''
        }
        axios.post('http://localhost:4000/user/editjob', newUser)
             .then(res => {alert("Created\t" + res.data.name+res.data.Register_as+res.data.Password);console.log(res.data)})
             .catch(err => { alert("Invalid Credentials")
              })
            }
    render()
    {
        return(
        <div>
            

            <style>{'.tab{margin-left:40px;}'}
                </style>
                <style>{'.tab2{margin-left:10px;}'}
                </style>
                <style>{'body { background-color: #202020; }'}</style>
            <h3 style = {{color:"yellow"}}>Fill any one of the following fields to update the values of the selected job</h3>
            <form onSubmit={this.onSubmit}>
                <div className="form-group">
                    <label style = {{color:"Yellow", fontSize:"120%"}}>Maximum Applications </label>
                    <input style = {{backgroundColor:"#505050",color:"yellow", width:"50%"}}type="text" 
                           className="form-control" 
                           value={this.state.maxapp}
                           onChange={this.onChangemaxapp}
                           />  
                </div>
                <div className="form-group">
                    <label style = {{color:"Yellow", fontSize:"120%"}}>Maximum Positions </label>
                    <input style = {{backgroundColor:"#505050",color:"yellow", width:"50%"}}type="text" 
                           className="form-control" 
                           value={this.state.maxpost}
                           onChange={this.onChangemaxpos}
                           />  
                           
                </div>
                <div className="form-group">
                    <label style = {{color:"Yellow", fontSize:"120%"}}>Deadline </label>
                    <input style = {{backgroundColor:"#505050",color:"yellow", width:"50%"}}type="password" 
                           className="form-control" 
                           value={this.state.deadline}
                           onChange={this.onChangedeadline}
                           />  
                </div>
                <div className="form-group">
                    <input type="submit" value="Update" className="btn btn-primary"/>
                </div>
                
            </form>
        </div>
        )
        
    }
}
