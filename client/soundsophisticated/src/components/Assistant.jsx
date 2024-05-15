import React, { useState } from 'react'
import Loader from './Loader'
import axios from 'axios'
import styles from '../styles/word.module.css'
import { assistant } from './modes'
import SuggestedWord from './SuggestedWord'
import AssistantHome from './AssitantHome'
import Header from './Header'
import { usePageState } from './PageStateContext';



function Assistant() {
    const [data, setData] = useState(null) 
    const [error, setError] =  useState('')
    const [loading, setLoading] = useState(false)

    //const { assistantState, setAssistantState } = usePageState();

    const mode = assistant

    
    const getSuggestion = async (context) => {
        setLoading(true)
        setData(null)
        setError(null)

        try{
            const response = await axios.post(`http://localhost:5000/api/v1/assistant/suggest/${context}`)
            //const response = await axios.post(`https://soundsohpisticated.onrender.com/api/v1/assistant/suggest/${context}`)
            console.log(response.data)
            setData(response.data)
            //setAssistantState({ ...assistantState, data: response.data });
            setLoading(false)
            // console.log(response.data)
        } catch(error) {
            setError(error.message)
            //setAssistantState({ ...assistantState, error: error.message });
            setData(null)
            //setAssistantState({ ...assistantState, data: null });
            setLoading(false)
            console.log(error.message)
        }
    }

    
    return (
        <>
            <Header mode={mode} getSuggestion={getSuggestion}/>
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