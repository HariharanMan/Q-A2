import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './page/Login';
import AdminHome from './page/AdminHome';
import Signup from './page/Signup';

function App() {
  return (
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/adminhome" element={<AdminHome />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
  );
}

export default App;