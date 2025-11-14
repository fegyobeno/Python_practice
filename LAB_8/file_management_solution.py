import os
import sys

class FileManager:
    def __init__(self, directory, relative = False):
        if relative:
            self.directory = os.path.join(os.getcwd(), directory)
        else:
            self.directory = directory
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
    
    def change_directory(self, new_directory):
        self.directory = new_directory
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)        
    
    def list_files(self):
        return os.listdir(self.directory)
    
    def read_file(self, filename):
        filepath = os.path.join(self.directory, filename)
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"{filename} does not exist in {self.directory}")
        with open(filepath, 'r') as file:
            return file.read()
        
    def edit_file(self, filename, content):
        filepath = os.path.join(self.directory, filename)
        with open(filepath, 'w') as file:
            file.write(content)
    
    def delete_file(self, filename):
        filepath = os.path.join(self.directory, filename)
        if os.path.isfile(filepath):
            os.remove(filepath)
        else:
            raise FileNotFoundError(f"{filename} does not exist in {self.directory}")
        
def main():
    directory = sys.argv[1]
    
    file_manager = FileManager(directory)
    
    while True:
        try:
            command = input("Enter command (list, read <filename>, change <new_directory>, edit <filename>, \ndelete <filename>, exit (ctrl + c)): ")
            parts = command.split()
            if parts[0] == "list":
                files = file_manager.list_files()
                print("Files:", files)
            if parts[0] == "read" and len(parts) == 2:
                content = file_manager.read_file(parts[1])
                print("Content of", parts[1], ":\n", content)
            if parts[0] == "change" and len(parts) == 2:
                file_manager.change_directory(parts[1])
                print("Changed directory to", parts[1])
            if parts[0] == "delete" and len(parts) == 2:
                file_manager.delete_file(parts[1])
                print("Deleted file", parts[1])
            if parts[0] == "edit" and len(parts) == 2:
                print("Enter content, end with ctrl + d (Linux/Mac) or ctrl + z (Windows):")
                content_lines = []
                while True:
                    try:
                        line = input()
                    except EOFError:
                        print("\nEnd of input detected.")
                        break
                    content_lines.append(line)
                content = "\n".join(content_lines)
                file_manager.edit_file(parts[1], content)
        except KeyboardInterrupt:
            print("\nExiting.")
            break
if __name__ == "__main__":
    main()
    