from typing import List

file_path = "input/02.txt"

with open(file_path, 'r') as file:    
    lines = [line.strip() for line in file]


def is_safe(report : List[str]) -> bool: 
    increasing, decreasing = False, False
    
    for i in range(len(report)-1):
        difference = int(report[i]) - int(report[i+1])

        if abs(difference) > 3:
            return False
        if difference == 0:
            return False
        if difference < 0:
            decreasing = True        
        if difference > 0:
            increasing = True
        
    return increasing ^ decreasing


def part_one() -> int:
    safe_reports = 0
    for report in lines:
        if is_safe(report.split()):
            safe_reports += 1
    return safe_reports


def part_two() -> int:
    safe_reports = 0
    for line in lines:
        report = line.split(" ")

        if is_safe(report):
            safe_reports += 1
            continue

        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if is_safe(modified_report):
                safe_reports += 1
                break

    return safe_reports


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")