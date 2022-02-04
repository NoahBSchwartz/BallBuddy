# Self-Aiming-Cannon
The goal of this project was to make an autonomous, self contained turret as cheaply as possible (I spent just $40 on the build). Because it was done so cheaply, I used a Raspberry Pi Zero which could only process one image every few seconds. To get around this speed problem, I sent the Pi's video stream to be processed on a separate computer which then sent commands back to the robot. I first streamed the Raspberry Pi's video to a webpage. From my laptop, I could analyze the stream (using tracker.py and gestureDetector.py) to find my hand coordinates and the number of fingers I had up. I sent this data back to the Raspberry Pi and it positioned the servos, activated the pump once I made a fist, and stopped the pump when the ball left the barrel. The turret followed my hand in realtime, more than 30 times as fast as it had when processing only on the Pi. 
