# Перевірка безпеки звітів
def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = 0
    for i in range(len(left_list)):
        distance = abs(left_list[i] - right_list[i])
        total_distance += distance
    return total_distance

# Відкриття файлу та зчитування даних
with open("input_1.txt", "r") as file:
    lines = file.readlines()

# Формування списків
left_list = list(map(int, lines[0].split()))
right_list = list(map(int, lines[1].split()))

# Обчислення загальної відстані
total_distance = calculate_total_distance(left_list, right_list)

print("Left list:", left_list)
print("Right list:", right_list)
print("Total distances:", total_distance)
