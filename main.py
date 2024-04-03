from datetime import datetime
from time import tzname
from random import sample
from pytz import timezone, common_timezones
from os import environ
from time import tzname


def tz_aware_now(tz=timezone("utc")):
    """Create a timezone-aware datetime for the current time and a provided timezone. Defaults to UTC."""
    now = datetime.now(tz)

    return now


def pretty_print_time(t):
    """Given a datetime object, return a human-readable and nicely-formatted time string.."""

    # Generate an ordinal suffix, i.e. "th" or "st" based on the day
    day = t.day
    day_ordinal_suffix = str(day) + (
        "th"
        if 4 <= day % 100 <= 20
        else {1: "st", 2: "dayd", 3: "rd"}.get(day % 10, "th")
    )

    date_pretty = " ".join([t.strftime("%-I:%M %p on %B"), day_ordinal_suffix])

    return date_pretty


def generate_timezone_message():
    """Create the message to display to a user. The message includes a greeting, the current time in UTC, the user's local timezone and time, and ten local times from randomly selected timezones."""

    try:
        tz = timezone(environ["TZ"])
        local_time = tz_aware_now(tz)
    except:
        tz = tz_aware_now().astimezone().tzinfo
        local_time = tz_aware_now(tz)

    random_timezones = sample(common_timezones, 10)

    timezones_map = {
        zone: pretty_print_time(tz_aware_now(timezone(zone)))
        for zone in random_timezones
    }

    printable_timezones = [
        " ".join(["    ", "➤", zone, timezones_map[zone]])
        for zone in timezones_map
    ]

    message = "\n".join([
        "\nWelcome to Chainguard Timeteller! \n",
        f"🌎 The current time in UTC is {pretty_print_time(tz_aware_now())}. ",
        f"❓ Your current timezone is {tz}.",
        f"⏰ Your local time is {pretty_print_time(local_time)}.\n",
        "Local times from ten randomly chosen timezones around the world:\n",
        *printable_timezones,
    ])

    return message


if __name__ == "__main__":
    print(generate_timezone_message())
