import React from 'react';
import Logo from './Logo';
import '../styles/Header.scss';

interface HeaderProps {

}

const Header: React.FC<HeaderProps> = () => {
    return (
        <div className="container header-container">
                <div className="header-logo">
                     <Logo alt="Logo" className="logo-main"/>

                </div>
                <div className="header-menu">
                    <div className="header-menu-main">Main</div>
                    <div className="header-menu-main">News</div>
                    <div className="header-menu-main">Training</div>
                    <div className="header-menu-main">Merch</div>
                </div>
                <div className="registration-button">
                    <button>Register</button>
                </div>
            </div>

    );
};

export default Header;