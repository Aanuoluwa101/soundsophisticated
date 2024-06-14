import Loader from './Loader'
import axios from 'axios'
import styles from '../styles/word.module.css'
import { assistant } from './modes'
import SuggestedWord from './SuggestedWord'
import AssistantHome from './AssitantHome'
import Header from './Header'
import { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';





function Assistant() {
    const [data, setData] = useState(null) 
    const [error, setError] =  useState('')
    const [loading, setLoading] = useState(false)
    const location = useLocation();
    const { context } = location.state || '';

    const mode = assistant

    
    useEffect(() => {
        if (context){
            console.log("got hereeeeeeeeee")
            getSuggestion(context)
        }
    }, [context])


    const getSuggestion = async (word, context) => {
        setLoading(true)
        setData(null)
        setError(null)

        //console.log(word)
        //console.log(context)
        //const baseUrl = 'http://localhost:5000/api/v1'
        const baseUrl = 'https://soundsohpisticated.onrender.com/api/v1'
        const url = `${baseUrl}/assistant/suggest`;
        try{
            const response = await axios.post(url, {
                word: word,
                context: context
            })
            //console.log(response.data)
            setData(response.data)
            setLoading(false)
        } catch(error) {
            if (error.response) {
                setError(error.response.data);        
            } else {
                setError(error.message);
            }
            setData(null)
            setLoading(false)
            //console.log(error.response.data)
        }
    }

    
    return (
        <>
            <Header mode={mode} getSuggestion={getSuggestion} 
                                passedSearchInput={context}
                                />
            {data && <SuggestedWord data={data}/>}
            {error && <p className={styles.error}>{error}</p>}
            {loading && (
                <div className={styles.loader}>
                    <Loader/>
                </div>
            )}
            {!data && !error && !loading && <AssistantHome />}
        </>
    );
}

export default Assistant;