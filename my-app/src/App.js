import React from 'react';
import logo from './logo.svg';
import './App.css';

import {Home} from './components/Home'
import {About} from './components/About'
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';


function App() {
  return (
    <div className="App">
       <Router>
    <div>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/about">About</Link></li>
     
      </ul>

      <hr />

      <Route exact path="/" component={Home} />
      <Route path="/about" component={About} />
 
    </div>
  </Router>
  
    </div>
  );
}

export default App;
