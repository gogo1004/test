with open("input.txt", "r", encoding="utf-8") as file:
    data = [line.strip().split("\t") for line in file]

# 배열 안에 있는 문자열 간격을 1칸 공백으로 변경
for i in range(len(data)):
    data[i] = [' '.join(x.split()) for x in data[i]]

formatted_lines = []
i = 0

while i < len(data):
    line = data[i]

    if line[0]:
        formatted_lines.append(line)
        i += 1

        while i < len(data) and not data[i][0]:
            formatted_lines.append(["###"] + data[i][1:])
            i += 1
    else:
        i += 1

output_lines = []
header = formatted_lines.pop(0)
output_lines.append("\t".join(header))

for line in formatted_lines:
    output_lines.append("\t".join(line))

with open("output.txt", "w", encoding="utf-8") as output_file:
    for line in output_lines:
        output_file.write(line + "\n")

print("The sorted output has been saved in the output.txt file.")
