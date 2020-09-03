import React, { Component } from 'react';
import { Link } from "react-router-dom"
import '../disasterInfo.css';

class TyphoonInfo extends Component {
    state = {
        typhoon: '...',
    }

    componentWillMount = () => {
        this.callAPI()
    }

    callAPI = async() => {
        var res = await this.call()
        console.log(res)
        this.setState({typhoon:res.typhoon})
    }

    call = async() => {
        return fetch('http://127.0.0.1:5000/Typhoon', {
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
                            <p className="infomainfont">태풍이 발생할 확률</p>
                            <p className="infosubfont">{this.state.typhoon}% 입니다.</p>
                            <p className='infosubfont'>이 확률은 제주도 지역의 습도, 해면 기압, 풍속, 강수량 등을 이용하여 예측하였습니다.
                            <br></br>
                            <br></br></p>
                            <Link to='/TyphoonHistory'>
                                <button  className='goButton'>
                                    역대 태풍 이력 보러가기
                                </button>
                            </Link>
                        </div>
                    </div>
                </div>
            </div> 
        );
    }
}

export default TyphoonInfo;