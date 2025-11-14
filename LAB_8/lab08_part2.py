import os
import sys
import time

# decide the os
if os.name == 'nt':
    print("Windows OS detected.")
    CLEAR_COMMAND = 'cls'
else:
    print("Unix-like OS detected.")
    CLEAR_COMMAND = 'clear'
    
# Function to clear the console
def clear_console():
    os.system(CLEAR_COMMAND)
    
# print("Clearing the console in 3 seconds...")
# time.sleep(3)
# clear_console()

# Check the current working directory
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")

# Change the current working directory
new_directory = os.path.join(current_directory, 'LAB_8')
try:
    os.chdir(new_directory)
    print(f"Changed Working Directory to: {new_directory}")
except Exception as e:
    print(f"Error changing directory: {e}")
    
def change_dir(new_dir):
    try:
        if os.path.isdir(new_dir):
            os.chdir(new_dir)
            print(f"Changed directory to: {new_dir}")
        else:
            print(f"The directory {new_dir} does not exist.")
            # create the dir
            os.makedirs(new_dir)
            print(f"Created directory: {new_dir}")
            os.chdir(new_dir)
            print(f"Changed directory to: {new_dir}")
    except Exception as e:
        print(f"Error changing directory: {e}")
        
change_dir('./test_dir')

# remove dir
def remove_dir(dir_path):
    # change path to absolute
    dir_path = os.path.abspath(dir_path)
    try:
        if os.path.isdir(dir_path):
            os.rmdir(dir_path)
            print(f"Removed directory: {dir_path}")
        else:
            print(f"The directory {dir_path} does not exist.")
    except Exception as e:
        print(f"Error removing directory: {e}")

# wont work as current working dir is noow within the test_dir        
#remove_dir('test_dir')

# only works if the dir is not open / being used
remove_dir('../test_dir')

# list files with given endings
change_dir('../')
print("Listing files in current directory:")
print(f"current dir: {os.getcwd()}")
print([x for x in os.listdir() if x.endswith('.py')])