const mongoose = require("mongoose");
const Schema = mongoose.Schema;

// Create Schema
const UserSchema = new Schema({
	name: {
		type: String,
		required: true
	},
	date:{
		type: Date,
		required: false
	},
	email: {
		type: String,
		required: true
	},
	Password:{
		type:String,
		required:false
	},
	Register_as:{
		type:String,
		required:false
	},
	Gender:{
		type:String,
		requried: false
	},
	Education:[
		{
			institute_name:{
				type :String,
				required:false
			},
			start_year:{
				type : String,
				required:false
			},
			end_year:{
				type:String,
				required:false
			}

		}
	],
Appliedjob:[
	{
		jobid:{
			type:String,
			required:false
		},
		jobtitle:{
			type:String,
			required:false
		},
		dateofjoining:{
			type:String,
			required:false
		},
		salary:{
			type:String,
			required:false
		},
		nameofrecruiter:{
			type:String,
			required:false
		},
		status:{
			type:String,
			required:false
		},
		rating:{
			type:String,
			required:false
		}

	}
]

});

module.exports = User = mongoose.model("Users", UserSchema);
