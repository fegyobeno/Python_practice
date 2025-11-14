import os
import sys

class FileManager:
    def __init__(self, directory, relative = False):
        #TODO: Implement the constructor to initialize the FileManager with the given directory.
        # If the file does not exist, create it.
        pass
    
    def change_directory(self, new_directory):
        #TODO: Change the current working directory to new_directory.
        pass       
    
    def list_files(self):
        #TODO: Return a list of files in the current directory.
        pass
    
    def read_file(self, filename):
        #TODO: Read and return the content of the specified file.
        pass
        
    def edit_file(self, filename, content):
        #TODO: Edit the specified file with the given content.
        pass
    
    def delete_file(self, filename):
        #TODO: Delete the specified file from the current directory it it exists.
        pass
    
def main():
    if sys.argv.__len__() < 2:
        directory = "./"
    else:
        directory = sys.argv[1]
    
    file_manager = FileManager(directory)
    
    while True:
        try:
            # TODO: Implement a command-line interface to interact with the FileManager.
            continue
        except KeyboardInterrupt:
            print("\nExiting.")
            break
if __name__ == "__main__":
    main()
    