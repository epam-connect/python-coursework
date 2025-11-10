#Create a custom context manager class for file handling?

class FileManager:
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.file_name, self.file_mode)
        print("File opened")
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        print("File closed")


with FileManager("abc.txt", "w") as file:
    file.write("Hello World!")
