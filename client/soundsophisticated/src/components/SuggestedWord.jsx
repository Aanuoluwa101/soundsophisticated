import MeaningsAndExamples from './MeaningsAndExamples'
import icons from './icons'
import styles from '../styles/suggestedWord.module.css'
import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';


function SuggestedWord({ data }) {
    const navigate = useNavigate();
    const [suggestedWordsCount, setSuggestedWordsCount] = useState(null)

    
    useEffect(() => {
        const getSuggestedWordsCount = async () => {
            //console.log("calling get meaning")
            try{
                //const response = await axios.get(`http://localhost:5000/api/v1/assistant/suggest`)
                const response = await axios.get(`https://soundsohpisticated.onrender.com/api/v1/assistant/suggest`)
                if (response.status == 200){
                    setSuggestedWordsCount(response.data)
                } 
            } catch(error) {
                console.log(error.message)
            }
        }
        getSuggestedWordsCount();
    }, [])

    const handleClick = (searchInput) => {
        navigate('/dictionary', { state: { searchInput } });
      };

    
      
    return (
        <>
            <h2>{suggestedWordsCount} words suggested</h2>
            <article className={styles["word-box"]}>
                <div className={styles.head}>
                    <h2 className={styles.word}>{data.word}</h2>
                    <div className={styles["volume-icon"]}><img src={icons.volume}/></div>
                </div>
                
                <MeaningsAndExamples 
                    partOfSpeech={data.part_of_speech} 
                    definition={data.definition} 
                    example={data.example}
                    context={data.context} />
                <p className={styles["others-suggested"]}>See more on <span onClick={() => handleClick(data.word)} className={styles.word}>{data.word}</span> using the dictionary mode</p>
            </article>
        </>
    );
}

export default SuggestedWord;