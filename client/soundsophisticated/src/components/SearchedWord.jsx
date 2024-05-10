import React, { useState, useEffect } from 'react'
import MeaningsAndExamples from './MeaningsAndExamples'
import icons from './icons'
import styles from '../styles/word.module.css'




function SearchedWord({ data }) {
    const [meanings, setMeanings] = useState(null)
    const [hasMultipleMeanings, setHasMultipleMeanings] =  useState(false)
    const [idx, setIdx] = useState(0)
    const [meaning, setMeaning] = useState(null)
    // const [colorIndex, setColorIndex] = useState(0);
    

    useEffect(() => {
        //console.log("idx useEffect")
        if (meanings)
            setMeaning(meanings[idx])
            // setColorIndex((colorIndex + 1) % colors.length);
        //console.log(`meaning is ${meaning}`)
    }, [idx])

    useEffect(() => {
        //console.log("data useEffect")
        if (data){
            setMeanings(data.meanings)
        }
    }, [data])

    useEffect(() => {
        //console.log("meanings useEffect")
        if (meanings){
            setHasMultipleMeanings(meanings.length > 1)
            setIdx(0)
            setMeaning(meanings[idx])
        }
    }, [meanings])


    // useEffect(() => {
    //     //console.log("searchInputOnClick useEffect")
    //     if (searchInputOnClick.length > 0){
            
    //         getMeaning();
    //     }
           
    // }, [searchInputOnClick])


        return (
            <article className={styles["word-box"]}>
                <h2 className={styles.word}>{data.word}</h2>
                <div className={styles.phonics}>
                    <p className={styles.transcription}>{data.phonetic}</p>
                    {data.phonetic && <div className={styles["volume-icon"]}><img src={icons.volume}/></div>}
                    {/* <p class="us-br"><a>us</a>|<a>br</a></p> */}
                </div>
                <MeaningsAndExamples 
                   partOfSpeech={meaning ? meaning.partOfSpeech : null} 
                   definition={meaning ? meaning.definition: null} 
                   example={meaning ? meaning.example: null} />
                {
                    hasMultipleMeanings && 
                        <div className={styles.others}>
                            {idx == 0 && <p>See more on <span className={styles.word}>{data.word}</span></p>}
                            {idx > 0 && <div onClick={() => setIdx(prevIdx => prevIdx - 1)} className={styles.previous}><img src={icons.previous}/></div>}
                            {idx >= 0 && idx < meanings?.length - 1 && <div onClick={() => setIdx(prevIdx => prevIdx + 1)} className={styles.next}><img src={icons.next}/></div>}
                        </div>
                }
            </article>
        );     
}

export default SearchedWord;