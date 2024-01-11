import React, { useState } from 'react';
import '../../../styles/Group.scss';

interface GroupProps {
    groupName: string;
    groupImage: string;
    groupText: string;
    groupAlt: string;
}
//TODO check the chrome and add the animation
const Group: React.FC<GroupProps> = ({groupName, groupImage, groupText, groupAlt}) => {
    const [showText, setShowText] = useState(false);

    const toggleText = () => {
        setShowText(!showText);
    };

    return (
        <div className="group-card">
            <img className="group-img" src={groupImage} alt={groupAlt} />
            <label className="group-name" onClick={toggleText}>{groupName}</label>
            {showText && <p className="group-text">{groupText}</p>}
        </div>
    );
};

export default Group;
