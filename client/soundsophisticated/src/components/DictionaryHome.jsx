import React, { useState, useEffect } from 'react';
import styles from '../styles/dictionaryHome.module.css';
import SearchedWord from './SearchedWord';
import axios from 'axios';
import Loader from './Loader'


const DictionaryHome = () => {
    const [data, setData] = useState(null);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false)

    useEffect(() => {
        const getWordOfTheDay = async () => {
            console.log("calling get word of the day");
            setData(null);
            setError(null);
            setLoading(true)
            try {
                //const response = await axios.get(`http://localhost:5000/api/v1/assistant/word_of_the_day`);
                const response = await axios.get(`https://soundsohpisticated.onrender.com/api/v1/assistant/word_of_the_day`);
                if (response.status === 200) {
                    const word = response.data;
                    setData(word);
                    // setLoading(false)
                    console.log(word);
                }
            } catch (error) {
                // setLoading(false)
                setError(error.message);
                setData(null);
            } finally {
                setLoading(false)
            }
        };
        getWordOfTheDay();
    }, []); 

    return (
        <div className={styles.container}>
            {data && <h1 className={styles.wordoftheday}>word of the day</h1>}
            {data && <SearchedWord data={data}/>}
            {error && !data && <p>{error}</p>}
            {loading && (
                <div className={styles.loader}>
                    <Loader/>
                </div>
            )}
        </div>
    );
}

export default DictionaryHome;
