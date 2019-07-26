import sys
import os

gitignore = ("__init__.py", "目录.md")
dict_file = {"py": "python文件", "MP3": "音频", "mp3": "音频"}

path = "."
level = 1
list_txt = ""


def writefile():
    with open("目录.txt", "w") as f:
        f.write(list_txt)


def get_list(level, file_path):
    global list_txt
    dir = False
    flag = " " * (level - 1) * 4 if level > 1 else ""
    for file in os.listdir(file_path):
        if file not in gitignore:
            new_file = file_path + "/" + file
            list_txt = list_txt + flag + file + "\n"
            if not os.path.isfile(new_file):
                dir = True
                new_level = level + 1
                new_path = file_path + "/" + file
                get_list(new_level, new_path)
    if not dir:
        return


if __name__ == '__main__':
    get_list(level, path)
    writefile()
