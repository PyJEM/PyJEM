# PyJEM: External control of JEOL TEM

**This site handles inquiries about PyJEM only.**  
**For instrument or JEOL software questions, contact your sales representative.**

- **Documentation** : https://pyjem.github.io/PyJEM/
- **Released** : https://github.com/PyJEM/PyJEM/tags
- **Share scripts** : https://github.com/PyJEM/ScriptCode/tree/master/trunk
- **Bug reports** : https://github.com/PyJEM/PyJEM/issues


#### Features provided:
- TEM unit control : beam, optics, stage, etc.
- Auto functions : auto-focus, auto-contrast-brightness, etc.
- Detector control : imaging, acquiring/changing imaging conditions, etc.
- Functions for other proprietary software, etc.

## vjem
vjem is a recommendate python environment for PyJEM development.
The vjem environment includes libraries such as NumPy and OpenCV.
It also makes it easier to specify and share recommended environments when exchanging code.

- python 3.10 : [vjem310.yml](vjem/vjem310.yml)
- python 3.9 : [vjem39.yml](vjem/vjem39.yml)

## Network model
**TEM PC (PyJEM is pre‑installed)**
- Older systems may not include PyJEM — contact your sales representative for installation.

**other PC (Remote control)**
- the PC with PyJEM and the TEM PC (TEMPC) are on the same network, remote operation is possible.
- To enable remote control, set the IP address in each relevant PyJEM package.

## Share scripts
We provide a [space](https://github.com/PyJEM/ScriptCode/tree/master/trunk) where users can share their scripts.
