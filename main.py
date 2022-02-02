# ! /usr/bin/env python3
import argparse
import os
import random
import shutil
import string

workdir: str


def read_file():
    filename = input("Enter file name : ")
    print(f"read file : {filename}")
    # TODO read file and print result
    with open(filename, 'r') as data:
        print(data.read())


def create_file():
    while True:
        filename = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        if not os.path.isfile(filename+'.txt'):
            break
    print(f"create_file : {filename}.txt")
    # TODO write content to file
    with open(filename, 'w') as data:
        data.write('Training_007')


def delete_file():
    filename = input("Enter file name : ")
    print(f"delete file : {filename}")
    # TODO delete file
    os.remove(filename)


def list_dir():
    print(f"list dir")
    print(os.listdir())
    # Print content of current working directory


def change_dir():
    while True:
        directory = input("Enter dir name : ")
        if os.path.isdir(directory):
            break
        else:
            print('dir not exist')
    print(f"change dir : {directory}")
    # Change current working directory
    old_path = workdir
    shutil.move(old_path, directory)


def main():
    # Create argument parser that will retrieve working directory
    commands = {
        "get": read_file,
        "create": create_file,
        "delete": delete_file,
        "ls": list_dir,
        "cd": change_dir
    }
    while True:
        command = input("Enter command: ")
        if command == "exit":
            return
        if command not in commands:
            print("Unknown command")
            continue
        command = commands[command]
        try:
            command()
        except Exception as ex:
            print(f"Error on {command} execution : {ex}")


def pars():
    my_pars = argparse.ArgumentParser()
    my_pars.add_argument('-w', '--workdir', default=os.getcwd())
    namespace = my_pars.parse_args()
    global workdir
    workdir = namespace.workdir
    print(namespace.workdir)


if __name__ == "__main__":
    pars()
    main()
