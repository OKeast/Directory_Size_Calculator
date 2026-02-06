import os

class File:
    def __init__(self, path):
        self.path = path

class Directory(File):
    def calculate(self):
        
        total_size = 0
        for item in os.listdir(self.path): # lsitdir finds all files and subdirectories in specific directory
            item_path = os.path.join(self.path, item) 
            # join will combine the directory path and the file/folder into a new valid directory path
            
            if os.path.isfile(item_path): # if the next item is a file
                total_size += os.path.getsize(item_path) # gets the size for each file and adds it to total_size
                print("file")
                
            elif os.path.isdir(item_path):
                total_size += Directory(item_path).calculate() # gets the size for any subdirectories and adds it to total_size
                print("folder")

        return total_size # total

class Size:

    def sizes(total_size):
        
        bytes_size = total_size
        kb_size = total_size / 1024 # 1024 bytes in a KB
        mb_size = kb_size / 1024
        gb_size = mb_size / 1024 

        print(f"Total size:")
        print(f"  {bytes_size} bytes")
        print(f"  {kb_size:.2f} KB")
        print(f"  {mb_size:.2f} MB")
        print(f"  {gb_size:.2f} GB")

        return bytes_size, kb_size, mb_size, gb_size