import csv

def sort_data(data):
    # Sort the data by node name.
    sorted_data = sorted(data, key=lambda row: row[0])

    # Format the data.
    for row in sorted_data:
        row = [str(item) for item in row]
        print("".join(row))

if __name__ == "__main__":
    with open("input.txt", "r" , encoding="utf-8") as txtfile:
        reader = csv.reader(txtfile, delimiter="\t")
        data = list(reader)

    # 결과 출력
    for line in data:
        print(line)
