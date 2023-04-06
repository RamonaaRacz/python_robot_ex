import re
from pprint import pprint
from datetime import datetime


start_android_app = "ActivityTaskManager: START u0"
stop_android_app = "Layer: Destroyed ActivityRecord"
stored_info = []
extract_info = {}


def received_text():
    with open("logcat_applications.txt", "rt") as file:
        for text_line in file:
            if start_android_app in text_line:
                stored_info.append(text_line)
            elif stop_android_app in text_line:
                stored_info.append(text_line)


def extract_text():
    for line in stored_info:
        time = re.search(r'\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}', line)
        # time = re.search(r'\d{2}- \d{2} \d{2}:\d{2}:\d{2}\. \d{3}', line)  # print time
        # package = re.search("cmp=([\w\./]+)", line)  # print package
        package = re.search('cmp=([\w\./]+)', line)
        start_app = time.group(0)

        if package and time:
            app_path = package.group(1)
            app = 'application_{}'.format(len(extract_info) + 1)
            extract_info[app] = {"app_path": app_path, 'ts_app_started': start_app, 'ts_app_closed': None, 'lifespan': None}

        else:
            if stop_android_app in line:
                pack = re.search(r"com.([\w.]+)", line)
                stop_date = time.group(0)
                path = pack.group(0)
                for applications in extract_info.items():
                    if path in applications[1]['app_path']:
                        applications[1]['ts_app_closed'] = stop_date
                        time_stop = datetime.strptime(stop_date, '%m-%d %H:%M:%S.%f')
                        time_start = datetime.strptime(applications[1]['ts_app_started'], '%m-%d %H:%M:%S.%f')
                        lifespan = time_stop - time_start
                        applications[1]['lifespan'] = str(lifespan.total_seconds()) + "s"

    pprint(extract_info)

if __name__ == "__main__":
    received_text()
    extract_text()
