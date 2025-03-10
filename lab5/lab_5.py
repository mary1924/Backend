with open("input_5.txt", "r") as file:
    lines = file.readlines()
class Directory:    
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.subdirs = {}

def parse_filesystem(commands):
    root = Directory("/")
    current_dir = root
    dir_stack = [root]
    
    for command in commands:
        parts = command.strip().split()
        if not parts:
            continue
        if parts[0] == '$' and parts[1] == 'cd':
            if parts[2] == '/':
                current_dir = root
                dir_stack = [root]
            elif parts[2] == '..':
                dir_stack.pop()
                current_dir = dir_stack[-1]
            else:
                if parts[2] not in current_dir.subdirs:
                    new_dir = Directory(parts[2])
                    current_dir.subdirs[parts[2]] = new_dir
                current_dir = current_dir.subdirs[parts[2]]
                dir_stack.append(current_dir)
        elif parts[0].isdigit():
            current_dir.size += int(parts[0])
    return root

def calculate_total_sizes(directory):
    return directory.size + sum(calculate_total_sizes(subdir) for subdir in directory.subdirs.values())

def find_directories_with_max_size(directory, max_size):
    sizes = []
    for subdir in directory.subdirs.values():
        size = calculate_total_sizes(subdir)
        if size <= max_size:
            sizes.append(size)
        sizes.extend(find_directories_with_max_size(subdir, max_size))
    return sizes

root = parse_filesystem(lines)
directories_with_max_size = find_directories_with_max_size(root, 100000)
sum_of_sizes = sum(directories_with_max_size)

print("Сума загальних розмірів директорій, що не перевищують 100000:", sum_of_sizes)
