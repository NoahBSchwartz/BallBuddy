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


![Screenshot 2023-08-18 at 6 47 21 PM](https://github.com/NoahBSchwartz/BallBuddy/assets/44248582/28d31610-2d85-4808-a584-5e53ebdf3e02)
