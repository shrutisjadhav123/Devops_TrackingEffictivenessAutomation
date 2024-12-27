from .logger import log_info
from .database import Database

class MetricsTracker:
    def __init__(self):
        self.db = Database()

    def log_lead_time(self, start_time, end_time):
        lead_time = (end_time - start_time).total_seconds() / 60  # Convert to minutes
        log_info(f'Lead Time: {lead_time:.2f} minutes')
        return lead_time

    def log_change_failure(self, successful_changes, total_changes):
        if total_changes > 0:
            change_failure_rate = (total_changes - successful_changes) / total_changes * 100
            log_info(f'Change Failure Rate: {change_failure_rate:.2f}%')
            return change_failure_rate