<h1 align="center" id="title">Controlling an electric vehicle model with mechanical wheels</h1>
<p align="center"><a href="https://imgur.com/70rNCbi"><img src="https://i.imgur.com/70rNCbim.png" title="source: imgur.com" /></a><a href="https://imgur.com/52Fler7"><img src="https://i.imgur.com/52Fler7m.png" title="source: imgur.com" /></a></p>

<p align="center">
 ![ezgif-4-59eba43863](https://github.com/mizticer/Control-of-an-electric-vehicle-model-with-mecanum-wheels/assets/68850404/eee3d9a0-5391-4be5-8bad-bbb5acde2c69)
</p>
<h2>💻 The concept:</h2>
The idea behind this project was to build and program an electric vehicle model. The user, using a mobile application, has the ability to remotely control the the vehicle. One of the functions will be free driving. It will vary depending on the type of wheels installed in the vehicle. Multidirectional wheels will be used, which base their design on rollers. They will increase the vehicle's range of motion. The Raspberry computer Pi 4 allows fully advanced control of the vehicle and the attachment of external components such as a camera. The computer is equipped with a Bluetooth module. It allows It provides wireless connectivity with a phone. The user of the mobile application can to select the function performed by the vehicle. The main program performs certain controls depending on the user's choice in the mobile application. One of the vehicle's functions is to move along a random route. The mobile application user can choose the color of the route along which the vehicle will move. For this purpose, the vehicle is equipped with a camera. The program analyzes the image from the camera and steers the vehicle accordingly.


<h2>🛠️ Components :</h2>
<p> </p>
<p>1. Raspberry Pi 4</p>
<p>2. 2x Controller LM298N</p>
<p>3. 4x Mecanum Wheel</p>
<p>4. PowerBank</p>
<p>5. 2x 18650 Battery</p>
<p>6. Camera</p>
<p>7. 4x DC motors</p>


<h2>📚 Modules and libraries:</h2>
<p> </p>
Modules:

- main.py - main program,
- Bluetooth.py - Bluetooth communication,
- Motor.py - creation of motor instances,
- Speed.py - changing the speed value,
- Directions.py - defining the range of movement of the vehicle,
- Detect.py - route detection,
- Regulator.py - PID controller,
- Controller.py - control the motors while driving on the line.

Libraries used:
- RPi.GPIO - GPIO control,
- Bluetooth - support for communication between phone and computer,
- threading - creating a multi-threaded program,
- cv2 - analyzing and processing camera images,
- numpy - performing elementary calculations on matrices,
- PiCamera - handling the camera,
- time - provides time-related functions.


<h2>⚡ Electrical diagram:</h2>
<p align="center"><a href="https://imgur.com/Zd0pFng"  ><img src="https://i.imgur.com/Zd0pFngl.png" title="source: imgur.com" /></a></p>

<h2>📷 Photo:</h2>
<p align="center"><a href="https://imgur.com/E7qJVhr"><img src="https://i.imgur.com/E7qJVhrl.png" title="source: imgur.com" /></a></p>
<h2 align="center">Mobile app for control</h2>
<p align="center"><a href="https://imgur.com/QmjS4fD"><img src="https://i.imgur.com/QmjS4fDl.png" title="source: imgur.com" /></a><a href="https://imgur.com/8VqZEo9"><img src="https://i.imgur.com/8VqZEo9l.png" title="source: imgur.com" /></a></p>
<h2 align="center">Use OpenCV to detect colorful road</h2>
<p align="center"><a href="https://imgur.com/a7xdCki"><img src="https://i.imgur.com/a7xdCkil.png" title="source: imgur.com" /></a></p>
<h2 align="center">Possible directions of movement</h2>
