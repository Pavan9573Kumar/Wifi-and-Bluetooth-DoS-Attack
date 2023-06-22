import os
import subprocess
import sys

def list_files():
    files = os.listdir()
    py_files = [file for file in files if file.endswith(".py")]
    return py_files

def run_file(filename):
    try:
        subprocess.run(["sudo", "python3", filename])
        #exec(compile(open(filename, "rb").read(), filename, 'exec'))
    except Exception as e:
        print(f"An error occurred while running the file: {e}")

def main():
    files = list_files()
    if not files:
        print("No Python files found in the current directory.")
        return

    print("Available files:")
    for index, file in enumerate(files, start = 0):
        if(file=="tool.py"):
            continue
        print(f"{index}. {file}")

    file_mapping = {index: file for index, file in enumerate(files, start=0)}

    while True:
        try:
            choice = int(input("Enter the number of the file you want to run (or 0 to exit): "))
            if choice == 0:
                print("Exiting the tool.")
                return
            elif choice in file_mapping:
                selected_file = file_mapping[choice]
                run_file(selected_file)
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
