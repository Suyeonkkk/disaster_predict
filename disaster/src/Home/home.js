import React from 'react';
import './home.css';
import { Link } from "react-router-dom"

var selected;
var root = "/";

const Home = () => {
    return (
        <div className="bodyline block">   
            <div className="maindisplay">                
                <h1 className="mainfont">Disaster Predict Service</h1>
                <h4 className="subfont">
                <br />인공지능 기술을 이용하여 재난을 예측해드립니다.
                <br />어떤 재난을 예측해드릴까요 ?
                <br /><p/></h4>
                {/* <select id = "dis_select" className="subfont subSearch" onClick = {e => setLink(e.target.value)} onChange = {e => setLink(e.target.value)}>
                    <option value = "default">재난을 선택하세요.</option>
                    <option value = "1" label = "태풍"/>
                    <option value = "2" label = "폭우"/>
                    <option value = "3" label = "폭설"/>
                </select>
                <button id = "go" className="subfont subButton" onClick = {e => disaster_select(selected)}>
                    <Link id = "link" to = {root} className="none">
                        go!
                    </Link>
                </button> */}
            </div>
        </div>
    );
}

// function setLink(value) {
//     selected = value;
//     if (value === 1) {
//         root = "/TyphoonInfo";
//     } else if (value === 2) {
//         root = "/SearchDate";
//     } else if (value === 3) {
//         root = "/SearchRegion";
//     }
//     var go = document.getElementById("link");
//     go.setAttribute('to', {root});
// }

// function disaster_select(value) {
//     var go = document.getElementById("link");
//     go.setAttribute('to', {root});
//     selected = value;
//     if (value === '1') {
//         root = "/TyphoonInfo";
//         alert('태풍 화면으로 이동합니다.');
//     } else if (value === '2') {
//         root = "/SearchDate";
//         alert('폭우 화면으로 이동합니다.');
//     } else if (value === '3') {
//         root = "/SearchRegion";
//         alert('폭설 화면으로 이동합니다.'); 
//     } else {
//         alert('error');
//     }
//     go = document.getElementById("link");
//     go.setAttribute('to', {root});
// }

export default Home;