from directory_calculator import *

directory_path = os.getcwd()

directory = Directory(directory_path)
total_size = directory.calculate()
bytes_size, kb_size, mb_size, gb_size = Size.sizes(total_size)