# [PYTHON] ASCII generator

## Introduction

Here is my python source code for ASCII generator. With my code: 
* **Given input image, we could generate ASCII art stored under text format in different languages (.txt)**
* **Given input image, we could generate ASCII art stored under image formats in different languages (.png, .jpg, ...).**
* **Given input video, we could generate ASCII art stored under video formats in different languages (.avi, .mp4, ...)**
* **Video/image outputs could be in grayscale or color format. It is totally up to you**

## Video to video
By running the sript **video2video_color.py** or **video2video.py** with different values for *background* and *mode*, we will have different outputs, for example:
<p align="center">
  <img src="data/vid2vid_output.gif" controls title="<img src=" width=800><br/>"></img>
  <i>Colored complex-character ASCII output</i>
</p>

## Image to text
By running the sript **img2txt.py**, we will have following outputs:
<p align="center">
  <img src="input/corgi.jpg" width=800><br/>
  <i>Input image</i>
</p>

<p align="center">
  <img src="data/img2text.jpg" width=800><br/>
  <i>Complex character ASCII output</i>
</p>

## Image to image
By running the sript **img2img_color.py** or **img2img.py** with different values for *background* and *mode*, we will have following outputs:
<p align="center">
  <img src="input/corgi.jpg" width=800><br/>
  <i>Input image</i>
</p>

<p align="center">
  <img src="data/img2color_output.jpg" width=800><br/>
  <i>Colored ASCII output</i>
</p>

## Requirements

* **python 3.6**
* **cv2**
* **PIL** 
* **numpy**