import React, { Component } from 'react';
import '../disasterInfo.css'

class TyphoonHistory extends Component {

    state = {
        load0: '...',
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

    callAPI = async () => {
        var res = await this.call()
        console.log(res)
        this.setState({ load0: res.load0 })
        this.setState({ load1: res.load1 })
        this.setState({ load2: res.load2 })
        this.setState({ load3: res.load3 })
        this.setState({ load4: res.load4 })
        this.setState({ load5: res.load5 })
        this.setState({ load6: res.load6 })
        this.setState({ load7: res.load7 })
        this.setState({ load8: res.load8 })
        this.setState({ load9: res.load9 })
        this.setState({ load10: res.load10 })
        this.setState({ load11: res.load11 })
        this.setState({ load12: res.load12 })
        this.setState({ load13: res.load13 })
        this.setState({ load14: res.load14 })
        this.setState({ load15: res.load15 })
        this.setState({ load16: res.load16 })
        this.setState({ load17: res.load17 })
        this.setState({ load18: res.load18 })
        this.setState({ load19: res.load19 })
        this.setState({ load20: res.load20 })
        this.setState({ load21: res.load21 })
        this.setState({ load22: res.load22 })
        this.setState({ load23: res.load23 })
        this.setState({ load24: res.load24 })
        this.setState({ load25: res.load25 })
        this.setState({ load26: res.load26 })
        this.setState({ load27: res.load27 })
        this.setState({ load28: res.load28 })
        this.setState({ load29: res.load29 })
        this.setState({ load30: res.load30 })
        this.setState({ load31: res.load31 })
        this.setState({ load32: res.load32 })

        var temp = this.state.load0 + this.state.load1 + this.state.load2 + this.state.load3 + this.state.load4 + this.state.load5 + this.state.load6 + this.state.load7
            + this.state.load8 + this.state.load9 + this.state.load10 + this.state.load11 + this.state.load12 + this.state.load13 + this.state.load14 + this.state.load15
            + this.state.load16 + this.state.load17 + this.state.load18 + this.state.load19 + this.state.load20 + this.state.load21 + this.state.load22 + this.state.load23
            + this.state.load24 + this.state.load25 + this.state.load26 + this.state.load27 + this.state.load28 + this.state.load29 + this.state.load30 + this.state.load31
            + this.state.load32;

        var arr = temp.split("\t");

        var i, j;
        var index = 0;
        for (i = 1; i < 33; i++) {
            for (j = 1; j < 5; j++) {
                temp = String(i) + String(j);
                document.getElementById(temp).innerText = arr[index];
                index++;
            }
        }
    }

    call = async () => {
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
                                    <input type="date" id="startDate"></input>
                                    .
                                    <input type="date" id="endDate"></input>
                                    .
                                    <input type="submit" value="조회" onClick={this.search}></input>
                                </p>
                            </form>
                            <table className="typhoonTable">
                                <thead>
                                    <tr>
                                        <th className="infomainfont">한글태풍명</th>
                                        <th className="infomainfont">영문태풍명</th>
                                        <th className="infomainfont">발생일시</th>
                                        <th className="infomainfont">소멸일시</th>
                                    </tr>
                                </thead>
                                <tbody className="infosubfont" id="table">
                                    <tr>
                                        <td id="11"></td>
                                        <td id="12"></td>
                                        <td id="13"></td>
                                        <td id="14"></td>
                                    </tr>
                                    <tr>
                                        <td id="21"></td>
                                        <td id="22"></td>
                                        <td id="23"></td>
                                        <td id="24"></td>
                                    </tr>
                                    <tr>
                                        <td id="31"></td>
                                        <td id="32"></td>
                                        <td id="33"></td>
                                        <td id="34"></td>
                                    </tr>
                                    <tr>
                                        <td id="41"></td>
                                        <td id="42"></td>
                                        <td id="43"></td>
                                        <td id="44"></td>
                                    </tr>
                                    <tr>
                                        <td id="51"></td>
                                        <td id="52"></td>
                                        <td id="53"></td>
                                        <td id="54"></td>
                                    </tr>
                                    <tr>
                                        <td id="61"></td>
                                        <td id="62"></td>
                                        <td id="63"></td>
                                        <td id="64"></td>
                                    </tr>
                                    <tr>
                                        <td id="71"></td>
                                        <td id="72"></td>
                                        <td id="73"></td>
                                        <td id="74"></td>
                                    </tr>
                                    <tr>
                                        <td id="81"></td>
                                        <td id="82"></td>
                                        <td id="83"></td>
                                        <td id="84"></td>
                                    </tr>
                                    <tr>
                                        <td id="91"></td>
                                        <td id="92"></td>
                                        <td id="93"></td>
                                        <td id="94"></td>
                                    </tr>
                                    <tr>
                                        <td id="101"></td>
                                        <td id="102"></td>
                                        <td id="103"></td>
                                        <td id="104"></td>
                                    </tr>
                                    <tr>
                                        <td id="111"></td>
                                        <td id="112"></td>
                                        <td id="113"></td>
                                        <td id="114"></td>
                                    </tr>
                                    <tr>
                                        <td id="121"></td>
                                        <td id="122"></td>
                                        <td id="123"></td>
                                        <td id="124"></td>
                                    </tr>
                                    <tr>
                                        <td id="131"></td>
                                        <td id="132"></td>
                                        <td id="133"></td>
                                        <td id="134"></td>
                                    </tr>
                                    <tr>
                                        <td id="141"></td>
                                        <td id="142"></td>
                                        <td id="143"></td>
                                        <td id="144"></td>
                                    </tr>
                                    <tr>
                                        <td id="151"></td>
                                        <td id="152"></td>
                                        <td id="153"></td>
                                        <td id="154"></td>
                                    </tr>
                                    <tr>
                                        <td id="161"></td>
                                        <td id="162"></td>
                                        <td id="163"></td>
                                        <td id="164"></td>
                                    </tr>
                                    <tr>
                                        <td id="171"></td>
                                        <td id="172"></td>
                                        <td id="173"></td>
                                        <td id="174"></td>
                                    </tr>
                                    <tr>
                                        <td id="181"></td>
                                        <td id="182"></td>
                                        <td id="183"></td>
                                        <td id="184"></td>
                                    </tr>
                                    <tr>
                                        <td id="191"></td>
                                        <td id="192"></td>
                                        <td id="193"></td>
                                        <td id="194"></td>
                                    </tr>
                                    <tr>
                                        <td id="201"></td>
                                        <td id="202"></td>
                                        <td id="203"></td>
                                        <td id="204"></td>
                                    </tr>
                                    <tr>
                                        <td id="211"></td>
                                        <td id="212"></td>
                                        <td id="213"></td>
                                        <td id="214"></td>
                                    </tr>
                                    <tr>
                                        <td id="221"></td>
                                        <td id="222"></td>
                                        <td id="223"></td>
                                        <td id="224"></td>
                                    </tr>
                                    <tr>
                                        <td id="231"></td>
                                        <td id="232"></td>
                                        <td id="233"></td>
                                        <td id="234"></td>
                                    </tr>
                                    <tr>
                                        <td id="241"></td>
                                        <td id="242"></td>
                                        <td id="243"></td>
                                        <td id="244"></td>
                                    </tr>
                                    <tr>
                                        <td id="251"></td>
                                        <td id="252"></td>
                                        <td id="253"></td>
                                        <td id="254"></td>
                                    </tr>
                                    <tr>
                                        <td id="261"></td>
                                        <td id="262"></td>
                                        <td id="263"></td>
                                        <td id="264"></td>
                                    </tr>
                                    <tr>
                                        <td id="271"></td>
                                        <td id="272"></td>
                                        <td id="273"></td>
                                        <td id="274"></td>
                                    </tr>
                                    <tr>
                                        <td id="281"></td>
                                        <td id="282"></td>
                                        <td id="283"></td>
                                        <td id="284"></td>
                                    </tr>
                                    <tr>
                                        <td id="291"></td>
                                        <td id="292"></td>
                                        <td id="293"></td>
                                        <td id="294"></td>
                                    </tr>
                                    <tr>
                                        <td id="301"></td>
                                        <td id="302"></td>
                                        <td id="303"></td>
                                        <td id="304"></td>
                                    </tr>
                                    <tr>
                                        <td id="311"></td>
                                        <td id="312"></td>
                                        <td id="313"></td>
                                        <td id="314"></td>
                                    </tr>
                                    <tr>
                                        <td id="321"></td>
                                        <td id="322"></td>
                                        <td id="323"></td>
                                        <td id="324"></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    search(e) {
        e.returnValue = true;
        e.preventDefault();
        var start = document.getElementById("startDate").value.replaceAll('-', '').trim();
        var end = document.getElementById("endDate").value.replaceAll('-', '').trim();

        if (end === "") {
            end = 99999999;
        }
        if (start === "") {
            start = 11111111;
        }
        if (start > end) {
            alert("조회하려는 시작날짜가 더 느립니다 !");
            window.location.reload();
        }
        start *= 1;
        end *= 1;
        var td = document.getElementsByTagName("td");
        for (var i = 0; i < 32; i++) {
            var temp = td[4 * i + 2].innerText.split(' ')[0].replaceAll('.', '').trim();
            temp *= 1;
            if (start <= temp && temp <= end) {
                td[4 * i].style.display = '';
                td[4 * i + 1].style.display = '';
                td[4 * i + 2].style.display = '';
                td[4 * i + 3].style.display = '';
            } else {
                td[4 * i].style.display = 'none';
                td[4 * i + 1].style.display = 'none';
                td[4 * i + 2].style.display = 'none';
                td[4 * i + 3].style.display = 'none';
            }
        }
    }
}

export default TyphoonHistory;