from typing import List

file_path = "input/09.txt"

with open(file_path, 'r') as file:    
    disk_map = file.read().strip()


def calculate_checksum(input: str) -> int:
    total = 0
    for index, character in enumerate(list(input)):
        total += index * int(character)
    return total


def create_id_list(disk_map: str) -> List[str]:
    file_spaces_list = []
    current_id : int = 0
    for index, character in enumerate(disk_map):
        if index % 2 == 0:
            file_spaces_list.append(str(current_id) * int(character))
            current_id += 1
        else:
            file_spaces_list.append("." * int(character))
    return file_spaces_list


def part_one() -> int:
    file_spaces_list = create_id_list(disk_map)
    id_list = list("".join(file_spaces_list))
    result = []
    for char in id_list:
        if char == ".":
            # Keep on popping elements until you find something that is not an '.' and add to new
            while id_list and (popped := id_list.pop()) == ".":
                pass
            if popped != ".":
                result.append(popped)
        else:
            result.append(char)

    return calculate_checksum("".join(result))


def part_two() -> int:
    id_list = create_id_list(disk_map)
    # print(id_list)
    return 


# blocks = []
# id = 0
# for i, ch in enumerate(disk_map):
#     n = int(ch)
#     if i % 2:
#         blocks += n * [-1]
#     else:
#         blocks += n * [id]
#         id += 1

# l, r = 0, len(blocks) - 1
# checksum1 = 0
# while l <= r:
#     if blocks[l] > -1:
#         checksum1 += l * blocks[l]
#         l += 1
#     elif blocks[r] > -1:
#         checksum1 += l * blocks[r]
#         l += 1
#         r -= 1
#     else:
#         r -= 1

# r = len(blocks) - 1
# while r > 0:
#     l = 0
#     if blocks[r] > -1:
#         size, id = 0, blocks[r]
#         while blocks[r] == id:
#             size += 1
#             r -= 1
#         free = 0
#         while l <= r:
#             free = free + 1 if blocks[l] == -1 else 0
#             if free >= size:
#                 blocks[l - free + 1:l - free + size + 1] = blocks[r + 1:r + size + 1]
#                 blocks[r + 1:r + size + 1] = size * [-1]
#                 break
#             l += 1
#     else:
#         r -= 1 

# checksum2 = sum(i * id if id > -1 else 0 for i, id in enumerate(blocks))

# print(checksum1)
# print(checksum2)

if __name__ == "__main__":
    print(f"Part One: {part_one()}") # 6401092019345
    print(f"Part Two: {part_two()}") 