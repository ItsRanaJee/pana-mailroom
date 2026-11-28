from datetime import date

from mailroom import count_subscribers, count_by_group, count_joined_since, next_send

assert count_subscribers("data/subscribers.csv") == 24
assert count_by_group("data/subscribers.csv")["learners"] == 8
assert count_by_group("data/subscribers.csv")["builders"] == 8
assert count_by_group("data/subscribers.csv")["leaders"] == 8

# Joined in the last 30 days, run date 2026-11-20: Noah, Yuki, Sara = 3.
assert count_joined_since("data/subscribers.csv", date(2026, 11, 20), 30) == 3

# Next send is the first Monday of the next month.
assert next_send(date(2026, 11, 20)) == date(2026, 12, 7)
assert next_send(date(2026, 12, 7)) == date(2027, 1, 4)

print("All checks passed")
