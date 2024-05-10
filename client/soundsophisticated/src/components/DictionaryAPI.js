function getAllMeanings(meanings) {
    const allMeanings = meanings.flatMap(meaning =>
        meaning.definitions.map(definition => ({
          partOfSpeech: meaning.partOfSpeech,
          definition: definition.definition,
          example: definition.example
        }))
      );
    return allMeanings;
}

function findPronunciation(phonetics){
    for (const phonetic of phonetics){
      if (phonetic.audio.length > 0)
        return phonetic.audio
    }
    return ""
}

function processData(rawData) {
//   console.log("in processData")
//   console.log(rawData)
  const data = rawData[0]
  const { word, phonetic } = data 
  const pronunciation = findPronunciation(data.phonetics)
  const meanings = getAllMeanings(data.meanings)

  //console.log('in process data')

  return {
    word, 
    phonetic,
    pronunciation,
    meanings
  }
}

export default processData;