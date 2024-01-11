import React from 'react';
import '../styles/App.css';

interface TitleProps {
  text: string;
  className?: string;
}

const Title: React.FC<TitleProps> = ({ text, className = '' }) => {
  return (
    <div className={`title ${className}`}>
      {text}
    </div>
  );
};

export default Title;