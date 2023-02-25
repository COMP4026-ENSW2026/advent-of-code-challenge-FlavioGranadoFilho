with open("sample.in") as f:
    contents = f.read()
    lines = contents.split("\n")

instructions = [[line.split()[0], int(line.split()[1])] for line in lines
                if line]

unique_tail_positons = set()

rope_points = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
               [0, 0], [0, 0]]

for instruction in instructions:
    direction, length = instruction[0], instruction[1]
    for i in range(length):
        current_position_head = rope_points[0]
        if direction == "R":
            current_position_head[0] += 1
        elif direction == "L":
            current_position_head[0] -= 1
        elif direction == "U":
            current_position_head[1] += 1
        elif direction == "D":
            current_position_head[1] -= 1

        for i in range(len(rope_points) - 1):
            current_position_head = rope_points[i]
            current_position_tail = rope_points[i + 1]
            if i == 8:
                unique_tail_positons.add(tuple(current_position_tail))

            if current_position_head[0] == current_position_tail[
                    0] and current_position_head[1] == current_position_tail:
                current_position_tail = list(current_position_head)

            elif abs(current_position_head[0] -
                     current_position_tail[0]) <= 1 and abs(
                    current_position_head[1] - current_position_tail[1]) <= 1:
                pass

            elif current_position_head[0] == current_position_tail[0]:
                if current_position_head[1] > current_position_tail[1]:
                    current_position_tail[1] += 1
                elif current_position_head[1] < current_position_tail[1]:
                    current_position_tail[1] -= 1
            elif current_position_head[1] == current_position_tail[1]:
                if current_position_head[0] > current_position_tail[0]:
                    current_position_tail[0] += 1
                elif current_position_head[0] < current_position_tail[0]:
                    current_position_tail[0] -= 1

            else:
                if current_position_head[0] > current_position_tail[0]:
                    current_position_tail[0] += 1
                elif current_position_head[0] < current_position_tail[0]:
                    current_position_tail[0] -= 1
                if current_position_head[1] > current_position_tail[1]:
                    current_position_tail[1] += 1
                elif current_position_head[1] < current_position_tail[1]:
                    current_position_tail[1] -= 1

unique_tail_positons.add(tuple(current_position_tail))
num_unique_tail_positions = len(unique_tail_positons)
print(num_unique_tail_positions)
