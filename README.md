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

# Introduction

In this project Mediapipe facial landmarks and opencv is used to add makeup on facial features.
- Mediapipe facial landmark library detects the face in the image and returns 478 landmarks on human face. (x,y) coordinates of each points is obtained w.r.t the image size.

<p align="center">

  <br>
  <b>Media pipe facial landmarks</b>
</p>

- From all the facial landmarks, extract Lips, Eyebrow, Eyeliner & Eyeshadow points and create a colored mask with respect to the input image.

<p align="center">
  <br>
  <b>Colored Mask for Lips, Eyebrow, Eyeliner & Eyeshadow</b>
</p>

- Blend the Original image and the mask with respect to its weights to add makeup on the original image.

<p align="center">
  <br>
  <b>Original image and Transformed Image with Makeup</b>
</p>

- Virtual Makeup on video.
  
<p align="center">
  <a href="sample/output_video.mp4">
      <br>
    <b>Virtal makeup on video</b>
  </a>
  
</p>

-
