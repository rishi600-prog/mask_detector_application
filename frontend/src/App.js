import React from "react";
import UploadForm from "./components/UploadForm";
import "./index.css";

const App = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-center text-3xl font-bold text-gray-800 mb-6">
        Face Mask Detection
      </h1>
      <UploadForm />
    </div>
  );
};

export default App;
