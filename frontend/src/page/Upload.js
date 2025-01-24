import React, { useState } from 'react';
import axios from 'axios';

const InsertFile = () => {
  const [file, setFile] = useState(null);
  const [title, setTitle] = useState('');
  const [fileFormat, setFileFormat] = useState('Q&A');
  const [message, setMessage] = useState('');

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file || !title) {
      setMessage('Please provide all required fields (Title and File).');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append('title', title);
    formData.append('fileFormat', fileFormat);

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/Insertfile/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setMessage(response.data.message);
    } catch (error) {
      setMessage('An error occurred while uploading the file.');
    }
  };

  return (
    <div className="container mx-auto p-5">
      <h2 className="text-xl font-bold mb-4">Upload File with Additional Metadata</h2>

      {/* Title Input */}
      <div className="mb-3">
        <label className="block text-sm font-bold mb-1">Title:</label>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Enter the title"
          className="w-full p-2 border border-gray-300 rounded"
        />
      </div>

      {/* Dropdown for File Format */}
      <div className="mb-3">
        <label className="block text-sm font-bold mb-1">File Format:</label>
        <select
          value={fileFormat}
          onChange={(e) => setFileFormat(e.target.value)}
          className="w-full p-2 border border-gray-300 rounded"
        >
          <option value="Q&A">Q&A</option>
          <option value="Table">Table</option>
          <option value="Paragraph">Paragraph</option>
        </select>
      </div>

      {/* File Input */}
      <div className="mb-3">
        <label className="block text-sm font-bold mb-1">Select File:</label>
        <input
          type="file"
          accept=".csv"
          onChange={handleFileChange}
          className="w-full p-2 border border-gray-300 rounded"
        />
      </div>

      {/* Upload Button */}
      <button
        onClick={handleUpload}
        className="bg-blue-500 text-white py-2 px-4 rounded"
      >
        Upload
      </button>

      {/* Message */}
      {message && <p className="mt-3 text-red-500">{message}</p>}
    </div>
  );
};

export default InsertFile;
