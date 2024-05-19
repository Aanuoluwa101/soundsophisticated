import React from 'react';
import styles from '../styles/assistantHome.module.css';
import icons from './icons'
import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';





const AssistantHome = () => {
    const navigate = useNavigate();
    const handleClick = (event) => {
        const context = event.target.textContent;
        navigate('/assistant', { state: { context } });
      };
    return (
        <div className={styles.container}>
            <p className={styles['context-ideas-header']}>some context ideas to get you started...</p>
            <div className={styles['context-ideas']}>
                <p onClick={(event) => handleClick(event)} className={styles['example-context']}>praise a good performance</p>
                <p onClick={(event) => handleClick(event)} className={styles['example-context' ]}>giving a presentation to the board of directors</p>
                <p onClick={(event) => handleClick(event)} className={styles['example-context']}>technician</p>
            </div>
            <div className={styles['context-prompt-container']}>
                <img src={icons.logo_gray} alt="Logo" />
                <p className={styles.prompt}>Enter a context and I'll suggest a word that fits!</p>
            </div>
        </div>
    );
}

export default AssistantHome;
