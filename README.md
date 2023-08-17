# Self-Aiming-Cannon 🎯

## 🎯 Goal

The goal of this project was to make an autonomous, self-contained turret as cheaply as possible. Total cost of the build: **$40**.

## 🥧 Hardware

- Raspberry Pi Zero 

## 🚀 Overview

Because it was done so cheaply, I used a **Raspberry Pi Zero** which could only process one image every few seconds. To get around this speed problem, I sent the Pi's video stream to be processed on a separate computer which then sent commands back to the robot. 

## 🛠 Process

1. **Stream Video:** 
   - Stream the Raspberry Pi's video to a webpage.
   
2. **Analyze Stream on Laptop:** 
   - From my laptop, I could analyze the stream to find my hand coordinates and the number of fingers I had up.
   
3. **Send Data Back to Pi:** 
   - Send the hand coordinates and finger count data back to the Raspberry Pi.
   
4. **Control the Turret:** 
   - The Pi positioned the servos, activated the pump once I made a fist, and stopped the pump when the ball left the barrel.
   
5. **Real-Time Tracking:** 
   - The turret followed my hand in real-time, more than **30 times as fast** as it had when processing only on the Pi.

## 📷 Demo

![Self Aiming Cannon Demo](https://github.com/NoahBSchwartz/Self-Aiming-Cannon/assets/44248582/719d333b-5602-4cad-a93b-8f3a38d87380)

## 💰 Budget

- Total cost of the build: **$40**

## 📑 Dependencies

(List any software or libraries that are required to run this project.)

## 🚀 How to Use

(Provide step by step instructions for setting up and running the project.)

## 🤝 Contributors

- [Noah B Schwartz](https://github.com/NoahBSchwartz)

## 📝 License

(If you are using a license, mention it here and link it.)
