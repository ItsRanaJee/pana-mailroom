from mailroom import count_subscribers, count_by_group

assert count_subscribers("data/subscribers.csv") == 24
assert count_by_group("data/subscribers.csv")["learners"] == 8
assert count_by_group("data/subscribers.csv")["builders"] == 8
assert count_by_group("data/subscribers.csv")["leaders"] == 8

print("All checks passed")
