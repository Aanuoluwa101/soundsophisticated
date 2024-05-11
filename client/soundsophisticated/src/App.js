import Assistant from './components/Assistant';
import Dictionary from './components/Dictionary';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


function App() {
  return (
    // <PageStateProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Assistant />} />
          <Route path="/assistant" element={<Assistant />} />
          <Route path="/dictionary" element={<Dictionary />} />
        </Routes>
      </Router>
    // </PageStateProvider>
  );
}

export default App;

