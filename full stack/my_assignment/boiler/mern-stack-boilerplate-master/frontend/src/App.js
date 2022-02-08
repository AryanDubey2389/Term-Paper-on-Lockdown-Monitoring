import React from 'react';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css"

import Register from './components/Common/Register'
import Navbar from './components/templates/Navbar'
import UsersList from './components/Users/UsersList'
import Home from './components/Common/Home'
import sop from './components/Users/SOP'
import editprof from './components/Users/profile_edit'
import Profile from './components/Users/Profile'
import Profiles_Navbar from './components/templates/Navbar_for_profile.js'
import Recruiters_Navbar from './components/templates/Navbar_for_recruiter.js'
import login from './components/Common/login'
import RecruiterProfile from './components/Users/Profile_Recruiter'
import myapplication from './components/Users/myapplication'
import recruiterjobs from './components/Users/recruiterjobs'
import editjob from './components/Users/job_edit'
import recruiterviewapplicant from './components/Users/view_applicants'
import Contact_us from './components/templates/bgcolor'

function App() { 
  const Default_Routes = () => {
  return (
      <div>
        <Navbar/>
        <br></br>
        <br></br>
        <Route path="/" exact component={Home}/>
        <Route path="/users" exact component={UsersList}/>
        <Route path="/register" component={Register}/>
        <Route path="/login" component ={login}/>   
        <Route path="/contact" component ={Contact_us}/>
      </div>
  )
  };
  const Profile_Routes = () => {
    return (
        <div>
          <Profiles_Navbar/>
          <br></br>
          <br></br>
          <Route path="/profile/sop" component = {sop}/>
          <Route path="/profile/edit" component = {editprof}/>
          <Route path="/profile/users" exact component={UsersList}/>
          <Route path="/profile/myapplications" component = {myapplication}/>
          <Route path="/profile" exact component ={Profile}/>
          <Route path="/profile/contact" exact component ={Contact_us}/>
        </div>
    )
  }
  const AnotherRoutes = () => {
    return (
        <div>
          <Recruiters_Navbar/>
          <br></br>
          <br></br>
          <Route path="/recruiterprofile/recruiterjobs/editjob" component = {editjob}/>
          <Route path="/recruiterprofile/recruiterjobs" exact component = {recruiterjobs}/>
          <Route path="/recruiterprofile/recruiterjobs/recruiterviewapplicant" component = {recruiterviewapplicant}/>
          <Route path="/recruiterprofile/edit" component = {editprof}/>
          <Route path="/recruiterprofile" exact component ={RecruiterProfile}/>
          <Route path="/recruiterprofile/recruiterjobs/users" exact component={UsersList}/>
          <Route path="/recruiterprofile/recruiterjobs/contact" exact component={Contact_us}/>
        </div>
    )
  }
    return(
      <Router>
        <Switch>
          <Route exact component = {Profile_Routes} path="/profile" />
          <Route exact component = {Profile_Routes} path="/profile/contact" />
          <Route exact component = {Profile_Routes} path="/profile/sop" />
          <Route exact component = {Profile_Routes} path="/profile/edit" />
          <Route exact component = {Profile_Routes} path="/profile/myapplications" />
          <Route exact component = {Profile_Routes} path="/profile/users" />
          <Route exact component = {AnotherRoutes} path="/recruiterprofile/recruiterjobs/recruiterviewapplicant" />
          <Route exact component = {AnotherRoutes} path="/recruiterprofile" />
          <Route exact component = {AnotherRoutes} path="/recruiterprofile/recruiterjobs" />
          <Route exact component = {AnotherRoutes} path="/recruiterprofile/recruiterjobs/editjob" />
          <Route exact component = {AnotherRoutes} path="/recruiterprofile/recruiterjobs/users" />
          <Route exact component = {AnotherRoutes} path="/recruiterprofile/recruiterjobs/contact" />
          <Route component = {Default_Routes} path="/" />
        </Switch>
      </Router>
    )
  };

export default App;
