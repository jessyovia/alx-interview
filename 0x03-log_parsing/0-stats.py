#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """Handles the interrupt signal (CTRL + C)"""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Regular expression to match log line format
log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)')

# Read from stdin
for line in sys.stdin:
    match = log_pattern.match(line)
    if match:
        status_code = int(match.group("status"))
        file_size = int(match.group("size"))
        
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        
        line_count += 1

        if line_count % 10 == 0:
            print_stats()

# Print final stats if the loop ends without an interrupt
print_stats()
