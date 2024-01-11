import React from 'react';
import '../../styles/MainPage.css';
import Title from "../Title";


const Contacts: React.FC = () => {

  return (
    <div className="container contacts-container">
      <Title text="contacts" className="contacts"/>

    </div>
  );
};

export default Contacts;