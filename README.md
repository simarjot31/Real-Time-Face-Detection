# Real-Time-Face-Detection
This repository demonstrates real-time face detection using Python and OpenCV. The system captures live video from the webcam, detects faces in each frame using a pre-trained Haar Cascade Classifier, and displays the bounding boxes around detected faces, along with the total number of faces detected in real-time.

## Installation
1. Clone or download this repository.
   
2. Navigate to the project directory:
    cd real-time-face-detection       #bash

3. Create a virtual environment (optional but recommended):
    python -m venv venv     #bash
    source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install the required dependencies:
    pip install -r requirements.txt     #bash

5. Download the Haar Cascade XML file: Download the haarcascade_frontalface_default.xml from this link and place it in your project folder.
