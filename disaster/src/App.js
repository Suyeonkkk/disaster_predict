import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Header from './Header/header';
import Home from './Home/home';
import TyphoonInfo from './Disasters/Typhoon/typhoonInfo';
import TyphoonHistory from './Disasters/Typhoon/typhoonHistory';
import RainInfo from './Disasters/Rain/rainInfo';
import RainLocation from './Disasters/Rain/rainLocation';
import SnowInfo from './Disasters/Snow/snowInfo';
import SnowLocation from './Disasters/Snow/snowLocation';

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
          <Route path='/SnowLocation' component={ SnowLocation } />
          <Route path='/RainLocation' component={ RainLocation } />
        </div>
      </Router>
    );
  }
}

export default App;
