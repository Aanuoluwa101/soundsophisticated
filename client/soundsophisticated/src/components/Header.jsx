import React, { useState } from 'react'
import icons from './icons'
import styles from '../styles/header.module.css'
import { useNavigate } from 'react-router-dom';



function Header(props) {
    const passedSearchInput = props.passedSearchInput || ''
    const { mode, getMeaning, getSuggestion } = props
    const [searchInput, setSearchInput] = useState(passedSearchInput)
    const navigate = useNavigate()

    
    const handleKeyPress = event => {
        if (event.key === "Enter") {
            handleSearchOrSuggest();
        }
    }


    const handleSearchOrSuggest = () => {
        //console.log(searchInput)
        if (mode.type == "assistant")
            getSuggestion(searchInput);
        else if (mode.type == "dictionary")
            getMeaning(searchInput);
    }

    const toAssistant = () => {
        if (mode.type == "dictionary")
            navigate('/assistant')
    }

    const toDictionary = () => {
        if (mode.type == "assistant")
            navigate('/dictionary')
    }

    
    // console.log(mode.assistantBg);
    return (
        <header>
            <div className={styles.logo}>
                <img src={icons.logo}/>
            </div>
            <div className={styles.modes}>
                <div style={{backgroundColor: `${mode.dictionaryBg}`}} 
                     className={styles.mode}
                     onClick={toDictionary}>
                    <img src={icons.dictionary}/>
                </div>
                <div style={{backgroundColor: `${mode.assistantBg}`}} 
                     className={styles.mode}
                     onClick={toAssistant}>
                    <img src={icons.bot}/>
                </div>
            </div>
            
            <div className={styles["search-bar"]}> 
                <input type="text" 
                       className={styles["search-input"]}
                       placeholder={mode.inputPlaceholder} 
                       value={searchInput}
                       onChange={e => setSearchInput(e.target.value)}
                       onKeyDown={handleKeyPress}/>
                <img src={mode.inputIcon} alt="Search" 
                     className={styles["search-icon"]} onClick={() => handleSearchOrSuggest(searchInput)}/>
            </div>
            <div className={styles.dev}>
                <a href="https://github.com/Aanuoluwa101/soundsophisticated">
                    <img src={icons.dev} alt="GitHub page" />
                </a>
            </div>
        </header>
    );
}

export default Header;