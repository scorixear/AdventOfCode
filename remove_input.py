import os, sys


def remove_input():
    # for each directory in the current directory
    for directory in os.listdir():
        if directory.isnumeric():
            for sub_dir in os.listdir(directory):
                if sub_dir.isnumeric():
                    # for each file in the subdirectory
                    for file in os.listdir(os.path.join(directory, sub_dir)):
                        if file == "input.txt":
                            # move file to current directory
                            os.rename(os.path.join(directory, sub_dir, file), os.path.join(f"{directory}+{sub_dir}+{file}"))


def move_back():
    for file in os.listdir():
        if file.endswith("input.txt"):
            file_name = file.split("+")
            os.rename(file, os.path.join(file_name[0], file_name[1], file_name[2]))
def main():
    move_back()

if __name__ == "__main__":
    main()
