import sys
from datetime import date, timedelta


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


def count_joined_since(path, run_date, days):
    start = run_date - timedelta(days=days)
    count = 0
    for row in read_rows(path):
        joined_on = date.fromisoformat(row[4])
        if start <= joined_on <= run_date:
            count = count + 1
    return count


def next_send(run_date):
    if run_date.month == 12:
        first = date(run_date.year + 1, 1, 1)
    else:
        first = date(run_date.year, run_date.month + 1, 1)
    days_to_monday = (7 - first.weekday()) % 7
    return first + timedelta(days=days_to_monday)


# The command line is the only place that reads today's date.
def get_run_date(args):
    if "--run-date" in args:
        return date.fromisoformat(args[args.index("--run-date") + 1])
    return date.today()


if len(sys.argv) > 1 and sys.argv[1] == "subscribers":
    path = "data/subscribers.csv"
    if "--since-days" in sys.argv:
        days = int(sys.argv[sys.argv.index("--since-days") + 1])
        run_date = get_run_date(sys.argv)
        print("Joined in the last", days, "days:", count_joined_since(path, run_date, days))
    else:
        print("Total:", count_subscribers(path))
        groups = count_by_group(path)
        for group in groups:
            print(group + ":", groups[group])

if len(sys.argv) > 1 and sys.argv[1] == "next-send":
    print("Next send:", next_send(get_run_date(sys.argv)))
