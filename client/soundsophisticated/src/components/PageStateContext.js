import React, { createContext, useContext, useState } from 'react';

const PageStateContext = createContext();

export const usePageState = () => {
    console.log("calling the usePageState hook!")
    return useContext(PageStateContext);
}

export const PageStateProvider = ({ children }) => {
  const [assistantState, setAssistantState] = useState({});
  const [dictionaryState, setDictionaryState] = useState({});

  return (
    <PageStateContext.Provider value={{ assistantState, setAssistantState, dictionaryState, setDictionaryState }}>
      {children}
    </PageStateContext.Provider>
  );
};
