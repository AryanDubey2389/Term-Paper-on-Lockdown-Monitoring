var express = require("express");
const { body, validationResult } = require('express-validator');
var router = express.Router();

router.get("/", (req, res) =>{
    User.find((err, users) =>{
      try{
        res.json(users);
      }catch(err){
			console.log(err);
		}
	})
});
router.get("/getu" , function(req, res) {
  //const varemail = req.email
  //User.findOne({ varemail }).then(user=>{
  //    res.json(user)
  //})
  var email=req.body.email
  User.findOne({email}).then(user=>{
    res.send(user)
  })
/*  User.find(function(err, users) {
  if (err) {
    console.log(err);
  } else {
    res.json(users);
  }
})*/
});
const User = require("../models/Users");
const jobs = require("../models/jobs");

router.post("/editjob", (req, res) => {
  const email=req.body.id
  jobs.findById(email,(err,user)=>{ 
    console.log(user)
    const id=user._id
    console.log("req.body", req.body);
    let temp = user
    console.log(temp)
    if(req.body.maxpost!==''){
      temp.maxpost=req.body.maxpost
    }  
    else{
      temp.maxpost=user.maxpost
      console.log(temp.maxpost)
      
    }
    console.log(temp)
    if(req.body.maxposition!==''){
      temp.maxposition=req.body.maxposition 
      console.log(temp.maxposition)
    }  
    else{
      temp.maxposition=user.maxposition
    }
    if(req.body.deadline!=='') {
      temp.deadline=req.body.deadline
    }
    else{
      temp.deadline=user.deadline
    }  

  jobs.findByIdAndUpdate(email,temp, (  err,temp)=> {
    try{
      res.send(temp);
    }catch(err){
      es.status(500).send(err);
    }
     
  });
})
});
router.post("/update", (req, res) => {
  let email=req.body.email
    let id = req.body.id;
    
      User.findOne({ email }).then(user=>{
      let temp={
        name:user.name,
        emailuser:req.body.email,
        dateapplied:Date.now(), 
        sop:req.body.sop,
        skill:user.skill,
        Education: user.Education
        
      }
      jobs.findByIdAndUpdate(id, { $push:{
      appleuser:temp}}).then(user=>res.send(user))
      })
    
  })
  router.post("/insrtjob", (req, res) => {
    let email = req.body.email
      User.findOne({ email }).then(user=>{
        jobs.findById(req.body.id,function(err,docs){
      
      let temp={
        salary:docs.salary,
        nameofrecruiter:docs.name,
        jobtitle:docs.title,
        jobid:req.body.id,
        dateofjoining:'',
        rating:"Unrated",
        status:"applied"
        
      }
      console.log(temp)
      User.findByIdAndUpdate(user._id, { $push:{
      Appliedjob:temp}}).then(user=>res.send(user))
      })
    })
  })
  router.post("/updateapplicant", (req, res) => {
    console.log("req.body", req.body);
    console.log("inside updateappliant route")
    const email=req.body.email
    User.findOne({ email }).then(user=>{
      const id=user._id
      var inventory = {
        name:'',
        Register_as: user.Register_as,
        Password: '',
        skill:'',
        Education: [{institutename:'',startyear:'',endyear:''}],
        
      };
      console.log(id)
      if(req.body.Password!=='') {
        inventory.Password=req.body.Password
        console.log(inventory.Password);
      }  
      else{
        inventory.Password=user.Password
        console.log(inventory.Password);
      }
      if(req.body.name!==''){
        inventory.name=req.body.name
        console.log(inventory.name);
      }  
      else{
        inventory.name=user.name
        console.log(inventory.name);
      }
     
      if(req.body.Education.length!==0) {
        inventory.Education=req.body.Education
        console.log(inventory.Education);
      }
      else{
        inventory.Education=user.Education
        console.log(inventory.Education);

      }  
  
    User.findByIdAndUpdate(id, inventory,(err,inventory
    )=> {
      try{
        res.send(inventory);
      }catch(err){
        console.log("err", err);
      }
    });
  })
  });
  
router.get("/jobregister1", (req, res) =>{
    jobs.find((err, users) =>{
      try{
        res.json(users);
      }catch(err){
        console.log(err);
      }
	})
});
router.post("/jobregister", body('email').isEmail(),(req, res) => {
    
    const errors = validationResult(req);
    const email = req.body.email
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }    
        const newUser = new jobs({
        title: req.body.title,
        name: req.body.name,
        email: req.body.email,
        maxposition: req.body.maxposition,
        maxpost: req.body.maxpost,
        date: Date.now(),
        duration: req.body.duration,
        typeofjob: req.body.typeofjob,
        salary: req.body.salary

    });
    newUser.save()
        .then(newUser => {
            return res.status(200).json(newUser);
            console.log(vari)
        })
        .catch(err => {
          console.log("here comes the error")
            return res.status(400).send(err);
        }); 
})
router.post("/register", body('email').isEmail(),(req, res) => {
    const email = req.body.email
    const password = req.body.password
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }
    User.findOne({ email }).then(user=>{
    if(!user)
    {
        const newUser = new User({
        name: req.body.name,
        Password: req.body.Password,
        date: req.body.date,
        email: req.body.email,
       
        Education:req.body.Education,
        Register_as:req.body.Register_as
        
    });

    newUser.save()
        .then(user => {
            return res.status.json(user);
        }).catch(err => {
            return res.status.send(err);
        });
    }
    else
    {
        return res.status(400).json({
            error: "Email already exists"
        })
        
    }
    })
})
router.post("/login", (req, res) => {
  const Password = req.body.Password;

    const email = req.body.email;
	User.findOne({ email }).then(user => {
    const Register_as=req.body.Register_as;
		if (!user) {
			return res.status(404).json({
				error: "Email not found",
			});
        }
        else{
            const matching_pass=user.Password
            const regisp=user.Register_as;
            if(matching_pass==Password && regisp==Register_as)
            {

                return res.status(200).json({
                    error: "Successfully Logged in"
                })
            
            }
            else{
                console.log("Invalid Credentials")
                return res.status(404).json({
                    error: "Invalid Credentials. Please try again"
                });
            }
        }
	});
});

module.exports = router;