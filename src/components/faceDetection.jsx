// import React, { useRef, useState, useCallback } from 'react';
// import Webcam from 'react-webcam';

// function FaceDetection() {
//   const webcamRef = useRef(null);
//   const [imageSrc, setImageSrc] = useState(null);
//   const [selectedFile, setSelectedFile] = useState(null);
//   const [uploadStatus, setUploadStatus] = useState('');

//   // Handle file selection
//   const handleFileChange = (event) => {
//     setSelectedFile(event.target.files[0]);
//   };

//   // Handle image upload
//   const handleUpload = async () => {
//     if (!selectedFile) {
//       alert('Please select an image file to upload.');
//       return;
//     }

//     const formData = new FormData();
//     formData.append('file', selectedFile);

//     try {
//       const response = await fetch('http://localhost:5000/upload-image', {
//         method: 'POST',
//         body: formData,
//       });

//       const data = await response.json();
//       if (response.ok) {
//         setUploadStatus(`Image uploaded successfully! Path: ${data.image_path}`);
//       } else {
//         setUploadStatus('Error uploading image');
//       }
//     } catch (error) {
//       console.error('Error uploading image:', error);
//       setUploadStatus('Error uploading image');
//     }
//   };
//   const capture = useCallback(() => {
//     const imageSrc = webcamRef.current.getScreenshot();
//     setImageSrc(imageSrc); 
//   }, [webcamRef]);

//   const handleSubmit = async () => {
//     const formData = new FormData();
    

//     const response = await fetch(imageSrc);
//     const blob = await response.blob();
//     formData.append('file', blob, 'captured_image.jpg');  // 'file' is the name used in Flask for file input

//     // Send the form data to the backend
//     const result = await fetch("http://localhost:5000/upload", {
//       method: "POST",
//       body: formData,  // FormData object contains the file
//     });

//     const resultText = await result.text();
//     alert(resultText);  // Display the result
//   };

//   return (
//     <div>
//       <h1>Face Recognition</h1>
//       <Webcam
//         audio={false}
//         ref={webcamRef}
//         screenshotFormat="image/jpeg"
//         width={320}
//         height={240}
//       />
//       <br />
//       <button onClick={capture}>Capture Image</button>
//       {imageSrc && (
//         <>
//           <img src={imageSrc} alt="captured" />
//           <br />
//           <button onClick={handleSubmit}>Send to Detect</button>
//         </>
//       )}
//        <div>
//       <h1>Image Upload</h1>
//       <input type="file" onChange={handleFileChange} accept="image/*" />
//       <br />
//       <button onClick={handleUpload}>Upload Image</button>
//       {uploadStatus && <p>{uploadStatus}</p>}
//     </div>
//     </div>
//   );
// }

// export default FaceDetection;

import axios from 'axios';
import React, { useRef, useState, useEffect, useCallback } from 'react';
import Webcam from 'react-webcam';

function FaceDetection() {
  const webcamRef = useRef(null);
  const [uploadStatus, setUploadStatus] = useState('');
  const [isCapturing, setIsCapturing] = useState(false); // State to track capturing process

  // Function to capture image from webcam and send it directly to the backend
  const captureAndSend = useCallback(async () => {
    setIsCapturing(true); // Indicate that capturing is in progress

    const imageSrc = webcamRef.current.getScreenshot();
    if (!imageSrc) {
      setUploadStatus('Error capturing image');
      setIsCapturing(false);
      return;
    }

    // Convert the base64 image to a blob and prepare form data
    try {
      // const response = await fetch(imageSrc);
      // const blob = await response.blob();
      // const formData = new FormData();
      // formData.append('file', blob, 'captured_image.jpg');  // 'file' is the name used in Flask for file input

      // // Send the form data to the backend
      // const result = await fetch("http://localhost:5000/upload", {
      //   method: "POST",
      //   body: formData,  // FormData object contains the file
      // });

      // const resultText = await result.text();
      
      // setUploadStatus(resultText);  // Display the result

          // Fetch the image as a blob from the provided image source
    const response = await fetch(imageSrc);
    const blob = await response.blob();

    // Create a new FormData object and append the blob with a filename
    const formData = new FormData();
    formData.append('file', blob, 'captured_image.jpg');  // 'file' is the key expected by Flask

    // Send the form data to the backend using axios
    const result = await axios.post("https://c1d958060255ed0454dfbd096bf7ac38.serveo.net/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    setUploadStatus(result.data?.status); 
   console.log(result);
    // Display the result
    // setUploadStatus(result.data);  // Assuming setUploadStatus is a state setter for displaying the result

    } catch (error) {
      console.error('Error sending captured image:', error);
      setUploadStatus('Error sending image');
    } finally {
      setIsCapturing(false); // Reset capturing state
    }
  }, [webcamRef]);

  // Start capturing images at a fixed interval when component mounts
  useEffect(() => {
    let intervalId;
    
    const startCapturing = () => {
      intervalId = setInterval(() => {
        if (!isCapturing) {
          captureAndSend();
        }
      }, 5000); // Adjust the interval as needed (5000 ms = 5 seconds)
    };

    startCapturing();

    // Clear interval on component unmount
    return () => clearInterval(intervalId);
  }, [captureAndSend, isCapturing]);

  return (
    <div>
      <h1>Face Recognition</h1>
      <Webcam
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={320}
        height={240}
      />
      {uploadStatus && <p>{uploadStatus}</p>}
    </div>
  );
}

export default FaceDetection 