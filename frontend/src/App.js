import React from 'react';
import Home from './pages/Home';
import Player from './pages/Player';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

function App() {
  return (
    <Router>
    <Routes>
      <Route path="/" element={<Home/>} />
      <Route path="/player/:id" element={<Player/>} />
    </Routes>
  </Router>
  );
}

export default App;

