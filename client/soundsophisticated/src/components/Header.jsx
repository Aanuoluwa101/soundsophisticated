import React, { useState, useEffect } from 'react'
import icons from './icons'
import styles from '../styles/header.module.css'
import { useNavigate } from 'react-router-dom';
import { dictionary, assistant } from './modes';



function Header(props) {
    const passedSearchInput = props.passedSearchInput || ''
    const { mode, getMeaning, getSuggestion } = props
    const [searchInput, setSearchInput] = useState(passedSearchInput)  //search input here is the word (both in the dictionary and assistant modes)
    const [context, setContext] = useState('')
    const navigate = useNavigate()
    

    useEffect(() => {
        setSearchInput(passedSearchInput);
    }, [passedSearchInput]);
    
    const handleKeyPress = event => {
        if (event.key === "Enter") {
            handleSearchOrSuggest();
        }
    }


    const handleSearchOrSuggest = () => {
        // console.log(searchInput)
        // console.log(context)

        //console.log(`word is ${searchInput}`)
        //console.log(`context is ${context}`)
        if (mode.type == "assistant")
            getSuggestion(searchInput, context);
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
            
            <div className={styles['search-bar-container']}>
        <div className={styles['search-bar']}>
          <input
            type="text"
            className={styles['search-input']}
            placeholder={dictionary.inputPlaceholder}
            value={searchInput}
            onChange={(e) => setSearchInput(e.target.value)}
            onKeyDown={handleKeyPress}
          />
          <img
            src={mode.inputIcon}
            alt="Search"
            className={styles['search-icon']}
            onClick={() => handleSearchOrSuggest()}
          />
        </div>
        {mode.type === 'assistant' && (
          <div className={styles['search-bar']}>
            <input
              type="text"
              className={styles['search-input']}
              placeholder={assistant.inputPlaceholder}
              value={context}
              onChange={(e) => setContext(e.target.value)}
              onKeyDown={handleKeyPress}
            />
            <img
              src={mode.inputIcon}
              alt="Search"
              className={styles['search-icon']}
              onClick={() => handleSearchOrSuggest()}
            />
          </div>
        )}
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