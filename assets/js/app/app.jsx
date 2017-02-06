import React from 'react'
import { render } from 'react-dom'
import { Router, Route, browserHistory, IndexRoute } from 'react-router'
import KipNav from './KipNav'
import Home from './Home'
import Requests from './Requests'
import DisbursementContainer from './admin/disbursementcontainer'
import CartContainer from './cart/CartContainer'
import Profile from './profile'
import {getJSON} from 'jquery'


function getRouteIfAdmin(userData) {
  console.log(userData)
  return userData.is_staff ? <Route path="admin" component={DisbursementContainer} admin={userData}/> : null
}

function initialize(userData) {
  render((
    <Router history={browserHistory}>
      <Route path="app" component={KipNav} user={userData}>
        <IndexRoute component={Home} user={userData}/>
        <Route path="requests" component={Requests} user={userData} />
        <Route path="profile" component={Profile} user={userData}/>
        <Route path="cart" component={CartContainer} user={userData} />
        {getRouteIfAdmin(userData)}
      </Route>
    </Router>),
    document.getElementById('root'));
}


getJSON("/api/users/current/.json", function(data) {
   var user = data
   initialize(user)
})
