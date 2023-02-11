# 468 landmarks face Detection
![](https://github.com/sv2441/faceDetection/blob/master/results.gif)


In this Project I used Mediapipeline to Detect 468 Landmarks in Faces .
### Media Pipeline 
MediaPipe Face Mesh is a solution that estimates 468 3D face landmarks in real-time even on mobile devices. It employs machine learning (ML) to infer the 3D facial surface, requiring only a single camera input without the need for a dedicated depth sensor. Utilizing lightweight model architectures together with GPU acceleration throughout the pipeline, the solution delivers real-time performance critical for live experiences.

![](https://mediapipe.dev/images/mobile/face_mesh_android_gpu.gif)


Additionally, the solution is bundled with the Face Transform module that bridges the gap between the face landmark estimation and useful real-time augmented reality (AR) applications. It establishes a metric 3D space and uses the face landmark screen positions to estimate a face transform within that space. The face transform data consists of common 3D primitives, including a face pose transformation matrix and a triangular face mesh. Under the hood, a lightweight statistical analysis method called Procrustes Analysis is employed to drive a robust, performant and portable logic. The analysis runs on CPU and has a minimal speed/memory footprint on top of the ML model inference

#### for Python API 
Supported configuration options:

static_image_mode
max_num_faces
refine_landmarks
min_detection_confidence
min_tracking_confidence

## To Run This Project 
1) Fork the repo
2) Download Dependencies 
opencv , Mediapipeline
3) RUN the main.py file 


Thank You For Reading .
References:
https://google.github.io/mediapipe/solutions/face_mesh

