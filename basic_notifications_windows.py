from plyer import notification

title = "Notification Title"
message = "This is the notification message."

notification.notify(
    title=title,
    message=message,
    app_name="YourAppName",
    timeout=10  # Optional: Notification timeout in seconds
)
