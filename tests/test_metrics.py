import unittest
from datetime import datetime, timedelta
from src.metrics import MetricsTracker

class TestMetricsTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = MetricsTracker()

    def test_log_lead_time(self):
        start_time = datetime.now()
        end_time = start_time + timedelta(minutes=5)  # Simulate a 5-minute lead time
        lead_time = self.tracker.log_lead_time(start_time, end_time)
        self.assertAlmostEqual(lead_time, 5.0, places=1)

    def test_log_change_failure(self):
        successful_changes = 8
        total_changes = 10
        change_failure_rate = self.tracker.log_change_failure(successful_changes, total_changes)
        self.assertAlmostEqual(change_failure_rate, 20.0, places=1)

    def test_log_change_failure_no_changes(self):
        successful_changes = 0
        total_changes = 0
        change_failure_rate = self.tracker.log_change_failure(successful_changes, total_changes)
        self.assertIsNone(change_failure_rate)

if __name__ == '__main__':
    unittest.main()