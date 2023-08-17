# Self-Aiming-Cannon 

An autonomous, self-contained turret built for under $40 

## 🚀 Overview

I used a **Raspberry Pi Zero** to make this build even cheaper. It could only process one image every few seconds so 
I had to send the data back and forth to my laptop for further processing. 

## 🛠 Process

1. Stream the Raspberry Pi's video to a webpage.
   
2. Analyze the stream to find hand coordinates and gestures on an external computer.
   
3. Send hand coordinates and finger count data back to the Raspberry Pi.
   
4. Position the servos, activate the pump when five fingers are detected, and stop the pump when the ball leaves the barrel.

## 📷 Demo

![Self Aiming Cannon Demo](https://github.com/NoahBSchwartz/Self-Aiming-Cannon/assets/44248582/719d333b-5602-4cad-a93b-8f3a38d87380)
