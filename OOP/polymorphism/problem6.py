class Alert:
    def send_alert(self, msg):
        pass

class EmailAlert(Alert):
    def send_alert(self, msg):
        print("Email:", msg)

class SMSAlert(Alert):
    def send_alert(self, msg):
        print("SMS:", msg)

class AppAlert(Alert):
    def send_alert(self, msg):
        print("App Notification:", msg)

alerts = [EmailAlert(), SMSAlert(), AppAlert()]

for a in alerts:
    a.send_alert("Warning!")
