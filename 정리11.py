with open("input.txt", "r", encoding="utf-8") as file:
    lines = [line.strip().split("\t") for line in file]

# 배열 안에 있는 문자열 간격을 1칸 공백으로 변경
for i in range(len(lines)):
    lines[i] = [' '.join(x.split()) for x in lines[i]]

print(lines)

for i, line in enumerate(lines):

    if line[0]:
        column_count = len(line) + len(lines[i + 1]) + 1
        print (column_count)
        break



processed_lines = [[""] * column_count]

print (processed_lines)
i = 0

while i < len(lines):
    line = lines[i]

    if line[0]:
        next_line = lines[i + 1] if i + 1 < len(lines) else []
        next_next_line = lines[i + 2] if i + 2 < len(lines) else []

        processed_line = line + next_line + [next_next_line[0]] if next_next_line else line + next_line
        while len(processed_line) < column_count:
            processed_line.insert(0, "##")

        processed_lines.append(processed_line)
        i += 3
    else:
        next_line = lines[i + 1] if i + 1 < len(lines) else []
        next_next_line = lines[i + 2] if i + 2 < len(lines) else []

        processed_line = ["##"] + line[1:] + next_line + [next_next_line[0]] if next_next_line else ["##"] + line[1:] + next_line
        while len(processed_line) < column_count:
            processed_line.insert(0, "##")

        processed_lines[-1] = processed_line
        i += 3

output_lines = []
for line in processed_lines:
    output_lines.append("\t".join(line))

with open("output.txt", "w", encoding="utf-8") as output_file:
    for line in output_lines:
        output_file.write(line + "\n")

print("The sorted output has been saved in the output.txt file.")
