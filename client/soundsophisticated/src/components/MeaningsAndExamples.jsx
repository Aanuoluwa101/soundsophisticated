import React from 'react'
import styles from '../styles/word.module.css'


function MeaningsAndExamples({ partOfSpeech, definition, example, context }) {
    return (
      <div className={styles["meaning-and-examples"]}>
            <div className={styles["meaning-container"]}>
                <p className={styles["part-of-speech"]}>{partOfSpeech}</p>
                <p className={styles.meaning}>{definition}</p>
            </div>
            <div className={styles["examples-container"]}>
                {context ? <p>Example in context <span className={styles.context}>{context}</span></p>: <p>Example</p>}
                <ul>
                    <li>{example}</li>
                </ul>
            </div>
      </div>
    );
}

export default MeaningsAndExamples;