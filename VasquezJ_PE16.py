#script that processes a log file and extracts relevant information.

import re

log_file_path = r"C:\Users\datam\OneDrive\Desktop\server_log.txt" # file created on my computer to test script

all_users = []
denied_users = []
denied_attempts_count = 0

# [2025-02-23 14:35:21] User: alice123 - ACCESS DENIED example log for my reference
log_pattern = r'User: (\w+) - (ACCESS DENIED|ACCESS GRANTED)$'

try:
    with open(log_file_path, 'r') as log_file:
        for lines in log_file:
            clean_line = lines.strip()
            if not clean_line:
                continue
            match = re.search(log_pattern, clean_line)

            if match:
                username = match.group(1)
                access_status = match.group(2)
                all_users.append(username)

                if access_status == "ACCESS DENIED":
                    denied_users.append(username)
                    denied_attempts_count += 1
except Exception as e:
    print(f'\n You\'ve encountered an unexpected error: {e}')

print("\n--Log File Results-- ")
print(f"All Users: {all_users}")
print(f"Denied Access: {denied_users}")
print(f"Total Denied Attempts: {denied_attempts_count}")



