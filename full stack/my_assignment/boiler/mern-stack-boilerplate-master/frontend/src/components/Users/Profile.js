import React, {Component} from 'react';
import axios from 'axios';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import "bootstrap/dist/css/bootstrap.min.css"

import TableBody from '@material-ui/core/TableBody';
import Button from '@material-ui/core/Button';
import TableRow from '@material-ui/core/TableRow';
import Table from '@material-ui/core/Table';

import ListItem from '@material-ui/core/ListItem';
import Divider from '@material-ui/core/Divider';
import TextField from '@material-ui/core/TextField';
import List from '@material-ui/core/List';

import InputAdornment from "@material-ui/core/InputAdornment";
import InputLabel from '@material-ui/core/InputLabel';
import Autocomplete from '@material-ui/lab/Autocomplete';
import IconButton from "@material-ui/core/IconButton";

import SearchIcon from "@material-ui/icons/Search";
import UpwardIcon from '@material-ui/icons/ArrowUpward';
import MenuItem from '@material-ui/core/MenuItem';
import Select from '@material-ui/core/Select';
import DownwardIcon from '@material-ui/icons/ArrowDownward';
import Fuse from 'fuse.js'

class Profile extends Component {
    
    constructor(props) {
        super(props);
        this.renderIcondate = this.renderIcondate.bind(this);
        this.state = {users: [],jobs:[],title:'',titlearr:[],temparr:[],sortName:true,searchvalue:'',maxsal:'1000000000',minsal:'-1',temp:"",_id:'',vari:false,flag:'0',taruser:'Loading',title:'',name:'',email:'',maxposition:'',maxpost:'',duration:0,typeofjob:'',appleuser:[],showfrm:'0',redirect:'',sortName:true,mnflg:false,mxflg:false};
        this.sortClicked = this.sortClicked.bind(this);
        this.renderIconrate = this.renderIconrate.bind(this);
        this.renderIcontitle = this.renderIcontitle.bind(this);
        this.renderIconsalary = this.renderIconsalary.bind(this);
        this.sortChange = this.sortChange.bind(this);
        this.sortrate = this.sortrate.bind(this);
        this.setsalfilt=this.setsalfilt.bind(this);
        this.sortsalary = this.sortsalary.bind(this);
        this.sortduration = this.sortduration.bind(this);
 
        this.setsaldefault=this.setsaldefault.bind(this);
        this.setminsal=this.setminsal.bind(this);
        this.setmaxsal=this.setmaxsal.bind(this);
        this.submitForm = this.submitForm.bind(this);
  
        this.Fuzzy = this.Fuzzy.bind(this);
        this.jobtypedrop = this.jobtypedrop.bind(this)
        this.durationtypedrop = this.durationtypedrop.bind(this)
    }
    state= {showForm: false}
    
    componentDidMount() {
        this.setState({})
        this.setState({temp : JSON.parse(localStorage.getItem("id"))})
        Promise.all([
            axios.get('http://localhost:4000/user'),
            axios.get('http://localhost:4000/user/jobregister1')
        ])
        .then(([userResponse, reposResponse]) => {
            this.setState({users : userResponse.data, jobs : reposResponse.data});
            this.setState({vari:true})
            for(var i=0;i<this.state.jobs.length;i++)
            {
               this.state.titlearr.push("apply")
            }
            this.setState.flag=1
            this.setState({temparr:this.state.jobs})
        });
        
    }
    Fuzzy(e) {
        const fuse = new Fuse(this.state.temparr, {
            keys:
                ['title']
            , includeScore: true

        })
        this.state.searchvalue = e.target.value;
        var ans=''
        const results = fuse.search(this.state.searchvalue);
        if(this.state.searchvalue)
        {
            ans=results.map(result => result.item)
        }
        else{
            ans=this.state.jobs
        }
        this.setState({ temparr: ans });
    }
    
