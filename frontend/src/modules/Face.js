import React, { Component } from 'react';
import Webcam from 'react-webcam';

class Face extends Component {
  constructor(props) {
    super(props);
    this.state = {image: null};
  }

  setRef = (webcam) => {
    this.webcam = webcam;
  }

  capture = () => {
    this.setState({image: this.webcam.getScreenshot()});
  }
  
  render() {
    return ( 
      <div className="Webcam">
        <div>
        <Webcam
          className="Webcam_live"
          audio={false}
          ref={this.setRef}
          screenshotFormat="image/jpeg"
          />
          </div>
         <div><button onClick={this.capture}>take picture</button></div>
          <div className="Webcam_still">
          <img src={this.state.image} alt=""/>
        </div>
      </div>  
    );
  }

}export default Face; 
 