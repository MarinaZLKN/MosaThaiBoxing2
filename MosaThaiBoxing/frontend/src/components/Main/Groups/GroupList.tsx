import React from 'react';
import Group from './Group';
import '../../../styles/Group.scss';

interface GroupData {
    groupName: string;
    groupImage: string;
    groupText: string;
    groupAlt: string;
}

interface GroupListProps {
    groups: GroupData[];
}

const GroupList: React.FC<GroupListProps> = ({groups}) => {
    return (
        <div className="container group-container">
            {groups.map((group, index) => (
                <Group
                    key={index}
                    groupName={group.groupName}
                    groupImage={group.groupImage}
                    groupText={group.groupText}
                    groupAlt={group.groupAlt}
                />
            ))}
        </div>
    );
};

export default GroupList;