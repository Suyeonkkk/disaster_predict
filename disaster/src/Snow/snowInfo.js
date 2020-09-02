import React, { Component } from 'react';
import './snowInfo.css';

class SnowInfo extends Component {
    state = {
        snow: '...',
    }

    componentWillMount = () => {
        this.callAPI()
    }

    callAPI = async() => {
        var res = await this.call()
        console.log(res)
        this.setState({snow:res.snow})
    }

    call = async() => {
        return fetch('http://127.0.0.1:5000/Snow', {
            method: 'get',
            headers: {
                'Accept': 'application/json', // eslint-disable-line quote-props
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "access-control-allow-origin": "localhost",
                "access-control-allow-credentials": "true"
            }
        })
        .then(response => response.json())
        .catch(err => console.log(err))
    }

    render() {
        return (
            <div className="bodyline">   
                <div className="maindisplay">
                    <div className="transbox"></div>
                    <div className="infowhitebox oneline">
                        <div className="explain">
                            <p className="infomainfont">눈이 내릴 확률</p>
                            <p className="infosubfont">{this.state.snow}% 입니다.</p>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default SnowInfo;