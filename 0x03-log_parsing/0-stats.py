import sys

# Initialize variables to store metrics
total_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

for line in sys.stdin:
    # Parse the line to extract relevant information
    parts = line.split(" ")
    try:
        # Check if the line matches the expected format
        if parts[0].startswith("<") and parts[2].startswith("[") and parts[4].startswith("\"GET"):
            status_code = int(parts[8])
            file_size = int(parts[9])
            # Update metrics
            total_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1
    except (ValueError, KeyError):
        # Skip lines that do not match the expected format or contain invalid status codes
        pass

    if line_count % 10 == 0:
        # Print metrics every 10 lines
        print("Total file size: ", total_size)
        for status_code in sorted(status_code_counts.keys()):
            if status_code_counts[status_code] > 0:
                print(f"{status_code}: {status_code_counts[status_code]}")
