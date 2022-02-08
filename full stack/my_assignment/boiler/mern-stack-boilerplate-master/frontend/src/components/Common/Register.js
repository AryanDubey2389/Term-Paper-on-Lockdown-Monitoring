import React, {Component} from 'react';
import axios from 'axios';
var flag=0
export default class Register extends Component {
    
    constructor(props) {
        super(props);

        this.state = {
            name: '',
            email: '',
            Password: '',
            Register_as: "Recruiter",
            Gender:'',
            Education: [
                {
                    institutename:'',
                    startyear:'',
                    endyear:''
                }
            ],
            date:null
        }

        this.onChangeUsername = this.onChangeUsername.bind(this);
        this.onChangeEmail = this.onChangeEmail.bind(this);
        this.onChangePassword = this.onChangePassword.bind(this);
        this.onChangeRegister_as = this.onChangeRegister_as.bind(this);
        this.onChangeGender = this.onChangeGender.bind(this);
      //  this.onChangeEducation = this.onChangeEducation(this);
        this.onSubmit = this.onSubmit.bind(this);
    }
    handleInputChange = (index, e) => {

        const Education = [...this.state.Education];
        const { name, value } = e.target;
        Education[index][name] = value;
        this.setState({ Education });
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
    onChangeGender(event) {
        this.setState({ Password: event.target.value });
    }
     onChangeRegister_as(event) {
        this.setState({ Register_as: event.target.value });
    }

    onSubmit(e) {
        e.preventDefault();

        const newUser = {
            name: this.state.name,     
            Gender:this.state.Gender,
            date: Date.now(),
            Register_as: this.state.Register_as,
            email: this.state.email,     
            Password: this.state.Password,
            Education: this.state.Education
        }
        axios.post('http://localhost:4000/user/register', newUser)
             .then(res => {alert("Congrats you successfully registered")})
             .catch(err => { alert("Invalid Credentials")
              })

        this.setState({
            name: '',
            email: '',
            date:null,
            Gender:'',
            Register_as: "Recruiter",
            Password: ''
        });
    }
    render() {
        const my_style = {backgroundColor:"#505050",color:"yellow", width:"50%", borderBlockColor:"yellow", borderBlockEndStyle:"groove"};
        const my_style2 = {backgroundColor:"#505050",color:"yellow", widht: "155%", margin:"0%"};
        return (
            <div>
                <style>{'.tab{margin-left:40px;}'}
                </style>
                <style>{'.tab2{margin-left:10px;}'}
                </style>
                <style>{'body { background-color: #202020; }'}</style>
                
              {(() => {
                if (this.state.Register_as=="Recruiter") {
                  return (
                    <div>
                        <style>{'select {width: 2500px;margin: 10px;width:200px;margin: 100px;fontsize:130%}'}</style>
                <form onSubmit={this.onSubmit}>
                <div className="form-group">
                    <label style = {{color:"Yellow", fontSize:"130%"}} className = "tab4">You want to register as a Recruiter or an Applicant? Select one option. <span class="tab"></span></label>
                   <select style = {my_style2}value={this.state.Register_as} onChange={this.onChangeRegister_as} >
                   <option style = {my_style2}name="Recruiter">Recruiter</option>
                   <option style = {my_style2}name="Applicant">Applicant</option>
                   </select> 
                   </div>
                    <div >
                        <label for = "username" style = {{color:"Yellow", fontSize:"120%"}}>Username: <span class="tab"></span></label>
                        <input name="Username" placeholder="Enter your Username here"style = {my_style}type="text" 
                               value={this.state.name}
                               onChange={this.onChangeUsername}
                               />
                    </div>
                    <br></br>
                    <div >
                        <label style = {{color:"Yellow", fontSize:"120%"}}>Email: <span class="tab"></span><span class="tab"><span class="tab2"></span></span></label>
                        <input name="Email" placeholder="Enter an unique email-id here"style = {my_style}type="text" 
                               value={this.state.email}
                               onChange={this.onChangeEmail}
                               />  
                    </div>
                    <br></br>
                    <div className="form-group">
                        <label style = {{color:"Yellow", fontSize:"120%"}}>Password: <span class="tab"></span></label>
                        <input name="Password" placeholder="Enter your Password here"style = {my_style}type="password"   
                               value={this.state.Password}
                               onChange={this.onChangePassword}
                               />  
                    </div>
                    <br></br>
                    <div className="form-group">
                        <input style = {{backgroundColor:"yellow",color:"black"}} type="submit" value="Register" className="btn btn-primary"/>
                    </div>
                    
                </form>
            </div>
                  )
                }
                 else {
                  return (
                    <div>
                        <style>{'select {width: 2500px;margin: 10px;width:200px;margin: 100px;fontsize:130%}'}</style>
                        <style>{'body { background-color: #202020; }'}</style>
                <form onSubmit={this.onSubmit}>
                <div className="form-group">
                    <label style = {{color:"Yellow", fontSize:"130%"}} className = "tab4">You want to register as a Recruiter or an Applicant? Select one option.  <span class="tab"></span></label>
                   <select style = {my_style2}value={this.state.Register_as} onChange={this.onChangeRegister_as} >
                   <option style = {my_style2}name="Recruiter">Recruiter</option>
                   <option style = {my_style2}name="Applicant">Applicant</option>
                   </select> 
                   </div>
                    <div className="form-group">
                        <label style = {{color:"Yellow"}}>Username: <span class="tab"></span></label>
                        <input name="Username" placeholder="Enter your Username here"style = {my_style}type="text" 
                                value={this.state.name}
                               onChange={this.onChangeUsername}
                               />
                    </div>
                    <div className="form-group">
                        <label style = {{color:"Yellow"}}>Email: <span class="tab"></span><span class="tab"></span></label>
                        <input name="Email" placeholder="Enter an unique email-id here"style = {my_style}type="text" 
                               value={this.state.email}
                               onChange={this.onChangeEmail}
                               />
                    </div>
                    <div className="form-group">
                    <label style = {{color:"Yellow"}}>Gender<span class="tab"></span><span class="tab"></span></label>
                   <select style = {{backgroundColor:"#505050",color:"yellow", widht: "155%", margin:"1%"}}value={this.state.Gender} onChange={this.onChangeGender} >
                   <option name="Male">Male</option>
                   <option name="Female">Female</option>
                   <option name="Others">Others</option>
                   </select> 
                   </div>
                    <div className="form-group">
                        <label style = {{color:"Yellow"}}>Skills: <span class="tab"></span><span class="tab"></span></label>
                        <input name="Skills" placeholder="Write your Skills here like the languages you learned"style = {my_style}type="text" 
                                
                               value={this.state.skill}
                               onChange={this.onChangeSkill}
                               />
                    </div>
                    <div className="form-group">
                        <label style = {{color:"Yellow"}}>Password: <span class="tab"></span></label>
                        <input name="Password" placeholder="Enter your Password here"style = {my_style}type="password" 
                                
                               value={this.state.Password}
                               onChange={this.onChangePassword}
                               />  
                    </div>
                    <div>
                        <label style = {{color:"Yellow"}}>Education: </label>
                        {
                                this.state.Education.map((x, i) => {
                                    return (
                                        <div className="box">
                                            <input style = {{width:"24%", backgroundColor:"#505050", color:"yellow"}}name="institutename" placeholder="institutename" value={x.institutename} onChange={this.handleInputChange.bind(this, i)} />
                                            <input style = {{width:"10%", backgroundColor:"#505050", color:"yellow"}}name="startyear" placeholder="startyear" value={x.startyear} onChange={this.handleInputChange.bind(this, i)} />
                                            <input style = {{width:"10%", backgroundColor:"#505050", color:"yellow"}}name="endyear" placeholder="endyear" value={x.endyear} onChange={this.handleInputChange.bind(this, i)} />
                                            {this.state.Education.length !== 1 && <input type='button' value='remove' onClick={this.handleRemoveRow.bind(this, i)} />}
                                            <div className="btn-box">
                                                {this.state.Education.length - 1 === i && <input type='button' value='add more' onClick={this.handleAddRow.bind(this)} style={{ color:"black",backgroundColor:"yellow", marginLeft: 0 }} />}
                                            </div>

                                        </div>
                                    );
                                })
                            }
                    </div>
                    <br></br><br></br>
                    <div className="form-group">
                        <input style = {{backgroundColor:"yellow",color:"black"}}type="submit" value="Register" className="btn btn-primary"/>
                    </div>
                    
                </form>
            </div>
                 
                  )
                }
              })()}
            </div>
          )
    }
}