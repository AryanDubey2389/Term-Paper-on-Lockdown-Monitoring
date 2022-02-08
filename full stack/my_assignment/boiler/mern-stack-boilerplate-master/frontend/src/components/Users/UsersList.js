import React, {Component} from 'react';
import axios from 'axios';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import TableBody from '@material-ui/core/TableBody';
import Button from '@material-ui/core/Button';
import TableRow from '@material-ui/core/TableRow';
import Table from '@material-ui/core/Table';
import UpwardIcon from '@material-ui/icons/ArrowUpward';
import DownwardIcon from '@material-ui/icons/ArrowDownward';

class UsersList extends Component {
    
    constructor(props) {
        super(props);
        this.state = {users: [],sortedUsers: [], sortName:true};
        this.renderIcon = this.renderIcon.bind(this);
        this.sortChange = this.sortChange.bind(this);
    }

    componentDidMount() {
        axios.get('http://localhost:4000/user')
             .then(response => {
                 this.setState({users: response.data, sortedUsers:response.data});
             }).catch(function(error) {
                 console.log(error);
             })
    }

    sortChange(){

        let flag = this.state.sortName;
        let array = this.state.users;
        array.sort( (var1, var2) => {
            if(var1.date != undefined && var2.date != undefined){
                return (1 - flag*2) * (new Date(var1.date) - new Date(var2.date));
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
        if(this.state.sortName == false){
            return(
                <UpwardIcon/>  
            )}
        return(
            <DownwardIcon/>
        )
    }

    render() {
        return (
            <div>
                <style>{'.tab{margin-left:40px;}'}
                </style>
                <style>{'.tab2{margin-left:10px;}'}
                </style>
                <style>{'body { background-color: #202020; }'}</style>
                <style>{'body { background-color: #303030; }'}</style>
                <h2 style = {{color:"yellow"}}> These are the list of users on our website.</h2>
                <Grid container>
                    <Grid item xs={40} md={26} lg={26}>
                    </Grid>
                    <Grid item xs={40} md={26} lg={26}>
                        <Paper>
                            <Table size="large">
                                <TableHead>
                                    <TableRow>
                                            <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>Sr no.</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}> <Button onClick={this.sortChange}>{this.renderIcon()}</Button>Date-Time of Registration</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>Name</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>Email-Id</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>Registred As</TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {this.state.users.map((user,ind) => (
                                        <TableRow key={ind}>
                                            <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>{ind+1}</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>{user.date}</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>{user.name}</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>{user.email}</TableCell>
                                            <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>{user.Register_as}</TableCell>
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
}

export default UsersList;