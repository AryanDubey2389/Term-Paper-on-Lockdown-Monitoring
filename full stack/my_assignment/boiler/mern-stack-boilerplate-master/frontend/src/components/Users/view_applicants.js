import React, {Component} from 'react';
import axios from 'axios';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import Divider from '@material-ui/core/Divider';
import Autocomplete from '@material-ui/lab/Autocomplete';
import IconButton from "@material-ui/core/IconButton";
import InputAdornment from "@material-ui/core/InputAdornment";
import SearchIcon from "@material-ui/icons/Search";
import UpwardIcon from '@material-ui/icons/ArrowUpward';
import DownwardIcon from '@material-ui/icons/ArrowDownward';

class recruiterviewapplicants extends Component {
    
    constructor(props) {
        super(props);
        this.state = {users: JSON.parse(localStorage.getItem("recruitview")),users1:[],sortedUsers: [], sortName:true,flag:false,filtusers:[],check:['IIT','BITs','NIT'],filttemp:[],namtemp:[]};
        this.renderIcon = this.renderIcon.bind(this);
        this.sortChange = this.sortChange.bind(this);
    }

    componentDidMount() {
        axios.get('http://localhost:4000/user')
             .then(response => {
                 this.setState({users1: response.data, sortedUsers:response.data});
                 for (var i=0;i<this.state.users.appleuser.length;i++)
                 {
                     for(var j=0;j<this.state.users1.length;j++)
                     {
                        if(this.state.users1[j].email===this.state.users.appleuser[i].emailuser)
                        {
                            
                            this.state.filtusers.push(this.state.users.appleuser[i])
                        }
                     }
                 }
                 this.setState({flag:true})
                 
             }).catch(function(error) {
                 console.log(error);
             })
             this.setState({flag:true})
             this.setState({filttemp:this.state.filtusers})
             
    }

    testfunc()
    {
        console.log("The button is working")
    }
    checksop(sop)
    {
        var show='Not found'
        show=sop
        alert(show)
        
    }
    sortChange(){
        var array = this.state.users;
        var flag = this.state.sortName;
        array.sort(function(a, b) {
            if(a.date != undefined && b.date != undefined){
                return (1 - flag*2) * (new Date(a.date) - new Date(b.date));
            }
            else{
                return 1;
            }
          });
        this.setState({
            users:array,
            sortName:!this.state.sortName,
        })
    }

    renderIcon(){
        if(this.state.sortName){
            return(
                <DownwardIcon/>
            )
        }
            return(
                <UpwardIcon/>
            )            
    }
    returnedu(filtrusers,idx)
    {
        var arrays=filtrusers.Education
        return(<div><TableBody>{this.state.check.map((user,ind) => (<TableRow key={ind}>{ind}</TableRow>))}</TableBody></div>)
        
    }
    render() {
        if(this.state.flag)
        {
        return (
            <div>
                <style>{'.tab{margin-left:40px;}'}
                </style>
                <style>{'.tab2{margin-left:10px;}'}
                </style>
                <style>{'body { background-color: #202020; }'}</style>
                <style>{'body { background-color: #303030; }'}</style>
                                        <h3 style = {{textAlign:"center", color:"yellow"}}>This is the list of applied users for this job</h3>                
                <Grid container>
                    <Grid item xs={12} md={3} lg={3}>
                        <List component="nav" aria-label="mailbox folders">
                            <Divider />
                        </List>
                    </Grid>
                    <Grid item xs={18} md={15} lg={15}>
                        <Paper>
                            <Table style = {{backgroundColor:"#505050", color:"yellow"}}size="small">
                                <TableHead style = {{backgroundColor:"#505050", color:"yellow"}}>
                                    <TableRow style = {{backgroundColor:"#505050", color:"yellow"}}>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}}> <Button onClick={this.sortChange}>{this.renderIcon()}</Button>Date of Apply</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}}><Button onClick={this.sortChange}>{this.renderIcon()}</Button>Name</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}}>Email_id of Applicant</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}}>Skills</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}}>Education(Institute Name,Startyear,Endyear)</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}}>SOP</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}}><Button style = {{backgroundColor:"#505050", color:"yellow"}}onClick={this.sortChange}>{this.renderIcon()}</Button>Rating</TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {this.state.filttemp.map((user,ind) => (
                                        <TableRow key={ind}>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}}>{user.dateapplied}</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}}>{user.name}</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}}>{user.emailuser}</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}}>{this.returnedu(this.state.filttemp[ind],ind)}</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}}>{this.returnedu(this.state.filttemp[ind],ind)}</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}} className='opration'><button  style = {{backgroundColor:"yellow", color:"black"}}onClick={()=>this.checksop(user.sop)} color='#4285F4'>Check SOP</button></TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}}></TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}} className='opration'><button  style = {{backgroundColor:"yellow", color:"black"}}onClick={()=>console.log("wo wala")} color='#4285F4'>Accept</button></TableCell>
                                            <TableCell style = {{backgroundColor:"#505050", color:"yellow"}} className='opration'><button  style = {{backgroundColor:"yellow", color:"black"}}onClick={()=>console.log("ye wala")} color='#4285F4'>Reject</button></TableCell>
                                        </TableRow>
                                        
                                ))}
                                </TableBody>
                          
                            </Table>
                        </Paper>               
                    </Grid>    
                </Grid>            
            </div>
        )
        }
        else
        {
            console.log("inside else")
            return(
                <div><p>Fetching Results...</p></div>
            )
        }
    }
}

export default recruiterviewapplicants;