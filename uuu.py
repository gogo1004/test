
import sys
import io

with io.open("SMF.txt", "r", encoding="utf-8") as f:
  data = f.read().splitlines()


data = '\n'.join(data)  # 리스트를 개행 문자로 연결하여 하나의 문자열로 변환
print (data)


# Split the lines into a list and remove unnecessary lines
lines = data.splitlines()[4:-1]

# Parse the header
header = lines[0]

# Initialize the result variable
result = []

# Initialize current_node and current_oper variables
current_node = ''
current_oper = ''

# Iterate through the lines with data
for i in range(1, len(lines)):
    row = lines[i].split()

    # If the line starts with 'DBC', add the 'NODE' and 'OPER' columns
    if 'DBC' in row[0]:
        result.append(' '.join(row[:7]))
        current_node = row[0]
        current_oper = row[1]

    # Otherwise, add the 'null' 'NODE', and current 'OPER' columns
    else:
        result.append('null ' + current_oper + ' ' + ' '.join(row))

# Combine the result into a single string
output = header + '\n' + '\n'.join(result)

# Print the formatted output
print(output)
