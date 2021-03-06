import React from 'react'
import { Grid, Row, Col, Form, Panel, FormGroup, FormControl, ControlLabel, Button, Well, Alert } from 'react-bootstrap'
import { getJSON, ajax, serialize } from 'jquery'
import { getCookie } from '../../../csrf/DjangoCSRFToken'
import TagMultiSelect from '../../TagMultiSelect'



const ItemCreationForm = React.createClass({
  getInitialState() {
    return {
      name: "",
      quantity: 0,
      model_no: "",
      description: "",
      tags: [],
      custom_fields: [],

      showCreatedSuccess: false,
      showErrorMessage: false,
      errorMessage: ""
    }
  },

  componentWillMount() {
    this.getCustomFields()
  },

  getCustomFields() {
    var url = "/api/fields/"
    var _this = this
    getJSON(url, null, function(data) {
      data.map( (field, i) => {
        var custom_field_entry = {"name": field.name, "value": "", "field_type": field.field_type}
        _this.setState({
          custom_fields: _this.state.custom_fields.concat([custom_field_entry])
        })
      })
    })
  },

  handleTagSelection(tagsSelected) {
    this.setState({tags: tagsSelected.split(",")});
  },

  getShortTextField(field_name, presentation_name, i) {
    return (
      <FormGroup key={field_name} bsSize="small">
        <Col sm={2} componentClass={ControlLabel}>
          {presentation_name}
        </Col>
        <Col sm={9}>
          <FormControl type="text"
                     value={this.state.custom_fields[i].value}
                     name={field_name}
                     onChange={this.handleCustomFieldChange.bind(this, i, field_name)} />
        </Col>
      </FormGroup>
    )
  },

  getLongTextField(field_name, presentation_name, i) {
    return (
      <FormGroup key={field_name} bsSize="small">
        <Col sm={2} componentClass={ControlLabel}>
          {presentation_name}
        </Col>
        <Col sm={9}>
          <FormControl type="text"
                     style={{resize: "vertical", height:"100px"}}
                     componentClass={"textarea"}
                     value={this.state.custom_fields[i].value}
                     name={field_name}
                     onChange={this.handleCustomFieldChange.bind(this, i, field_name)} />
        </Col>
      </FormGroup>
    )
  },

  getIntegerField(field_name, presentation_name, min, step, i) {
    return (
      <FormGroup key={field_name} bsSize="small">
        <Col sm={2} componentClass={ControlLabel}>
          {presentation_name}
        </Col>
        <Col sm={9}>
          <FormControl type="number"
                     min={min}
                     step={step}
                     value={this.state.custom_fields[i].value}
                     name={field_name}
                     onChange={this.handleCustomFieldChange.bind(this, i, field_name)} />
        </Col>
      </FormGroup>
    )
  },

  getFloatField(field_name, presentation_name, i){
    return (
      <FormGroup key={field_name} bsSize="small">
        <Col sm={2} componentClass={ControlLabel}>
          {presentation_name}
        </Col>
        <Col sm={9}>
          <FormControl type="number"
                     value={this.state.custom_fields[i].value}
                     name={field_name}
                     onChange={this.handleCustomFieldChange.bind(this, i, field_name)} />
        </Col>
      </FormGroup>
    )
  },

  getCustomFieldForms() {
    return this.state.custom_fields.map( (field, i) => {

      var field_name = field.name
      var is_private = field.private
      var field_type = field.field_type

      switch(field_type) {
        case "Single":
          return this.getShortTextField(field_name, field_name, i)
          break;
        case "Multi":
          return this.getLongTextField(field_name, field_name, i)
          break;
        case "Int":
          return this.getIntegerField(field_name, field_name, 0, 1, i)
          break;
        case "Float":
          return this.getFloatField(field_name, field_name, i)
          break
        default:
          return null
      }
    })
  },

  getSuccessMessage() {
    var url = "/app/inventory/" + this.state.createdName + "/"
    var ret = this.state.showCreatedSuccess ? (
      <Row>
        <Col sm={12}>
          <Well bsSize="large">Item <a href={url}>{this.state.createdName}</a> successfully created!</Well>
        </Col>
      </Row>) : (null)
    return ret
  },

  getErrorMessage() {
    return this.state.showErrorMessage ? (
      <Row>
        <Col sm={12}>
          <Alert bsStyle="danger" bsSize="small">{this.state.errorMessage}</Alert>
        </Col>
      </Row>
    ) : null
  },

  validateData(data) {
    console.log(data)
    if (data.name.length < 1) {
      return false
    }
    if (Number(data.quantity) < 0) {
      return false
    }
    return true
  },

  createItem() {
    var _this = this;
    var item_name = this.state.name;
    var data = {
        name: _this.state.name,
        quantity: _this.state.quantity,
        model_no: _this.state.model_no,
        description: _this.state.description,
        tags: _this.state.tags,
      }
    var valid = this.validateData(data)
    console.log(valid)
    if (valid) {
      ajax({
        url:"/api/items/",
        contentType: "application/json",
        type: "POST",
        beforeSend: function(request) {
          request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        data: JSON.stringify({
          name: _this.state.name,
          quantity: _this.state.quantity,
          model_no: _this.state.model_no,
          description: _this.state.description,
          tags: _this.state.tags,
        }),
        success:function(response){
          for (var i=0; i<_this.state.custom_fields.length; i++) {
            var cf = _this.state.custom_fields[i]
            var url = "/api/items/" + item_name + "/fields/" + cf.name + "/"
            ajax({
              url: url,
              contentType: "application/json",
              type: "PUT",
              data: JSON.stringify({
                value: cf.value
              }),
              beforeSend: function(request) {
                request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
              },
              success:function(response){},
              complete:function(){},
              error:function (xhr, textStatus, thrownError){
                console.log(xhr);
                console.log(textStatus);
                console.log(thrownError);
              }
            });
          }
          _this.setState({
            name: "",
            quantity: 0,
            model_no: "",
            description: "",
            tags: [],
            custom_fields: [],
            showCreatedSuccess: true,
            createdName: item_name,
            showErrorMessage: false,
            errorMessage: ""
          }, _this.getCustomFields())
        },
        complete:function(){},
        error:function (xhr, textStatus, thrownError){
          var response = xhr.responseJSON
          console.log(xhr)
          _this.setState({
            showCreatedSuccess: false,
            createdName: "",
            showErrorMessage: true,
            errorMessage: "An error occurred."
          })
        }
      });
    } else {
      this.setState({
        showCreatedSuccess: false,
        createdName: "",
        showErrorMessage: true,
        errorMessage: "Ensure that name is not blank and quantity is a positive integer."
      })
    }
  },

  handleItemFieldChange(e) {
    e.preventDefault()
    this.setState({
      [e.target.name]: e.target.value
    })
  },

  handleCustomFieldChange(i, name, e) {
    var custom_fields = this.state.custom_fields
    custom_fields[i].value = e.target.value
    this.setState({
      custom_fields: custom_fields
    })
  },

  render() {
    return (
      <Grid fluid>

        <Row>
          <Col sm={12}>
            <h3>Item Creation</h3>
            <hr />
            <p>
              Use this form to add new items to the inventory.
            </p>
            <br />
          </Col>
        </Row>

        { this.getSuccessMessage() }
        { this.getErrorMessage() }

        <Row>
          <Col sm={12}>
            <Form horizontal>

              <Panel>
                <h4>Create an item</h4>
                <hr />

                <FormGroup bsSize="small">
                  <Col componentClass={ControlLabel} sm={2}>
                    Name
                  </Col>
                  <Col sm={9} >
                    <FormControl
                      type="text"
                      name="name"
                      value={this.state.name}
                      onChange={this.handleItemFieldChange}
                    />
                  </Col>
                </FormGroup>

                <FormGroup bsSize="small">
                  <Col componentClass={ControlLabel} sm={2}>
                    Model No.
                  </Col>
                  <Col sm={9} >
                    <FormControl
                      type="text"
                      name="model_no"
                      value={this.state.model_no}
                      onChange={this.handleItemFieldChange}
                    />
                  </Col>
                </FormGroup>

                <FormGroup bsSize="small">
                  <Col componentClass={ControlLabel} sm={2}>
                    Quantity
                  </Col>
                  <Col sm={2} >
                    <FormControl
                      type="number"
                      name="quantity"
                      min={0} step={1}
                      value={this.state.quantity}
                      onChange={this.handleItemFieldChange}
                    />
                  </Col>
                </FormGroup>

                <FormGroup bsSize="small">
                  <Col componentClass={ControlLabel} sm={2}>
                    Description
                  </Col>
                  <Col sm={9} >
                    <FormControl
                      type="text"
                      style={{resize: "vertical", height:"100px"}}
                      componentClass={"textarea"}
                      name="description"
                      value={this.state.description}
                      onChange={this.handleItemFieldChange}
                    />
                  </Col>
                </FormGroup>

                <FormGroup bsSize="small">
                  <Col componentClass={ControlLabel} sm={2}>
                    Tags
                  </Col>
                  <Col sm={9} >
                    <TagMultiSelect tagsSelected={this.state.tags} tagHandler={this.handleTagSelection}/>
                  </Col>
                </FormGroup>

                { this.getCustomFieldForms() }

                <FormGroup bsSize="small">
                  <Col smOffset={2} sm={2}>
                    <Button bsSize="small" type="button" bsStyle="info" onClick={this.createItem}>
                      Submit
                    </Button>
                  </Col>
                </FormGroup>
              </Panel>

            </Form>
          </Col>

        </Row>
      </Grid>
    )
  }
})

export default ItemCreationForm
