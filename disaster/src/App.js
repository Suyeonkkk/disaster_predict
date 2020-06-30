import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Header from './Header/header';
import Home from './Home/home';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Header />
          <Route exact path="/" component={ Home } />{/*
          <Route path="/Search" component={  } />*/}
        </div>
      </Router>
    );
  }
}

export default App;