    showForm()
    {
        this.setState({showfrm:1})
        return (
          <div> 
           <form onSubmit={this.onSubmit}>
                    <div className="form-group">
                        <label> Please enter SOP </label>
                        <input type="text" 
                               className="form-control" 
                               value={this.state.sop}
                               onChange={this.onChangesop}
                               />
                    </div>
                    <div className="form-group">
                        <input type="submit" value="submit sop" className="btn btn-primary"/>
                    </div>
                    
            </form>
           </div>
          );
      }
    submitForm(idx,newid){
        localStorage.setItem("forsop",JSON.stringify(newid))
        this.props.history.push('/profile/sop') 
      }

    fuzzy()
    {
        console.log("fuzzy")
    }

    sortClicked(){
        console.log(this.state);
    }
    sortChange(){
        var flag = this.state.sortName;
        var array = this.state.temparr;
        array.sort((var1, var2) => {
            if(var1.date != undefined){ 
                if(var2.date != undefined){
                return (1 - flag*2) * (new Date(var1.date) - new Date(var2.date));
                }
            }
            else{
                return 1;
            }
          }); 
        this.setState({
            jobs:array,
            sortName:!this.state.sortName,
        })
    }
    sortduration(){
        var flag = this.state.sortName;
        var array = this.state.temparr;
        array.sort((var1, var2) =>{
            if(var1.duration != undefined){ 
                if(var2.duration!= undefined){
                return (1 - flag*2) * (var1.duration - var2.duration);
                }
            }
            else{
                return 1;
            }
          }); 
        this.setState({
            jobs:array,
            sortName:!this.state.sortName,
        })
    }
    sortsalary(){
        var flag = this.state.sortName;
        var array = this.state.temparr;
        array.sort((var1, var2) => {
            if(var1.salary != undefined){
                if(var2.salary!= undefined){
                return (1 - flag*2) * (var1.salary - var2.salary);
                }
            }
            else{
                return 1;
            }
          }); 
        this.setState({
            jobs:array,
            sortName:!this.state.sortName,
        })
    }
    
    sortrate(){
        var array = this.state.temparr;
        var flag = this.state.sortName;
        array.sort((var1, var2) =>{
            if(var1.duration != undefined){
                if(var2.duration!= undefined){
                return (1 - flag*2) * (var1.duration - var2.duration);
                }
            }
            else{
                return 1;
            }
          }); 
        this.setState({
            jobs:array,
            sortName:!this.state.sortName,
        })
    }

    renderIconrate(){
        if(this.state.sortName == false){
            return(
                <UpwardIcon/>
            )
        }
            return(
                <DownwardIcon/>
            )            
    }
    renderIcondate(){
        if(this.state.sortName == false){
            return(
                <UpwardIcon/>
            )
        }
            return(
                <DownwardIcon/>
            )            
    }
    renderIconsalary(){
        if(this.state.sortName){
            return(
                <UpwardIcon/>
            )
        }
            return(
                <DownwardIcon/>  
            )            
    }
    renderIcontitle(){
        if(this.state.sortName == false){
            return(
                <UpwardIcon/>
            )
        }
            return(
                <DownwardIcon/>
            )            
    }
    renderIconrating(){
        if(this.state.sortName){
            return(
                <UpwardIcon/>
            )
        }
            return(
                <DownwardIcon/>  
            )           
    }
    renderIconduration(){
        if(this.state.sortName){
            return(
                <UpwardIcon/>
            )
        }
            return(
                <DownwardIcon/>
            )            
    }
    setsalfilt(){

            var array = this.state.temparr.filter(varia=>parseInt(varia.salary)>=parseInt(this.state.minsal))
            var array1 = array.filter(varia=>parseInt(varia.salary)<=parseInt(this.state.maxsal))

            this.setState({temparr:array1})
        
   
    }
    setminsal(e){
        this.setState({minsal:e.target.value})
        this.setState({mnflg:true})
    }
    setmaxsal(e){
        this.setState({maxsal:e.target.value})
        this.setState({mxflg:true})
    }
 
