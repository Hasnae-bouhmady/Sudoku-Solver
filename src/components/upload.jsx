import React, { useState } from "react";
import "./App.css";

function Upload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [isFilePicked, setIsFilePicked] = useState(false);

  const fileSelectedHandler = (event) => {
    setSelectedFile(event.target.files[0]);
    setIsFilePicked(true);
  };

  const fileUploadHandler = () => {
    const formData = new FormData();
    formData.append("image", selectedFile);

    fetch("http://127.0.0.1:5000/getPuzzle",{
      method: "POST",
      body: formData,
    }).then(response => {
      console.log(response);
    })
  };
  

  return (
    <div className="sudokufile">
      <label>Upload Here a picture of your sudoku</label>
      <br />

      <input
        type="file"
        id="sudoku"
        name="file"
        onChange={fileSelectedHandler}
      />
      <button type="button" onClick={fileUploadHandler}>
        solve
      </button>
    </div>
  );
}

export default Upload;
