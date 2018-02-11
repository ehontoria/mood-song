import React, { Component } from 'react';
import './App.css';
import Face from './modules/Face.js'
import Song from './modules/Song.js';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">MoodSong</h1>
        </header>

        <p className="App-intro">
            Please make sure your webcam is on and enabled.
        </p>

        <div className="App-controls">
        <Face className="Face"> </Face>
        </div>
      </div>
    );
  }
}

export default App;
