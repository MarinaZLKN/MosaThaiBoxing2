import React from 'react';
import '../styles/Header.scss'
import logo from '@images/logo.png';


interface LogoProps {
  alt: string;
  className?: string;
}

const Logo: React.FC<LogoProps> = ({ alt , className = 'logo-main' }) => {
  return (
    <div className="logo">
      <img className={` ${className}`} src={logo} alt={alt} />
    </div>
  );
};

export default Logo;