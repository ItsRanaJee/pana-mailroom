from datetime import date

from mailroom import count_subscribers, count_by_group, count_joined_since, next_send

SUBSCRIBERS = "data/subscribers.csv"


def test_counts_24_subscribers_in_total():
    assert count_subscribers(SUBSCRIBERS) == 24


def test_learners_group_has_8_subscribers():
    assert count_by_group(SUBSCRIBERS)["learners"] == 8


def test_builders_group_has_8_subscribers():
    assert count_by_group(SUBSCRIBERS)["builders"] == 8


def test_leaders_group_has_8_subscribers():
    assert count_by_group(SUBSCRIBERS)["leaders"] == 8


def test_three_joined_in_the_30_days_to_20_november_2026():
    # Noah, Yuki and Sara.
    assert count_joined_since(SUBSCRIBERS, date(2026, 11, 20), 30) == 3


def test_next_send_after_20_november_2026_is_7_december():
    assert next_send(date(2026, 11, 20)) == date(2026, 12, 7)


def test_next_send_after_a_first_monday_is_the_next_months_first_monday():
    assert next_send(date(2026, 12, 7)) == date(2027, 1, 4)
