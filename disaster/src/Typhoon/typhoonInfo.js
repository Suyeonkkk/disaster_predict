import React from 'react';
import './typhoonInfo.css';

const DisasterInfo = () => {
    return (
        <div className="bodyline">   
            <div className="maindisplay">
                <div className="transbox"></div>
                <div className="infowhitebox oneline">
                    <div className="explain">
                        <p className="infomainfont">태풍이 발생할 확률</p>
                        <p className="infosubfont">p</p>
                    </div>
                </div>
            </div>
        </div> 
    );
}

export default DisasterInfo;