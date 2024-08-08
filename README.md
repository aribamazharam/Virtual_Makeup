# Virtual Makeup
## Overview

This project applies virtual makeup to facial images or real-time video using Mediapipe and OpenCV. The makeup effects include applying lipstick, eyeliner, eyeshadow, and enhancing eyebrows. The project detects facial landmarks using Mediapipe and creates a mask to apply the desired makeup colors on the face.

## Features

- **Real-time Virtual Makeup**: Apply makeup to a live video stream from your camera.
- **Image-based Virtual Makeup**: Apply makeup to a static image.
- **Customizable Makeup Colors**: Easily modify the colors used for different facial features.
- **Mediapipe Facial Landmarks**: Utilizes Mediapipe to detect 478 facial landmarks, ensuring precise application of makeup.
  
## Clone  and Run
```
git clone 
cd Virtual_Makeup_opencv
conda env create -f environment.yml
conda activate virtual_makeup
```
### Run on Camera input
```
python camera.py
```
### Run on sample image
```
python image.py --img sample/face.png
```


