import React from 'react';
import './disasterInfo.css';

const DisasterInfo = () => {
    return (
        <div className="bodyline">   
            <div className="maindisplay">
                <div className="transbox"></div>
                <div className="infowhitebox oneline">
                    <div className="explain">
                        <p className="infomainfont">디비 정보</p>
                        <p className="infosubfont">뽑기</p>
                        <p className="infomainfont">디비</p>
                        <p className="infosubfont">뽑기</p>
                        <p className="infomainfont">디비</p>
                        <p className="infosubfont">뽑기</p>
                        <p className="infomainfont">디비</p>
                        <p className="infosubfont">뽑기</p>
                    </div>
                </div>
            </div>
        </div> 
    );
}

export default DisasterInfo;