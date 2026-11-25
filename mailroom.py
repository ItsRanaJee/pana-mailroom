import sys


def read_rows(path):
    file = open(path, encoding="utf-8")
    text = file.read()
    file.close()
    lines = text.splitlines()
    rows = []
    for line in lines[1:]:
        if line.strip() != "":
            rows.append(line.split(","))
    return rows


def count_subscribers(path):
    return len(read_rows(path))


def count_by_group(path):
    counts = {}
    for row in read_rows(path):
        group = row[3]
        if group in counts:
            counts[group] = counts[group] + 1
        else:
            counts[group] = 1
    return counts


if len(sys.argv) > 1 and sys.argv[1] == "subscribers":
    path = "data/subscribers.csv"
    print("Total:", count_subscribers(path))
    groups = count_by_group(path)
    for group in groups:
        print(group + ":", groups[group])
