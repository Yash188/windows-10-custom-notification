


# importing required modules
from win10toast import ToastNotifier
import time

# initializing toastnotifier
custom_notification = ToastNotifier()

# showing windows 10 notification
custom_notification.show_toast("Custom Notification","This is a message body",threaded=True,
                   icon_path=None,duration=4)

# check if any notification is active
while custom_notification.notification_active():
    time.sleep(0.1)
