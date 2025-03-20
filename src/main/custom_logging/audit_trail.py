import datetime
import os
class AuditTrail:
    def __init__(self, log_file="audit_trail.log"):
        self.log_file = log_file
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                f.write("Audit Trail Log\n")
    
    def record(self, message):
        timestamp = datetime.datetime.now().isoformat()
        entry = f"[{timestamp}] {message}\n"
        with open(self.log_file, "a") as f:
            f.write(entry)