    setsaldefault(e)
    {
        this.setState({temparr:this.state.jobs})
        this.setState({minsal:'0'})
        this.setState({maxsal:'1000000000'})

    }
    jobtypedrop(e)
    {
        var array = this.state.temparr.filter(varia=>(varia.typeofjob)===(e.target.value))
        this.setState({temparr:array})
    }
    durationtypedrop(e)
    {
        var array = this.state.temparr.filter(varia=>parseInt(varia.duration)<parseInt(e.target.value))
        this.setState({temparr:array})
    }
    btntxt(ind,user)
    {
        var initval = "Click Here to Apply"
            for(var j=0;j<user.appleuser.length;j++)
            {
                if((user.appleuser[j]).emailuser===(this.state.temp.email))
                {
                    initval=user.appleuser[j].status;
                }
            }

        return(<TableCell className='opration'><button  onClick={()=>this.submitForm(ind,user)}  style = {{backgroundColor:"yellow"}} color='#4285F4'>{initval}</button></TableCell>)
        
    }
    render() {
  
        if(this.state.vari == true)
        {
       
        return (
            
            <div>
                <h3 style = {{textAlign:"center", color:"Yellow"}}>This is the list of all available jobs for you.</h3>
                <style>{'.tab{margin-left:40px;}'}
                </style>
                <style>{'body { background-color: #303030; }'}</style>
            <Grid container>
            <Grid item xs={12} md={3} lg={3}>
                <List component="nav" aria-label="mailbox folders">
                    <ListItem text>
                    <h3 style = {{color:"Yellow"}}>Filters</h3>
                    </ListItem>
                </List>
            </Grid>
                <Grid item xs={12} md={9} lg={9}>
                <List component="nav" aria-label="mailbox folders" onChange={this.Fuzzy}>
                    <TextField placeholder = "Write the title of the job here"
                    id="standard-basic" 
                    label="Search by Job Title here" 
                    fullWidth={true}   
                    InputProps={{
                        endAdornment: (
                            <InputAdornment>
                                <IconButton>
                                    <SearchIcon />
                                </IconButton>
                            </InputAdornment>
                        )}}
                    />
                </List>
                </Grid>
            </Grid>
            <p style = {{color:"yellow", textAlign:"center"}}>Note: After every filter click on set things to default to make it again default.</p>
            <Grid container>
                <Grid item xs={12} md={3} lg={3}>
                    <List component="nav" aria-label="mailbox folders">

                        <ListItem button>
                            <form noValidate autoComplete="off" >
                                <label style = {{color:"yellow"}}>Salary</label>
                                <TextField id="standard-basic"  placeholder = "Minimum Salary"label="Min Salary" fullWidth={true} onChange={this.setminsal} />
                                <TextField id="standard-basic"  placeholder = "Maximum Salary"label="Max Salary" fullWidth={true} onChange={this.setmaxsal}/>
                                <br></br><br></br>
                                <Button style = {{backgroundColor:"yellow",color:"black",borderBlockEndColor:"black"}}value="submit" onClick={this.setsalfilt}>Filter by given data</Button>
                                <br></br><br></br>
                                <Button style = {{backgroundColor:"yellow",color:"black",borderBlockEndColor:"black"}}value="submit" onClick={this.setsaldefault}>Set things to default</Button>

                            </form>                                                                
                        </ListItem>
        
                        <Divider />
                        <ListItem button divider>
                            <Autocomplete style = {{backgroundColor:"#505050",color:"yellow"}} id="combo-box-demo"
                                options={this.state.users} getOptionLabel={(option) => option.name} style={{ width: 300 }}
                                renderInput={(params) => <TextField {...params} label="Select Names" variant="outlined" />}
                            />
                        </ListItem>
                    </List>
                </Grid>
                <Grid style = {{backgroundColor:"#505050",color:"yellow"}}item xs={12} md={9} lg={9}>
                    <Paper>
                        <Table style = {{backgroundColor:"#505050",color:"yellow"}} size="small">
                            
                        <TableHead style = {{backgroundColor:"#505050",color:"yellow"}}>
                                <TableRow style = {{backgroundColor:"#505050",color:"yellow"}}>
                                <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}><span class="tab"></span><span class="tab"></span></TableCell>
                                <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}><span class="tab"></span><span class="tab"></span></TableCell>
                                <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}><span class="tab"></span><span class="tab"></span></TableCell>
                                <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}><span class="tab"></span><span class="tab"></span></TableCell>
                                <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>
                                        <InputLabel placeholder = "Lesser than 0"style = {{backgroundColor:"#505050",color:"yellow"}}id="label">Filter job by duration</InputLabel>
                                            <Select placeholder = "Lesser than 0"style = {{backgroundColor:"#505050",color:"yellow",width:"150px"}}labelId="label" 
                                            id="select" value="duration" onClick={this.durationtypedrop}>
                                            <MenuItem style = {{backgroundColor:"#505050",color:"yellow"}}value="1">Lesser than 1</MenuItem>
                                            <MenuItem style = {{backgroundColor:"#505050",color:"yellow"}}value="2">Lesser than 2</MenuItem>
                                            <MenuItem style = {{backgroundColor:"#505050",color:"yellow"}}value="3">Lesser than 3</MenuItem>
                                            <MenuItem style = {{backgroundColor:"#505050",color:"yellow"}}value="4">Lesser than 4</MenuItem>
                                            <MenuItem style = {{backgroundColor:"#505050",color:"yellow"}}value="5">Lesser than 5</MenuItem>
                                            <MenuItem style = {{backgroundColor:"#505050",color:"yellow"}}value="6">Lesser than 6</MenuItem>
                                            <MenuItem style = {{backgroundColor:"#505050",color:"yellow"}}value="7">Lesser than 7</MenuItem>
                                        </Select></TableCell>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>
                                        <InputLabel style = {{backgroundColor:"#505050",color:"yellow"}}id="label">Filter by type of job
                                        <span class="tab"></span> <span class="tab"></span></InputLabel>
                                            <Select style = {{backgroundColor:"#505050",color:"yellow",width:"150px"}}labelId="label" 
                                            id="select" value="jobtype" onClick={this.jobtypedrop}>
                                            <MenuItem style = {{backgroundColor:"#505050",color:"yellow"}} value="Full Time">Full Time</MenuItem>
                                            <MenuItem style = {{backgroundColor:"#505050",color:"yellow"}} value="Part Time">Part Time</MenuItem>
                                            <MenuItem style = {{backgroundColor:"#505050",color:"yellow"}} value="Work From Home">Work From Home</MenuItem>
                                           
                                            
                                        </Select></TableCell>
                                        
                                </TableRow>
                            </TableHead>
                            
                            <TableHead>
                                <TableRow>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}> <Button onClick={this.sortChange}>{this.renderIcondate()}</Button>Date</TableCell>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>Title of job</TableCell>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>Email id of recruiter</TableCell>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}><Button onClick={this.sortsalary}>{this.renderIconsalary()}</Button>Salary</TableCell>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}><Button onClick={this.sortduration}>{this.renderIconduration()}</Button>Duration</TableCell>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>Job Type</TableCell>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}><Button onClick={this.sortrate}>{this.renderIconrate()}</Button>Rating</TableCell>
                                        
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {this.state.temparr.map((user,ind) => (
                                    <TableRow key={ind}>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>{user.date}</TableCell>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>{user.title}</TableCell>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>{user.email}</TableCell>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>{user.salary}</TableCell>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>{user.duration}</TableCell>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>{user.typeofjob}</TableCell>
                                        <TableCell style = {{backgroundColor:"#505050",color:"yellow"}}>{user.rating}</TableCell>
                                        {this.btntxt(ind,user)}
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
            return(
                <p>Loading Please wait ...</p>
            )
        }
    }
}

export default Profile;