# Fast Object Tracking for Depth Cameras and Sensors

This program performs fast object tracking under special conditions: both depth sensor and background are stationary, and detection characteristcs are known. Goal of this program is to be fast and concise.

Detecting and tracking objects in general rely on computer vision and machine learning algorithms. In special cases where environment information is known, it is possible to use faster and more efficient algorithms at a loss of generality.

# Performance
On depth stream of 200,000 points/frame, this program achieves greater than real time performance using a single core. (35 FPS processing batch of 1000 frames on one core of Ryzen 3600 CPU)

# License and Copyright
Copyright 2021 David Y. Wang

GNU AGPLv3 
