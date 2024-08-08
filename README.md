# Virtual Makeup
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

In this project Mediapipe [1] facial landmarks and opencv is used to add makeup on facial features.
- Mediapipe facial landmark library detects the face in the image and returns 478 landmarks on human face. (x,y) coordinates of each points is obtained w.r.t the image size.

<p align="center">
  <img src="sample/facial_landmarks.jpeg" alt="Landmarks image">
  <br>
  <b>Media pipe facial landmarks example [2]</b>
</p>

- From all the facial landmarks, extract Lips, Eyebrow, Eyeliner & Eyeshadow points and create a colored mask with respect to the input image.

<p align="center">
  <img src="sample/mask.png" alt="mask" width="200" height="200">
  <br>
  <b>Colored Mask for Lips, Eyebrow, Eyeliner & Eyeshadow</b>
</p>

- Blend the Original image and the mask with respect to its weights to add makeup on the original image.

<p align="center">
  <img src="sample/comparison.png" alt="mask" width="500" height="300">
  <br>
  <b>Original image and Transformed Image with Makeup [3]</b>
</p>

- Virtual Makeup on video.
  
<p align="center">
  <a href="sample/output_video.mp4">
    <img src="sample/000.png" alt="Watch the video" width="600" height="auto">
      <br>
    <b>Virtal makeup on video [4]</b>
  </a>
  
</p>

-
