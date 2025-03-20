import datetime
class Logger:
    def log(self, message):
        timestamp = datetime.datetime.now().isoformat()
        print(f"[{timestamp}] {message}")
