import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
//import Face from './modules/Face.js';
//import Song from './modules/Song.js';
import {Face, Song} from './modules/modules.js';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">MoodSong</h1>
        </header>
        <p className="App-intro">
            Please make sure your webcam is on and enabled.
        </p>
        <Face classname="Face"> </Face>
        <Song classname="Song"> </Song>
      </div>
    );
  }
}

export default App;
