import React, { Component } from 'react';
import { Link } from "react-router-dom"
import '../disasterInfo.css';

class RainInfo extends Component {
    state = {
        rain: '...',
    }

    componentWillMount = () => {
        this.callAPI()
    }

    callAPI = async() => {
        var res = await this.call()
        console.log(res)
        this.setState({rain:res.rain})
    }

    call = async() => {
        return fetch('http://127.0.0.1:5000/Rain', {
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
                            <p className="infomainfont">비가 내릴 확률</p>
                            <p className="infosubfont"><b>{this.state.rain}%</b> 입니다.</p>
                            <p className='infosubfont'>이 확률은 기온, 습도, 가조시간, 구름양, 강수량 등을 이용하여 예측하였습니다.
                            <br></br>
                            <br></br>
                            위의 지역은 기본 설정 값인 대전의 날씨를 예측한 정보입니다.
                            <br></br>
                            <br></br>
                            <br></br></p>
                            <Link to='/RainLocation'>
                                <button  className='goButton'>
                                    다른 지역에서 비가 내릴 확률 보기
                                </button>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default RainInfo;