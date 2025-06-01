from notifypy import Notify
import time

def drink_water_reminder(interval_minutes=60):
    notification = Notify()
    notification.title = "Hydration Reminder"

    while True:
        notification.message = "Time to drink water! 💧 Stay hydrated."
        notification.send()
        print("Reminder sent. Next reminder in", interval_minutes, "minutes.")
        time.sleep(interval_minutes * 60)  # Wait for the given interval

# Start the reminder (default: every 60 minutes)
drink_water_reminder(60)
