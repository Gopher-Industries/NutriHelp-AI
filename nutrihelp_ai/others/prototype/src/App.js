import React from 'react';
import { BrowserRouter as Router, Navigate, Route, Routes } from 'react-router-dom';
import ObesityPredict from './components/ObesityPredict';
import ObesityResult from './components/ObesityResult';
import Nutribot from './components/Nutribot';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/nutribot" replace />} />
        <Route path="/nutribot" element={<Nutribot />} />
        <Route path="/predict" element={<ObesityPredict />} />
        <Route path="/predict/result" element={<ObesityResult />} />
        <Route path="*" element={<Navigate to="/nutribot" replace />} />
      </Routes>
    </Router>
  );
}

export default App;