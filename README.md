# IoT-Enabled Smart Pill Bottle

This project focuses on designing an IoT-based Smart Pill Bottle to automatically
monitor pill quantity and provide timely medicine reordering indication.

## Problem Statement
Patients often forget to monitor the remaining quantity of medicines, which leads
to missed doses and delayed medicine reordering.

## Proposed Solution
The system uses an ultrasonic sensor to detect pill levels inside the bottle.
An Arduino microcontroller processes the sensor data and sends pill status to a
mobile application via Bluetooth (HC-05).

## Features
- Automatic pill quantity monitoring
- Threshold-based low medicine detection
- Wireless communication using Bluetooth
- Mobile application for pill status display

## Hardware Used
- Arduino microcontroller
- Ultrasonic sensor
- Bluetooth module (HC-05)

## Software Used
- Arduino IDE
- Python (Kivy framework)

## Applications
- Home healthcare
- Elderly care
- Chronic disease management

## Repository Structure
- Arduino_Code/ : Arduino program for pill level detection
- Mobile_Application_Code/ : Mobile app source files
- Documentation/ : Project report and presentation
- Images/ : System diagram and prototype images

