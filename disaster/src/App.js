import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Header from './Header/header';
import Home from './Home/home';
import SearchRegion from './Search/searchRegion';
import SearchDate from './Search/searchDate';
import DisasterInfo from './Info/disasterInfo';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Header />
          <Route exact path="/" component={ Home } />
          <Route path="/SearchRegion" component={ SearchRegion } />
          <Route path="/SearchDate" component={ SearchDate } />
          <Route path="/DisasterInfo" component={ DisasterInfo } />
        </div>
      </Router>
    );
  }
}

export default App;
