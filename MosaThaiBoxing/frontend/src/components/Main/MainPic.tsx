import React from 'react';
import '../../styles/MainPic.scss';
import mainpic from '@images/main.png';


interface MainPicProps {
    alt: string;
}

const MainPic: React.FC<MainPicProps> = ({alt}) => (
    <div className="image-container">
        <img src={mainpic} alt={alt} className="main_picture"/>
        <div className="image-title_btn">
            <div className="main-page_pic-title"> Mosa <br/> Thai Boxing</div>
            <button id="main-page-pic-btn">Register for training</button>
        </div>
    </div>
);

export default MainPic;