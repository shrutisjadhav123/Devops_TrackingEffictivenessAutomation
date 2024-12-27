from datetime import datetime, timedelta
from src.metrics import MetricsTracker
from src.logger import setup_logging

def main():
    setup_logging()
    tracker = MetricsTracker()

    # Simulate logging metrics
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=5)  # Simulate a 5-minute lead time
    lead_time = tracker.log_lead_time(start_time, end_time)

    # Simulate successful changes
    successful_changes = 8
    total_changes = 10
    change_failure_rate = tracker.log_change_failure(successful_changes, total_changes)

    # Log a deployment
    deployment_frequency = 1
    tracker.db.insert_metrics(lead_time, change_failure_rate, deployment_frequency, mttr=15)

    print("Metrics logged successfully.")

    # Close the database connection
    tracker.db.close()

if __name__ == "__main__":
    main()