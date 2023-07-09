with open("input_file.txt", "r") as f:
    lines = f.readlines()

# Remove unnecessary separator line
lines.pop(1)

# Iterate through lines and modify formatting
formatted_lines = []
for line in lines:
    if line.startswith("NODE"):
        node = line.strip()
    else:
        parts = line.strip().split()
        formatted_line = "{}   {}".format(node, "  ".join(parts))
        formatted_lines.append(formatted_line)

# Print the formatted data
print("      NODE   OPER                aaaaaaa     ddddddd    tttttttt   kkkkkkkkk      rereee    gggggggg  llllllllll     eeeeeee     cccccc   nnnnnnnnn  RES_TIME     C_RATIO   HIT_RATIO")
print("      " + "\n      ".join(formatted_lines))
