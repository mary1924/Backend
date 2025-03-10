with open("input_3.txt", "r") as file:
    commands = file.readlines()

class Directory:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.subdirectories = []
        self.files = []

def parse_filesystem(commands):
    root = Directory("/")
    current_dir = root
    dir_stack = [root]
    
    for command in commands:
        parts = command.strip().split()
        if parts[0] == '$':
            cmd = parts[1]
            if cmd == 'cd':
                if parts[2] == '/':
                    current_dir = root
                    dir_stack = [root]
                elif parts[2] == '..':
                    dir_stack.pop()
                    current_dir = dir_stack[-1]
                else:
                    new_dir = Directory(parts[2])
                    current_dir.subdirectories.append(new_dir)
                    dir_stack.append(new_dir)
                    current_dir = new_dir
            elif cmd == 'ls':
                continue
        elif parts[0] == 'dir':
            new_dir = Directory(parts[1])
            current_dir.subdirectories.append(new_dir)
        else:
            file_size = int(parts[0])
            current_dir.size += file_size
            current_dir.files.append((parts[1], file_size))
    
    return root

def calculate_total_sizes(directory):
    total_size = directory.size
    for subdir in directory.subdirectories:
        total_size += calculate_total_sizes(subdir)
    return total_size

def find_directories_with_max_size(root, max_size):
    result = []
    for subdir in root.subdirectories:
        size = calculate_total_sizes(subdir)
        if size <= max_size:
            result.append(size)
        result.extend(find_directories_with_max_size(subdir, max_size))
    return result

root = parse_filesystem(commands)
directories_with_max_size = find_directories_with_max_size(root, 100000)
sum_of_sizes = sum(directories_with_max_size)

print("Sum of the total sizes of directories with at most 100000 size:", sum_of_sizes)
