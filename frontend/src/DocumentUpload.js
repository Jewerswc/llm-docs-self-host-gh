import React, { useState } from 'react';
import axios from 'axios';

function DocumentUpload() {
  const [file, setFile] = useState(null);

  const handleUpload = () => {
    if (!file) {
      alert("Please select a file to upload.");
      return;
    }

    const formData = new FormData();
    formData.append('document', file);

    axios.post('/upload', formData)
      .then(response => alert(response.data.message))
      .catch(error => {
        console.error(error);
        alert("An error occurred while uploading the document.");
      });
  };

  return (
    <div>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload Document</button>
    </div>
  );
}

export default DocumentUpload;