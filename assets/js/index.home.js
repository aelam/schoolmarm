import React, { Component } from 'react';
import ReactDOM from 'react-dom';
// import { DatePicker, message, Button } from 'antd';
import 'antd/dist/antd.css';  // or 'antd/dist/antd.less'
import { DatePicker } from 'antd';

// class App extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       date: '',
//     };
//   }
//   handleChange(date) {
//     message.info('Selected Date: ' + date.toString());
//     this.setState({ date });
//   }
//   render() {
//     return (
//       <div style={{ width: 400, margin: '100px auto' }}>
//         <DatePicker onChange={value => this.handleChange(value)} />
//         <div style={{ marginTop: 20 }}>Date: {this.state.date.toString()}</div>
//       </div>
//     );
//   }
// }

// ReactDOM.render(<App />, document.getElementById('react-app'));


class App extends React.Component {
  render() {
      return (
          <div>
              <h1>Hello Django + React = Awesomeness HAHA </h1>
              <DatePicker></DatePicker>
              {/*<Button >xxx</Button>*/}

          </div>);
  }
}

ReactDOM.render(<App />, document.getElementById('react-app'));
