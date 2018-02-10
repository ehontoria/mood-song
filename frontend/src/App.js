import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Webcam from 'react-webcam';

function Face(props) {
  return <div> 
    <Webcam
        audio={false}
        height={350}
        ref={props.ref}
        screenshotFormat="image/jpeg"
        width={350}
    />
    <button onClick={props.capture}> face </button>
  </div>;
}

function Song() {
    return <div> song </div>;
}

class App extends Component {
  setRef = (webcam) => {
    this.webcam = webcam;
  }
  
  capture = () => {
    const imageSrc = this.webcam.getScreenshot();
  }
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
        <Face ref={this.setRef} capture={this.capture}>
        </Face>
        <Song></Song>
      </div>
    );
  }
}

export default App;
