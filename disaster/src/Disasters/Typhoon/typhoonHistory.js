import React, { Component } from 'react';
import '../disasterInfo.css'

class TyphoonHistory extends Component {
    state = {
        load1: '...',
        load2: '...',
        load3: '...',
        load4: '...',
        load5: '...',
        load6: '...',
        load7: '...',
        load8: '...',
        load9: '...',
        load10: '...',
        load11: '...',
        load12: '...',
        load13: '...',
        load14: '...',
        load15: '...',
        load16: '...',
        load17: '...',
        load18: '...',
        load19: '...',
        load20: '...',
        load21: '...',
        load22: '...',
        load23: '...',
        load24: '...',
        load25: '...',
        load26: '...',
        load27: '...',
        load28: '...',
        load29: '...',
        load30: '...',
        load31: '...',
        load32: '...',
    }

    componentWillMount = () => {
        this.callAPI()
    }

    callAPI = async() => {
        var res = await this.call()
        console.log(res)
        this.setState({load1:res.load1})
        this.setState({load2:res.load2})
        this.setState({load3:res.load3})
        this.setState({load4:res.load4})
        this.setState({load5:res.load5})
        this.setState({load6:res.load6})
        this.setState({load7:res.load7})
        this.setState({load8:res.load8})
        this.setState({load9:res.load9})
        this.setState({load10:res.load10})
        this.setState({load11:res.load11})
        this.setState({load12:res.load12})
        this.setState({load13:res.load13})
        this.setState({load14:res.load14})
        this.setState({load15:res.load15})
        this.setState({load16:res.load16})
        this.setState({load17:res.load17})
        this.setState({load18:res.load18})
        this.setState({load19:res.load19})
        this.setState({load20:res.load20})
        this.setState({load21:res.load21})
        this.setState({load22:res.load22})
        this.setState({load23:res.load23})
        this.setState({load24:res.load24})
        this.setState({load25:res.load25})
        this.setState({load26:res.load26})
        this.setState({load27:res.load27})
        this.setState({load28:res.load28})
        this.setState({load29:res.load29})
        this.setState({load30:res.load30})
        this.setState({load31:res.load31})
        this.setState({load32:res.load32})
    }

    call = async() => {
        return fetch('http://127.0.0.1:5000/CSV', {
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
                    <div className="infowhitelongbox oneline">
                        <div className="explain">
                            <p className="infomainfont">태풍 발생 이력
                                <br></br>
                            </p>
                            <form>
                                <p>
                                    <input type="date"></input>
                                    . 
                                    <input type="date"></input>
                                    .
                                    <input type="submit" value="Submit"></input>
                                </p>
                            </form>
                            <p className='infosubfont'>{this.state.load1}</p>
                            <p className='infosubfont'>{this.state.load2}</p>
                            <p className='infosubfont'>{this.state.load3}</p>
                            <p className='infosubfont'>{this.state.load4}</p>
                            <p className='infosubfont'>{this.state.load5}</p>
                            <p className='infosubfont'>{this.state.load6}</p>
                            <p className='infosubfont'>{this.state.load7}</p>
                            <p className='infosubfont'>{this.state.load8}</p>
                            <p className='infosubfont'>{this.state.load9}</p>
                            <p className='infosubfont'>{this.state.load10}</p>
                            <p className='infosubfont'>{this.state.load11}</p>
                            <p className='infosubfont'>{this.state.load12}</p>
                            <p className='infosubfont'>{this.state.load13}</p>
                            <p className='infosubfont'>{this.state.load14}</p>
                            <p className='infosubfont'>{this.state.load15}</p>
                            <p className='infosubfont'>{this.state.load16}</p>
                            <p className='infosubfont'>{this.state.load17}</p>
                            <p className='infosubfont'>{this.state.load18}</p>
                            <p className='infosubfont'>{this.state.load19}</p>
                            <p className='infosubfont'>{this.state.load20}</p>
                            <p className='infosubfont'>{this.state.load21}</p>
                            <p className='infosubfont'>{this.state.load22}</p>
                            <p className='infosubfont'>{this.state.load23}</p>
                            <p className='infosubfont'>{this.state.load24}</p>
                            <p className='infosubfont'>{this.state.load25}</p>
                            <p className='infosubfont'>{this.state.load26}</p>
                            <p className='infosubfont'>{this.state.load27}</p>
                            <p className='infosubfont'>{this.state.load28}</p>
                            <p className='infosubfont'>{this.state.load29}</p>
                            <p className='infosubfont'>{this.state.load30}</p>
                            <p className='infosubfont'>{this.state.load31}</p>
                            <p className='infosubfont'>{this.state.load32}</p>
                        </div>
                    </div>
                </div>
            </div> 
        );
    }
}

export default TyphoonHistory;