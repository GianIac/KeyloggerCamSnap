# KeyloggerCamSnap
KeyloggerCamSnap is a Python-based monitoring tool that logs keystrokes and takes periodic screenshots and webcam images.
I suppose I will integrate new features, at the moment it is in embryonic stage. 

video: 

https://github.com/GianIac/KeyloggerCamSnap/assets/80957309/e864a18f-a82a-479f-9dfb-67ce6af87ca5



# Disclaimer
Ufff ! I don't like write this, but this tool is provided for educational use only. Alright? Use it wisely ;)

# Features
<li>Keystroke logging with the window title context.</li>
<li>Periodic screenshots.</li>
<li>Webcam image capture.</li>

# Requirements
To run this project, you'll need to install the required Python packages. Install them using:
>> pip install -r requirements.txt

# Usage
Clone the repository to your local machine, navigate to the project directory and Run main.py to start the monitoring process.
>> python main.py
Check the log directory for the keystroke logs, screenshots, and webcam images.

# How it Works
main.py sets up logging and initiates a daemon thread that runs periodic tasks, such as capturing screenshots and webcam images every 5 minutes. It uses pynput to monitor and log keystrokes and mouse clicks.

# Contributions
Contributions to this project are welcome, especially those that improve functionality or adhere to best privacy practices.
