file_path = "input/13-test.txt"

with open(file_path, 'r') as file:
    lines = [line.strip() for line in file if line.strip()]  # Remove empty lines

def part_one():
    for i in range(0, len(lines), 3):
        button_a = lines[i]
        button_b = lines[i+1]
        prize = lines[i+2]
        
        button_a = parse_coordinates(button_a)
        button_b = parse_coordinates(button_b)
        prize = parse_coordinates(prize)
        
        a = button_a["X"]
        b = button_a["Y"]
        c = button_b["X"]
        d = button_b["Y"]
        e = prize["X"]
        f = prize["Y"]

        b_value = (((f * a) - e) / ((d * a)-c))
        print(b_value)
        a_value = (f-((d * f * a) - (d * e)/(d * d * a)-c))/ b**2
        print(a_value)

def parse_coordinates(line):
    """Extract coordinates from a line."""
    if "Button" in line or "Prize" in line:
        x, y = line.split(":")[1].split(",")
        return {
            "X": int(x.split("+")[-1] if "+" in x else x.split("=")[-1]),
            "Y": int(y.split("+")[-1] if "+" in y else y.split("=")[-1]),
        }
    return None

part_one()


def part_two() -> int:
    return 

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")