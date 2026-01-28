# 📄 Document Boundary Detection using Computer Vision.

## 🔍 Overview
This project was developed as part of a technical assignment for the AI Trainee selection process. The objective is to design a generalized, training-free algorithm capable of detecting and extracting the boundaries of identity card–like documents under real-world conditions such as rotation, perspective distortion, occlusion, and background noise.
The solution is implemented as a real-time web application using Streamlit and OpenCV. It supports both image upload and live camera input and can be accessed from desktop as well as mobile devices.

## 🎯 Problem Statement:
- Detect boundaries of identity card–like documents.  
- No training data is provided.  
- Handle rotation, skew, occlusion, and noise.  
- Accept input images or live camera capture.  
- Output bordered and perspective-corrected document images  
- Provide complete documentation for easy evaluation.  .

## ✨ Key Features:
- Training-free document detection.  
- Image upload and live camera input support.  
- Works on both desktop and mobile browsers.  
- Robust to rotation and perspective skew. 
- Real-time processing.  
- Clean and modular code structure  .

## 🛠️ Technology Stack:
| Component | Technology |
|---------|------------|
| Programming Language | Python 3.8+ |
| Computer Vision | OpenCV |
| Web Framework | Streamlit |
| Numerical Computing | NumPy |

## 🧠 Algorithm Explanation:
The document detection pipeline is based on classical computer vision techniques:
1. Convert the input image to grayscale.
2. Apply Gaussian blur to reduce noise.
3. Perform Canny edge detection.
4. Detect contours from the edged image.
5. Sort contours by area and select the largest 4-point contour.
6. Draw the detected contour on the original image.
7. Apply perspective transformation to extract a top-down view of the document.

The algorithm returns:
- A bordered image with detected document boundaries.
- A cropped, perspective-corrected document image.

## 📁 Project Structure:

document_border_assignment/
├── app.py # Streamlit web application
├── detector.py # Document detection logic
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── data/
│ └── test_images/ # Sample test images
└── output/ # Generated outputs


## ⚙️ Installation:
### Prerequisites:
- Python 3.8 or higher.
- pip package manager.

### Install Dependencies:
pip install -r requirements.txt.

## ▶️ Running the Application:

streamlit run app.py:
The application will open in the default browser and can be accessed from desktop or mobile devices.

## 📷 Usage Instructions:
### Input Options.
- Upload Image: Upload JPG or PNG document images.
- Use Camera: Capture documents using webcam or mobile camera.

### Output:
- Original input image.
- Detected document with boundary.
- Extracted and perspective-corrected document.

## 📱 Mobile & Camera Support:
The application uses Streamlit’s camera input API, enabling real-time capture on desktop webcams and mobile cameras without requiring any app installation.

## 📊 Dataset Information:
No training dataset is required. The algorithm was tested using:
- MIDV-500 dataset.
- SmartDoc dataset.
- Custom mobile-captured images.

## ⚠️ Limitations:
- Heavy occlusion may reduce detection accuracy.
- Low-contrast images may affect edge detection.
- Assumes documents are approximately rectangular.

## 🚀 Future Enhancements:
- Automatic capture when document edges are detected.
- OCR integration for text extraction.
- Face masking for privacy.
- PDF export of extracted documents.
- Backend API using FastAPI.

## 🧪 Evaluation Alignment:
- Handles rotated, skewed, and noisy documents.
- Real-time performance.
- Cross-platform accessibility.
- Fully documented and reproducible.

## 🧾 Conclusion:
This project demonstrates a practical and efficient computer vision solution for real-time document boundary detection. It is training-free, robust, and suitable for real-world applications, fulfilling all requirements of the AI Trainee technical assignment.

## 👤 Author:
Mayur Patil.
AI / Machine Learning Enthusiast.  
Project submitted for AI Trainee selection process.


