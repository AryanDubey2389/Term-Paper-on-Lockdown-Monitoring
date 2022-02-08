import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import axios from 'axios';
import "bootstrap/dist/css/bootstrap.min.css"
import DatePicker from "react-datepicker";
import ArrowUpwardIcon from '@material-ui/icons/ArrowUpward';
import ArrowDownwardIcon from '@material-ui/icons/ArrowDownward';
import { ContactSupportOutlined, PrintDisabledTwoTone } from '@material-ui/icons';
var usem;
var cnt=0;

class ReProfile extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            email: '',
            title: '',
            maxposition:'',
            maxpost:'',
            date: null,
            skill: [],
            duration:'',
            salary:'',
            flag:'0',
            typeofjob:'Work From Home',
            usmail:'',
            deadline: new Date()
        }
        this.onChangetitle = this.onChangetitle.bind(this);
        this.onChangemaxapp = this.onChangemaxapp.bind(this);
        this.onChangemaxpos = this.onChangemaxpos.bind(this);
        this.onChangesalary = this.onChangesalary.bind(this);
        this.onChangetypeofjob = this.onChangetypeofjob.bind(this);
        this.onChangeduration = this.onChangeduration.bind(this);
        this.onChangedeadline = this.onChangedeadline.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    }

    componentDidMount() {
        var abc=JSON.parse(localStorage.getItem("id"))
        this.setState({flag:'1'})
        this.setState({usmail:abc.email})
    }
    onChangetitle(event) {
        this.setState({ title: event.target.value });
    }

    onChangemaxapp(event) {
        this.setState({ maxposition: event.target.value });
    }
    onChangemaxpos(event) {
        this.setState({ maxpost: event.target.value });
    }
    onChangesalary(event) {
        this.setState({ salary: event.target.value });
    }
     onChangetypeofjob(event) {
        this.setState({ typeofjob: event.target.value });
    }
    onChangeduration(event) {
        this.setState({ duration: event.target.value });
    }
    onChangedeadline(date) {
        this.setState({ deadline: date});
    }
    state= {showForm: false}
    
    sortClicked(){
        console.log(this.state);
    }

    sortChange(){
        var array = this.state.users;
        var flag = this.state.sortName;
        array.sort((var1, var2) => {
            if(var1.date != undefined && var2.date != undefined){
                return (1 - flag*2) * (new Date(var1.date) - new Date(var2.date));
            }
            else{
                return 1;
            }
          }); // Sort youngest first
        this.setState({
            users:array,
            sortName:!this.state.sortName,
        })
    }
    createUI() {
        return this.state.skill.map((el, i) =>
            <div key={i}>
                <input style = {{backgroundColor:"#505050",color:"yellow", width:"700px"}} type="text" value={el} onChange={this.handleChange.bind(this, i)} />
                <span class="tab"></span>
                <input style = {{backgroundColor:"#505050",color:"yellow", width:"200px"}} type='button' value='remove' onClick={this.removeClick.bind(this, i)} />
            </div>
        )
    }
    addClick() {
        this.setState(prevState => ({ skill: [...prevState.skill, ''] }))
    }
    handleChange(i, event) {
        let skill = [...this.state.skill];
        skill[i] = event.target.value;
        this.setState({skill})
    }
    removeClick(i) {
        let skill = [...this.state.skill];
        skill.splice(i, 1);
        this.setState({ skill });
    }
    showForm()
    {
        const my_style = {backgroundColor:"#505050",color:"yellow", width:"50%", borderBlockColor:"yellow"
        , borderBlockEndStyle:"groove"};
        return(
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
            <form onSubmit={this.onSubmit}>
                <div >
                    <label style = {{color:"Yellow", fontSize:"110%"}}> <br></br>Job title:<span class="tab2">
                        </span><span class="tab2"></span> <span class="tab"></span><span class="tab"></span>
                        <span class="tab"></span><span class="tab"></span></label>
                    <input placeholder = "Enter the title of the Job" style = {my_style} type="text" 
                            
                           value={this.state.title}
                           onChange={this.onChangetitle}
                           />
                </div>
                <br></br>
                <div >
                    <label style = {{color:"Yellow", fontSize:"110%"}}>Maximum Applications: <span class="tab2"></span>
                    <span class="tab2"></span><span class="tab2"></span><span class="tab3"></span>
                    <span class="tab4"></span></label>
                    <input  placeholder = "Enter the Maximum number of Applicants for the Job"style = {my_style} type="text"   
                           value={this.state.maxapp}
                           onChange={this.onChangemaxapp}
                           />  
                </div>
                <br></br>
                <div >
                    <label style = {{color:"Yellow", fontSize:"110%"}}>Maximum Positions:<span class="tab2">
                        </span><span class="tab2"></span> <span class="tab"></span><span class="tab3"></span></label>
                    <input placeholder = "Enter the Maximum number of Positions for the Job"style = {my_style} type="text"  
                           value={this.state.maxpost}
                           onChange={this.onChangemaxpos}
                           />  
                </div>
                <br></br>
                <div className="form-group">
                    <label style = {{color:"yellow"}}>Deadline </label>
                    <DatePicker
                        selected={ this.state.deadline }
                        onChange={ this.onChangedeadline }
                        showTimeSelect
                        timeFormat="HH:mm"
                        timeIntervals={20}
                        timeCaption="time"
                        dateFormat="MMMM d, yyyy h:mm aa"
                    />
                </div>
                <p style = {{color:"yellow"}}> Please enter the deadline in the given format</p>
                <br></br>
                <div >
                    <label style = {{color:"Yellow", fontSize:"110%"}}>Required Skills for the job <span class="tab3"></span>
                    <span class="tab3"></span><span class="tab4"></span></label>
                    {
                    this.createUI()
                    }
                    <input placeholder = "You can add the languages you know here"style = {{backgroundColor:"#505050",color:"yellow", width:"200px"}} type='button' 
                    value='Add' onClick={this.addClick.bind(this)} />
                </div>
                <br></br>
                <div >
                <label style = {{color:"Yellow", fontSize:"110%"}}>Job type <span class="tab"></span><span class="tab"></span>
                <span class="tab"></span><span class="tab2"></span><span class="tab"></span><span class="tab4"></span>
                <span class="tab4"></span><span class="tab4"></span></label>
               <select style = {{backgroundColor:"#505050", color:"yellow", width:"200px"}}value={this.state.typeofjob} onChange={this.onChangetypeofjob} >
               <option style = {{backgroundColor:"#505050", color:"yellow"}}name="FT">Full Time</option>
               <option style = {{backgroundColor:"#505050", color:"yellow"}}name="PT">Part Time</option>
               <option style = {{backgroundColor:"#505050", color:"yellow"}}name="WFH">Work From Home</option>
               </select> 
               </div>
               <br></br>
               <div >
                    <label style = {{color:"Yellow", fontSize:"110%"}}>Duration <span class="tab"></span>
                    <span class="tab"></span><span class="tab"></span><span class="tab"></span>
                    <span class="tab3"></span><span class="tab3"></span></label>
                    <input placeholder = "One day duration of the job (In hours)" style = {my_style} type="String" 
                            
                           value={this.state.duration}
                           onChange={this.onChangeduration}
                           />  
                </div>
                <br></br>
                <div >
                    <label style = {{color:"Yellow", fontSize:"110%"}}>Salary <span class="tab"></span><span class="tab"></span>
                    <span class="tab"></span><span class="tab"></span><span class="tab2"></span><span class="tab2"></span>
                    <span class="tab2"></span></label>
                    <input placeholder = "Salary given to the employee per month(In thousand)"style = {my_style} type="String"                      
                           value={this.state.salary}
                           onChange={this.onChangesalary}
                           />  
                </div>
                <div >
                    <label style = {{color:"Yellow", fontSize:"110%"}}>Bio: <span class="tab"></span><span class="tab"></span>
                    <span class="tab"></span><span class="tab2"></span><span class="tab"></span><span class="tab2"></span><span class="tab2"></span>
                    <span class="tab2"></span><span class="tab2"></span><span class="tab3"></span></label>
                    <input placeholder = "Write about you in max 250 words"style = {my_style} type="String"                      
                           className = "form-control"                           />  
                </div>
                <br></br>
                <div >
                    <br></br>
                    <input style = {{backgroundColor:"yellow",color:"black"}} type="submit" value="Register" className="btn btn-primary"/>
                </div>
                
            </form>
        </div>
        )
    }
    renderIcon(){
        if(this.state.sortName){
            return(
                <ArrowDownwardIcon/>
            )
        }
            return(
                <ArrowUpwardIcon/>
            )            
    }
    onSubmit(e) {
        e.preventDefault();
        const newUser = {
            email: this.state.usmail,
            title: this.state.title,
            maxposition:this.state.maxposition,
            maxpost:this.state.maxpost,
            date: null,
            skill: this.state.skill,
            duration:this.state.duration,
            salary:this.state.salary,
            typeofjob:this.state.typeofjob
        }
        console.log("before submit")
        console.log(newUser)
        axios.post('http://localhost:4000/user/jobregister', newUser)
             .then(res => {alert("You registered the job Succesfully");console.log(res.data)})
             .catch(err => { alert("Invalid Credentials")
              })

      /*  this.setState({
            name: '',
            email: '',
            date:null,
            Register_as: "Recruiter",
            Password: ''
        });*/
    }
    render() {
        if(this.state.flag!=='0')
        {
        return (
            
            <div>
                <style>{'.tab{margin-left:40px;}'}
                </style>
                <style>{'.tab2{margin-left:10px;}'}
                </style>
                <style>{'body { background-color: #202020; }'}</style>
                <style>{'body { background-color: #202020; }'}</style>
                <p style = {{color:"yellow", textAlign:"center", fontWeight:"bold", fontSize:"150%"}} >Welcome Recruiter</p>
                <br></br>
                <p style = {{color:"yellow", fontWeight:"bold", fontSize:"110%"}} > If you want to create a job click below on create new jobs</p>
                <button style = {{color:"yellow", textAlign:"center", backgroundColor:"#505050"}} onClick={()=>this.setState({showForm: true})}>Create New job</button>
                <br></br>
                {this.state.showForm ? this.showForm() : null}
                <br></br>
            </div>
        )
        }
        else{
            return(
                <div><p>Fetching info...</p></div>
            )
        }
        
    }
}

export default ReProfile;