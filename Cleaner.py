import os
import shutil
from datetime import datetime, timedelta

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")


important_extensions = ['.docx', '.pdf', '.xlsx']
junk_extensions = ['.tmp', '.log']
important_keywords = ['project', 'report']
junk_keywords = ['temp', 'backup']
important_age = timedelta(days=30)
junk_age = timedelta(days=365)


important_dir = os.path.join(desktop_path, 'Important_Files')
junk_dir = os.path.join(desktop_path, 'Junk_Files')


os.makedirs(important_dir, exist_ok=True)
os.makedirs(junk_dir, exist_ok=True)


now = datetime.now()


def is_important(file):
    ext = os.path.splitext(file)[1]
    if ext in important_extensions:
        return True
    if any(keyword in file for keyword in important_keywords):
        return True
    file_path = os.path.join(desktop_path, file)
    if os.path.getmtime(file_path) > (now - important_age).timestamp():
        return True
    return False


def is_junk(file):
    ext = os.path.splitext(file)[1]
    if ext in junk_extensions:
        return True
    if any(keyword in file for keyword in junk_keywords):
        return True
    file_path = os.path.join(desktop_path, file)
    if os.path.getmtime(file_path) < (now - junk_age).timestamp():
        return True
    return False


for file in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, file)
    if os.path.isfile(file_path):
        if is_important(file):
            shutil.move(file_path, important_dir)
        elif is_junk(file):
            shutil.move(file_path, junk_dir)

print("Files have been sorted.")
