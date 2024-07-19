#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_file_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
line_count = 0


def print_stats():
    """Prints the statistics"""
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


def signal_handler(sig, frame):
    """Handles the keyboard interruption signal"""
    print_stats()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = parts[-2]
            if status_code in status_counts:
                status_counts[status_code] += 1
            total_file_size += file_size
        except ValueError:
            continue

        # Increment the line count
        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
