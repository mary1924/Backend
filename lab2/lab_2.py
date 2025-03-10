with open("input_2.txt", "r") as file:
    reports = [list(map(int, line.split())) for line in file]

def is_safe(report):
    inc = True
    dec = True
    for i in range(len(report) - 1):
        if report[i] >= report[i + 1]:
            inc = False
        if report[i] <= report[i + 1]:
            dec = False
        if abs(report[i] - report[i + 1]) < 1 or abs(report[i] - report[i + 1]) > 3:
            return False
    return inc or dec

safe_count = sum(is_safe(report) for report in reports)
print("Кількість безпечних звітів:", safe_count)
