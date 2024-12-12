from collections import deque

file_path = "input/09-test.txt"

with open(file_path, "r") as file:
    disc_map = [int(num) for num in file.read()]

print("input:",disc_map)

def create_disc(disc_map):
    disc = []
    current_block_id = 0
    for i, block in enumerate(disc_map):
        if i % 2 == 1:
            disc += block * [-1]
        else:
            disc += block * [current_block_id]
            current_block_id += 1
    return disc


def calculate_checksum(disc):
    return sum(index * number for index, number in enumerate(disc) if number > -1)


def find_fragments(disc):
    occupied, empty = [], []
    start = 0
    for i in range(1, len(disc)):
        if disc[i] != disc[start]:
            if disc[start] == -1:
                empty.append([start, i - 1])
            else:
                occupied.append([start, i - 1])
            start = i
    if disc[start] != -1:
        occupied.append([start, len(disc) - 1])
    return occupied, empty


def defragment(disc):
    defragmented = disc.copy()
    occupied, empty = find_fragments(disc)
    for start, end in occupied[::-1]:
        block_size = end - start + 1
        for empty_block in empty:
            empty_start, empty_end = empty_block
            if empty_start > start:
                break
            if empty_end - empty_start + 1 >= block_size:
                defragmented[empty_start : empty_start + block_size] = disc[
                    start : start + block_size
                ]
                defragmented[start : start + block_size] = [-1] * block_size
                empty_block[0] += block_size
                if empty_block[0] > empty_block[1]:
                    empty.remove(empty_block)
                break
    return defragmented

disc = create_disc(disc_map)

def part_one() -> int:
    updated_disc = disc.copy()
    print("disk", disc)
    free_space = deque([i for i, num in enumerate(disc) if num == -1])
    print(free_space)
    for i in range(len(disc) - 1, -1, -1):
        if disc[i] != -1 and free_space and free_space[0] < i:
            index_to_move = free_space.popleft()
            updated_disc[index_to_move], updated_disc[i] = updated_disc[i], -1
    print(updated_disc)
    return calculate_checksum(updated_disc)


def part_two() -> int:    
    defragmented = defragment(disc)
    return calculate_checksum(defragmented)


if __name__ == "__main__":
    print(f"Part One: {part_one()}") # 1928
    print(f"Part Two: {part_two()}") # 2858