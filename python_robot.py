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
    for line in stored_info:
        time = re.search(r'\d{2}- \d{2}) \d{2}:\d{2}:\d{2}\. \d{3}', line)
        package = re.search("cmp=([\w\./]+)", line)
        start_app_date = time.group(0)
        if package and time:
            app = 'application{}'.format(len(extract_info) + 1)
            app_path = package.group(1)
            extract_info[app] = {"app_path", 'ts_app_started': start_android_app}
        if "/" in app_path:
            apps_value = app_path.split('/')[0]
            if apps_value and stop_android_app in line:
                stop = time.group(0)
                extract_info[app]['ts_app_closed'] = stop



if __name__ == "__main__":
    received_text()


