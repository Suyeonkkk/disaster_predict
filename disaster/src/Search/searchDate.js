import React from 'react';
import './searchDate.css';
import Calendar from 'react-calendar';

const SearchDate = () => {
    return (
        <div className="bodyline">   
            <div className="maindisplay">
                <div className="calendar">
                    <Calendar />
                    <div className="schedule">
                        <p className="scsubfont">디비</p>
                        <p>내용</p>
                        <p>내용</p>
                        <p>내용</p>
                        <p className="scsubfont">디비</p>
                        <p>내용</p>
                        <p className="scsubfont">디비</p>
                        <p>내용</p>
                        <p>내용</p>
                        <p className="scsubfont">디비</p>
                        <p>내용</p>
                        <p>내용</p>
                    </div>
                </div>
            </div>
        </div>   
    );
}

export default SearchDate;