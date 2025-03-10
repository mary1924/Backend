with open("input_3.txt", "r") as file:
    lines = file.readlines()

def get_calibration_value(line):
    first_digit = next(int(char) for char in line if char.isdigit())
    last_digit = next(int(char) for char in reversed(line) if char.isdigit())
    calibration_value = int(f"{first_digit}{last_digit}")
    return calibration_value

total_sum = sum(get_calibration_value(line.strip()) for line in lines)

print("sum of all:", total_sum)
