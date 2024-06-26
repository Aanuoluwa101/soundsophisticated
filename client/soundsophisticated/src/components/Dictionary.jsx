import React, { useState, useEffect } from 'react'
import Loader from './Loader'
import styles from '../styles/word.module.css'
import axios from 'axios'
import { dictionary } from './modes'
import SearchedWord from './SearchedWord'
import DictionaryHome from './DictionaryHome'
import Header from './Header'
import { useLocation } from 'react-router-dom';



function Dictionary() {
    const [data, setData] = useState(null) 
    const [error, setError] =  useState('')
    const [loading, setLoading] = useState(false)
    const location = useLocation();
    const { searchInput } = location.state || '';

    const [initialLoading, setInitialLoading] = useState(true); 

    const mode = dictionary
    
    const getMeaning = async (searchInput) => {
        //console.log("calling get meaning")
        setLoading(true)
        setData(null)
        setError(null)
        try{
            //const response = await axios.get(`http://localhost:5000/api/v1/dictionary/${searchInput}`)
            const response = await axios.get(`https://soundsohpisticated.onrender.com/api/v1/dictionary/${searchInput}`)
            if (response.status == 200){
                const word = response.data
                //console.log(word)
                setData(word)
                //console.log(word)
                //console.log(data)
            } 
        } catch(error) {
            if (error.response) {
                setError(error.response.data);        
            } else {
                setError(error.message);
            }
            setData(null);
        } finally {
            setLoading(false);
            setInitialLoading(false);
        }
    }

    useEffect(() => {
        //console.log("a search input was passed")
        if (searchInput){
            getMeaning(searchInput)
        }  else {
            setInitialLoading(false);  // No search input, set initial loading to false immediately
        }
    }, [searchInput])
        

        return (
            <>
                <Header mode={mode} getMeaning={getMeaning} passedSearchInput={searchInput}/>
                {data && <SearchedWord data={data}/>}
                {error && <p className={styles.error}>{error}</p>}
                {loading && <div className={styles.loader}><Loader/></div>}
                {!data && !error && !loading && !initialLoading && <DictionaryHome/>}
            </>  
        );     
}

export default Dictionary;