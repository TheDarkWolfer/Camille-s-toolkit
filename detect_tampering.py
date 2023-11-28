import os
import datetime

def check_metadata_tampering():
    max_days_without_tampering = 7

    # Check if file was modified in the last max_days_without_tampering days
    last_modified_timestamp = os.path.getmtime(__file__)
    current_timestamp = datetime.datetime.now().timestamp()
    days_since_last_modified = (current_timestamp - last_modified_timestamp) / (24 * 3600)

    if days_since_last_modified > max_days_without_tampering:
        print("Metadata tampering detected.")

if __name__ == "__main__":
    check_metadata_tampering()
    print("Script execution continues...")