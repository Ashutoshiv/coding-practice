"""Simple console alarm clock for Windows."""

from datetime import datetime, timedelta
import time
import winsound


def parse_alarm_time(value: str) -> datetime:
	"""Parse a 24-hour HH:MM time for today or the next day."""
	now = datetime.now()
	alarm_time = datetime.strptime(value, "%H:%M").replace(
		year=now.year,
		month=now.month,
		day=now.day,
	)
	if alarm_time <= now:
		alarm_time += timedelta(days=1)
	return alarm_time


def ring_alarm() -> None:
	"""Play a short repeating alarm until the user stops it."""
	print("Alarm ringing. Press Ctrl+C to stop.")
	try:
		while True:
			winsound.Beep(1000, 800)
			time.sleep(0.2)
	except KeyboardInterrupt:
		print("Alarm stopped.")


def main() -> None:
	alarm_input = input("Enter alarm time in HH:MM (24-hour format): ").strip()
	alarm_time = parse_alarm_time(alarm_input)
	print(f"Alarm set for {alarm_time.strftime('%Y-%m-%d %H:%M')}")

	while True:
		now = datetime.now()
		if now >= alarm_time:
			ring_alarm()
			break
		remaining = alarm_time - now
		print(f"Time remaining: {remaining}", end="\r")
		time.sleep(1)


if __name__ == "__main__":
	main()

