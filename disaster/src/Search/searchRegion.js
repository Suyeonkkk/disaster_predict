import React from 'react';
import './searchRegion.css';
import { Link } from "react-router-dom"

const SearchRegion = () => {
    return (
        <div className="bodyline">   
            <div className="maindisplay">
                <div className="oneline">
                    <Link to="/DisasterInfo" className="none">
                        <div className="dicwhitebox">
                            <p className="dicalign">검색한 내용</p>
                            <p className="dicalign">정보</p>
                        </div>
                    </Link>
                </div>
            </div>
        </div>
    );
}

export default SearchRegion;