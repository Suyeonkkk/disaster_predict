import React, { Component } from 'react';
import '../disasterInfo.css'

class RainLocation extends Component {
// 서울 108 인천 112 대구 143 대전 133 부산 159 울산 152 광주 156 제주도 184
    state = {
        loc0: '...',
        loc1: '...',
        loc2: '...',
        loc3: '...',
        loc4: '...',
        loc5: '...',
        loc6: '...',
        loc7: '...',
    }

    componentWillMount = () => {
        this.callAPI()
    }

    callAPI = async() => {
        var res = await this.call()
        console.log(res)
        this.setState({loc0:res.loc0})
        this.setState({loc1:res.loc1})
        this.setState({loc2:res.loc2})
        this.setState({loc3:res.loc3})
        this.setState({loc4:res.loc4})
        this.setState({loc5:res.loc5})
        this.setState({loc6:res.loc6})
        this.setState({loc7:res.loc7})
    }

    call = async() => {
        return fetch('http://127.0.0.1:5000/RainLocation', {
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
                            <p className="infomainfont">다른 지역에서 비가 내릴 확률입니다.
                            <br></br>
                            <br></br>
                            <br></br></p>
                            <table className='infosubfont infoTable'>
                                <tr>
                                    <td>서울</td>
                                    <td>인천</td>
                                    <td>대구</td>
                                    <td>대전</td>
                                    <td>부산</td>
                                    <td>울산</td>
                                    <td>광주</td>
                                    <td>제주</td>
                                </tr>
                                <tr>
                                    <td>{this.state.loc0}%</td>
                                    <td>{this.state.loc1}%</td>
                                    <td>{this.state.loc2}%</td>
                                    <td>{this.state.loc3}%</td>
                                    <td>{this.state.loc4}%</td>
                                    <td>{this.state.loc5}%</td>
                                    <td>{this.state.loc6}%</td>
                                    <td>{this.state.loc7}%</td>
                                </tr>
                            </table>
                        </div>
                    </div>
                </div>
            </div> 
        );
    }
}

export default RainLocation;