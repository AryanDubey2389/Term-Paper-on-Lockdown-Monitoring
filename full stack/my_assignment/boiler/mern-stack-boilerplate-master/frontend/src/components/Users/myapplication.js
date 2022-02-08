import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import axios from 'axios';
import TableCell from '@material-ui/core/TableCell';
import TableRow from '@material-ui/core/TableRow';
export default class myapp extends Component {
    
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
        
    }
    componentDidMount() {

       var abc=JSON.parse(localStorage.getItem("id"))
       axios.get('http://localhost:4000/user')
       .then(response => {
           this.setState({users: response.data});
           this.setState({flag:'1'})
            for(var i=0;i<this.state.users.length;i++)
            {
                if(this.state.users[i].email===abc.email)
                {
           this.setState(prevState => ({
            arr: [...prevState.arr, this.state.users[i]]
          }))}
        }
        for(var i=0;i<this.state.arr[0].Appliedjob.length;i++)
        {
            this.setState(prevState => ({
                arrnew: [...prevState.arrnew, this.state.arr[0].Appliedjob[i]]
              }))
        //
        }
       }) .catch(function(error) {
           console.log(error);
       })
    }
    render()
    {
        if(this.state.flag==='0')
        {
        return(<div><p style = {{font:"130%", color:"yellow"}}>Welcome to my applications</p></div>)
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
                                            <TableCell style = {{color:"yellow", font:"350%"}}>Sr no. </TableCell>
                                            <TableCell style = {{color:"yellow", font:"350%"}}>Date of Joining </TableCell>
                                            <TableCell style = {{color:"yellow", font:"350%"}}>Title of Job</TableCell>
                                            <TableCell style = {{color:"yellow", font:"350%"}}>Salary offered</TableCell>
                                            <TableCell style = {{color:"yellow", font:"350%"}}>Name of recruiter </TableCell>
                                            <TableCell style = {{color:"yellow", font:"350%"}}>Status of my application</TableCell>
                                            <TableCell style = {{color:"yellow", font:"350%"}}>Rating of the job</TableCell>
                </TableRow>
                <p>{this.state.arrnew.map((user,ind) => (
                                        <TableRow key={ind}>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{ind+1}</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{user.dateofjoining}</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{user.jobtitle}</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{user.salary}</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{user.nameofrecruiter} </TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{user.status}</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}}>{user.rating}</TableCell>
                                            <TableCell style = {{color:"yellow", font:"120%"}} className='opration'>

                    </TableCell>
                                        </TableRow>
                                ))}</p>
        </div>
                
             )
        }
    }
}
