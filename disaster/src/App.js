import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Header from './Header/header';
import Home from './Home/home';
import TyphoonInfo from './Typhoon/typhoonInfo';
import RainInfo from './Rain/rainInfo';
import SnowInfo from './Snow/snowInfo';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Header />
          <Route exact path="/" component={ Home } />
          <Route path="/SnowInfo" component={ SnowInfo } />
          <Route path="/RainInfo" component={ RainInfo } />
          <Route path="/TyphoonInfo" component={ TyphoonInfo } />
        </div>
      </Router>
    );
  }
}

export default App;
