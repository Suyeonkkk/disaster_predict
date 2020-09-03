import React from 'react';
import './home.css';

const Home = () => {
    return (
        <div className="bodyline block">   
            <div className="maindisplay">                
                <h1 className="mainfont">Disaster Predict Service</h1>
                <h4 className="subfont">
                <br />인공지능 기술을 이용하여 재난을 예측해드립니다.
                <br />어떤 재난을 예측해드릴까요 ?
                <br /><p/></h4>
            </div>
        </div>
    );
}

export default Home;