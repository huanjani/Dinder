import React, { Component } from 'react';
import logo from './pan-icon-3.png';
import DataViz from './components/DataViz';
import './App.css';

class App extends Component {
  constructor(props) {
    super();
    this.state = {
    }
  }

  render() {
    // const BASE_URL = 'http://localhost:5000'
    // const BASE_URL = 'https://dinder-flask.herokuapp.com'
    const BASE_URL = '/api'
    // 'dinde-Publi-EXUI6JTIP4L3-1856349916.us-west-2.elb.amazonaws.com/api'

    return (
      <div className='App'>
        <header className='App-header'>
          <img src={logo} className='App-logo' alt="logo"/>
          <h1 className='App-title'>dinder</h1>
          <p className='App-subtitle'>The Ingredient Matchmaker</p>
        </header>
        <main className='App-body'>
          <DataViz url={BASE_URL}/>
        </main>
        <footer>
        </footer>
      </div>
    );
  }
}

export default App;
