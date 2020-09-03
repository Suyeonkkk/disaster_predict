import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Header from './Header/header';
import Home from './Home/home';
import TyphoonInfo from './Disasters/Typhoon/typhoonInfo';
import RainInfo from './Disasters/Rain/rainInfo';
import SnowInfo from './Disasters/Snow/snowInfo';
import TyphoonHistory from './Disasters/Typhoon/typhoonHistory';

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
          <Route path='/TyphoonHistory' component={ TyphoonHistory } />
        </div>
      </Router>
    );
  }
}

export default App;
