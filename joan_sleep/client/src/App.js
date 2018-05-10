import React, { Component } from 'react';
import './App.css';
import axios from 'axios';
import moment from 'moment';

class App extends Component {
  state = {
    isActive: false,
    status: 'Loading...',
    futureTime: '',
    minutes: ''
  };
  deviceState = { active: 'Active', inactive: 'Inactive' };
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
          isActive: false,
          status: this.deviceState.inactive,
          minutes: minutesToGo
        });
      } else {
        this.setState({ status: this.deviceState.active, isActive: true });
      }
    });
  }

  render() {
    let minutes = '';
    let statusColor = '';
    if (this.state.isActive) {
      statusColor = 'green';
    } else {
      minutes = `${this.state.minutes} minutes till activation.`;
      statusColor = 'red';
    }
    return (
      <div className="App container">
        <div
          className={`center-align card-panel lighten-4 ${statusColor}`}
          style={{ width: '300px', margin: '0 auto', marginTop: '100px' }}
        >
          Device state: {this.state.status}
        </div>
        <p>{minutes}</p>
      </div>
    );
  }
}

export default App;
