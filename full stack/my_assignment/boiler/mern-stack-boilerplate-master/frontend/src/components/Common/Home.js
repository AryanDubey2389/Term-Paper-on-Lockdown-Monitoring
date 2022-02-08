import React, {Component} from 'react';
export default class Home extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            name:'',
            email:''
        }
    }

    componentDidMount() {

    }
    
    render() {
        const my_style = {
            color:"yellow", 
            position:"absolute", 
            top:"50%", left:"50%",
            marginRight : "-50%", 
            transform: "translateAliases(-50%,50%)"
        }
          return (
            <div>
                <style>{'body { background-color: #202020; }'}</style>
                <h1 style = {my_style}>
                    Hi There!<br/>
                    Welcome
                </h1>
            </div>
          );
    }
}