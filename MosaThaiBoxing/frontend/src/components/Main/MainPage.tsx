import React from 'react';
import MainPic from "./MainPic";
import Logo from '../Logo';
import '../../styles/MainPage.css';
import Title from "../Title";
import FeedbackForm from "./FeedbackForm";
import Contacts from "./Contacts";
import GroupList from "./Groups/GroupList";
import adv from '@images/advanced.png';
import beg from '@images/beginners.png';
import child from '@images/children.png';

interface Groups {
    groupName: string;
    groupImage: string;
    groupText: string;
    groupAlt: string;
}
const MainPage: React.FC = () => {
    const handleSubmit = (formData: FormData) => {
        console.log('Данные из формы:', formData);

    };

    const groupsData: Groups[] = [
    {
      groupName: 'Advanced',
      groupImage: adv,
      groupText: 'This session is for experienced fighters, focusing on advanced techniques and strategies. It includes complex combinations, counter-attacks, clinch work, advanced footwork, head movement, and defensive strategies. Intensive sparring is a key component. Conditioning aims to enhance endurance, strength, and agility.',
      groupAlt: 'group picture',
    },
    {
      groupName: 'Beginners',
      groupImage: beg,
      groupText: 'Tailored for newcomers, this training covers the fundamentals of Muay Thai, including basic stances, punches, kicks, elbows, knee strikes, and defensive maneuvers. The focus is on coordination, balance, and fitness, with strength and flexibility exercises. Light sparring is introduced gradually.',
      groupAlt: 'group picture',
    },
    {
      groupName: 'Children',
      groupImage: child,
      groupText: 'Designed for young learners, this program emphasizes fun, discipline, and basic Muay Thai techniques. It includes age-appropriate drills focusing on basic strikes and defenses, fostering physical fitness, coordination, and confidence. Safety is prioritized with non-contact or light-contact exercises.',
      groupAlt: 'group picture',
    },
  ];

    return (
        <div className="container main-page_container">
            <div className="main-page_pic">
                <MainPic alt="Main page picture"/>
            </div>
            <div className="main-page_aboutUs">
                <div className="aboutUs-info">
                    <div className="aboutUs-title">
                        <Title text="About us"/>
                    </div>
                    <div className="subtitle">
                        Sports club MMAces was founded in Pärnu in 2010, when it was the third sports club in Estonia
                        that trains freestyle combat, or MMA. Sports club MMAces is a member of the Estonian Sports
                        Freestyle Wrestling Association (ESVL) and cooperates with other Estonian sports clubs that
                        train freestyle sports. <br/> <br/>Today, we have grown into a family sports club that offers training for
                        children, youth and adults, both men and women.
                    </div>
                </div>
                <div className="aboutUs-logo">
                    <Logo alt="About Us Logo" className="aboutUs-logo"/>
                </div>
            </div>
            <div className="main-page-groups">
                <div className="main-page-groups-title">
                    <Title text="Groups"/>
                    <GroupList groups={groupsData} />

                </div>
            </div>
            <div className="main-page_mt-block">
                <div className="main-page_mt-block">
                    <Title text="Why muay thai?"/>
                    <div className="main-page_mt-block_text">
                        <div className="subtitle">Muay Thai, known as Thai boxing, provides a multitude of <label className="highlight">physical</label> benefits.
                            It's a holistic full-body workout that significantly improves
                            cardiovascular health, enhancing endurance and heart fitness. The practice increases
                            strength, particularly in the legs, back, and shoulders, and improves flexibility and
                            coordination. This high-intensity training also aids in effective weight management and
                            muscle toning. Additionally, Muay Thai equips practitioners with practical self-defense
                            skills.</div>
                        <div className="subtitle">
                            <br/>
                            On the <label className="highlight">mental</label> side, Muay Thai serves as a potent stress buster, promoting resilience and
                            mental toughness. The discipline and focus required in training sharpen these cognitive
                            skills, beneficial in various life situations. Practitioners often notice an uplift in
                            self-confidence as they progress, bolstered by physical improvement and self-defense
                            proficiency. The practice encourages mindfulness and present moment awareness, contributing
                            to overall mental well-being. Engaging in Muay Thai also allows individuals to connect with
                            its rich cultural heritage, adding a deeper layer of appreciation. The social aspect of
                            joining a Muay Thai community fosters camaraderie and support, enhancing the overall
                            experience.
                        </div>
                    </div>
                </div>
            </div>
            <div className="main-page_info">
                <div className="main-page_form">
                    <Title text="Write to us"/>
                    <FeedbackForm />
                </div>
            </div>
            <div className="main-page_contacts">
                <Contacts/>
            </div>
            <div className="main-page_sponsors"></div>


        </div>
    );
};

export default MainPage;