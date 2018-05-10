import React, { Component } from 'react';
import './App.css';
import axios from 'axios';
import moment from 'moment';

class App extends Component {
  deviceState = {
    isActive: false,
    active: 'Active',
    inactive: 'Inactive'
  };
  state = {
    status: 'Loading...',
    futureTime: '',
    minutes: ''
  };
  path = 'getSleep/';
  url = 'http://127.0.0.1:8000';

  componentDidMount() {
    axios.get(`${this.url}/${this.path}`).then(res => {
      this.setState({ futureTime: res.data.shouldSleep });

      if (res.data.shouldSleep !== false) {
        const futureTime = this.state.futureTime;
        const now = moment().subtract({ hours: 2 });
        const future = moment(futureTime.slice(0, 19)).utc();
        const duration = future - now;
        const minutesToGo = Math.floor(duration / 60000);
        this.setState({
          isActive: true,
          status: this.deviceState.inactive,
          minutes: minutesToGo
        });
      } else {
        this.setState({ status: this.deviceState.active });
      }
    });
  }

  render() {
    let minutes = '';
    if (this.state.isActive) {
      minutes = <div>{this.state.minutes} minutes till activation.</div>;
    }
    return (
      <div className="App">
        <div>Device state: {this.state.status}</div>
        {minutes}
      </div>
    );
  }
}

export default App;
