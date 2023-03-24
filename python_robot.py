# def received_text():
# file = open("logcat_applications.txt", 'rt')
# file_content = file.read()
# print(file_content)
# file.close()

import re

start_android_app = "ActivityTaskManager: START u0"
stop_android_app = "Layer: Destroyed ActivityRecord"
stored_info = []
extract_info = {}

def received_text():
    with open("logcat_applications.txt", "rt") as file:
        for text_line in file:
            if start_android_app in text_line:
                stored_info.append(text_line)
            if stop_android_app in text_line:
                stored_info(text_line)

def extract_text():


if __name__ == "__main__":
    received_text()


