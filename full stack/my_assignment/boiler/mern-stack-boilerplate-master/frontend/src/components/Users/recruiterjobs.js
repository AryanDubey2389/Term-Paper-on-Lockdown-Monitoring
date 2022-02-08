import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import axios from 'axios';
import TableCell from '@material-ui/core/TableCell';
import TableRow from '@material-ui/core/TableRow';
export default class recruiterjobs extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            applied:[{
            jobid:'',
            jobtitle:'',
            dateofjoining:'',
            salary:'',
            nameofrecruiter:'',
            status:'',
            rating:''
            }],
            users: [],
            arr:[],
            arrnew:[],
            flag:'0',
            vari:''
        };
        this.editform = this.editform.bind(this);
        
    }
    componentDidMount() {

       var abc=JSON.parse(localStorage.getItem("id"))
       axios.get('http://localhost:4000/user/jobregister1')
       .then(response => {
           this.setState({users: response.data});
           this.setState({flag:'1'})
           console.log(this.state.users)
            for(var i=0;i<this.state.users.length;i++)
            {
                if(this.state.users[i].email===abc.email)
                {
           this.setState(prevState => ({
            arr: [...prevState.arr, this.state.users[i]]
          }))}
        }
       })
       .catch(function(error) {
           console.log(error);
       })
    }
    editform(idx,user)
    {
        localStorage.setItem("jobrecruid",JSON.stringify(user._id))
        this.props.history.push("/recruiterprofile/recruiterjobs/editjob")
        
    }
    deleteform()
    {
        console.log(" form deleted")
    }
    viewapplicant(idx,user)
    {
        localStorage.setItem("recruitview",JSON.stringify(user))
        this.props.history.push("/recruiterprofile/recruiterjobs/recruiterviewapplicant")
    }
    render()
    {
        
        if(this.state.flag==='0')
        {
        return(<div><p>Please wait while loading...</p></div>)
        }
        else
        {

        return(<div>
            <style>{'.tab{margin-left:40px;}'}
                </style>
                <style>{'.tab2{margin-left:10px;}'}
                </style>
                <style>{'body { background-color: #202020; }'}</style>
            <style>{'body { background-color: #202020; }'}</style>
         <TableRow>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>Date and Time of Posting </TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>Title of the Job</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>Salary offered</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%",margin:"10px"}}>Maximum of Applicants </TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>Remaining Positions </TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>Status of my application</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%",marginLeft:"1000px"}}>Rating of the job</TableCell>
                </TableRow>
                <p>{this.state.arr.map((user,ind) => (
                                        <TableRow key={ind}>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{user.date}</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{user.title}</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{user.salary}</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{user.nameofrecruiter} </TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%",width:"250px"}}>{user.maxposition} </TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{user.maxpost} </TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{user.status}</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{user.rating}</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}} className='opration'>
                                            <button style = {{fontSize:"14px"}}onClick={()=>this.editform(ind,user)}>Edit</button>
                                            <button style = {{fontSize:"14px"}}onClick={()=>this.deleteform()}>Delete</button>
                                            <button style = {{fontSize:"14px"}}onClick={()=>this.viewapplicant(ind,user)}>View Applicants</button>
                    </TableCell>
                                        </TableRow>
                                ))}</p>
        </div>
                
             )
        }
    }
}
