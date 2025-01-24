import React from 'react';
import { useNavigate } from 'react-router-dom';

const HomePage = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex flex-col bg-black">
      {/* Navigation Bar */}
      <nav className="bg-white bg-opacity-10 backdrop-blur-md p-4 flex justify-end">
        <button
          onClick={() => navigate('/home')}
          className="py-2 px-6 bg-red-600 text-white font-bold rounded-full shadow-lg transition-all duration-300 ease-in-out hover:bg-red-700"
        >
          Learn Language
        </button>
        <button
          onClick={() => navigate('/ai-learning')}
          className="ml-4 py-2 px-6 bg-red-600 text-white font-bold rounded-full shadow-lg transition-all duration-300 ease-in-out hover:bg-red-700"
        >
          AI Learning
        </button>
        <button
          onClick={() => navigate('/examlist')}
          className="ml-4 py-2 px-6 bg-red-600 text-white font-bold rounded-full shadow-lg transition-all duration-300 ease-in-out hover:bg-red-700"
        >
          Exams
        </button>
        <button
          onClick={() => navigate('/Insertfile')}
          className="ml-4 py-2 px-6 bg-blue-600 text-white font-bold rounded-full shadow-lg transition-all duration-300 ease-in-out hover:bg-blue-700"
        >
          Upload
        </button>
      </nav>

      {/* Main Content */}
      <div className="flex-1 flex items-center justify-center">
        <div className="text-center bg-white bg-opacity-10 backdrop-blur-md p-10 rounded-xl shadow-2xl transition-all duration-300 ease-in-out">
          <h1 className="text-4xl text-white mb-5">Welcome to Learning Platform</h1>
          <p className="text-lg text-white text-opacity-80 mb-8">
            Your gateway to knowledge and success
          </p>
        </div>
      </div>

      {/* Footer */}
      <footer className="bg-white bg-opacity-10 backdrop-blur-md p-4 text-center text-white text-sm">
        <p>© 2025 Learning Platform. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default HomePage;
