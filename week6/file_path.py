import os

def cwd():
    path = os.getcwd()
    print(f"Current working directory is: {path}")
    print("The directory contains the following files:")
    for files in os.listdir(path):
        print(files)

def run():
    print("Processing....")
    cwd()

if __name__ == "__main__":
    run()