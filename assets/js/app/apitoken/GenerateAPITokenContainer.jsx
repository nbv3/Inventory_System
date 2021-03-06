import React,  { Component } from 'react'
import { Grid, Button, Row, Col, Well } from 'react-bootstrap'
import $ from "jquery"

class GenerateAPITokenContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      current_token: "",
    }
    // this.handleChange = this.handleChange.bind(this);

    this.handleClick = this.handleClick.bind(this);
    this.getToken = this.getToken.bind(this);

  }


  getToken(){
    var thisObj = this;
    $.getJSON("/api/apitoken/", function(data){
      thisObj.setState({current_token : data.token});
    });
  }

  handleClick(event){
    event.preventDefault();
    this.getToken();
  }


  render(){
    return(
      <div>
        <h3>API Token Generator</h3>
        <hr></hr>
        <Row>
          <Col xs={3}>
            <Button onClick={this.handleClick}>Generate Token</Button>
          </Col>
          <Col xs={3}>
            <p>API Token:</p>
          </Col>
          <Col xs={6}>
            <p>{this.state.current_token}</p>
          </Col>
          
        </Row>
      </div>

    );
  }
}


export default GenerateAPITokenContainer
