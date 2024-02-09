PyJEM
=====================
This site only answers questions about PyJEM. 

- Manual : [PyJEM manual](https://pyjem.github.io/PyJEM/)

vjem (python virtual environment)
------------------------------------
vjem is a recommendate virtual python environment for PyJEM development.

- python 3.5 : [vjem35.yml](vjem/vjem35.yml)
- python 3.7 : [vjem37.yml](vjem/vjem37.yml)
- python 3.8 : [vjem38.yml](vjem/vjem38.yml)
- python 3.9 : [vjem39.yml](vjem/vjem39.yml)
- python 3.10 : [vjem310.yml](vjem/vjem310.yml)

Summary
---------
  In recent years, there is an increasing demand to automatically control from 
  TEM control to acquisition of images, and to control the TEM remotely. 
  Until now, it was necessary to organize programs using TEM external control 
  (TEMExt) written in C ++, but there are problems such as the high level of 
  hurdling to create programs in C ++ language and few functions available in TEMExt had.
  
PyJEM solved these problems. Since PyJEM is a python library, 
  we can interactively control TEM. 
  In addition, functions available from existing TEMExt are powered up, enabling remote control.


What you can do with PyJEM
----------------------------
With PyJEM, it is relatively easy to control the TEM itself and acquire images. 
By combining this with a rich Python library you can create a variety of applications.

* **Electronic optical system control**： 
  
  Beam control, detector In / Out, magnification change, brightness change, etc..

* **Stage control**：

  Absolute position movement, Relative position movement, Piezoelectric movement, etc..

* **Image acquisition**：

  STEM or TEM image acquisition, image storage type change, resolution specification, etc..

* **Auto function**：

  Auto Focus、Auto Contrast Brightness、Auto Stigmator, etc..

