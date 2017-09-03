import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { DatePicker } from 'antd';
// import DateRangePicker from "reacteasyui/src/js/plugin/Date/DateRangePicker";


class App extends React.Component {
render() {
    return (
    <div>
        <h1>Hello Django + React = Awesomeness HAHA </h1>

        <DatePicker/>
    </div>);
}
}


ReactDOM.render(<App />, document.getElementById('react-app'));
