# 0x03. Log Parsing

## Description

This project involves developing a Python script to parse and process log data streams in real-time. The script reads from standard input (stdin), processes the data, and computes specific metrics based on the log entries.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder is mandatory
- Code should follow the PEP 8 style (version 1.7.x)
- All files must be executable
- The length of files will be tested using `wc`

## Concepts

To successfully complete this project, you will need to understand the following concepts:

- **File I/O in Python**: Reading from `sys.stdin` line by line.
- **Signal Handling in Python**: Handling keyboard interruptions (CTRL + C) using signal handling in Python.
- **Data Processing**: Parsing strings to extract specific data points and aggregating data to compute summaries.
- **Regular Expressions**: Using regular expressions to validate the format of each line.
- **Dictionaries in Python**: Counting occurrences of status codes and accumulating file sizes.
- **Exception Handling**: Handling possible exceptions during file reading and data processing.

## Task

### 0. Log parsing

Write a script that reads stdin line by line and computes metrics:

- **Input format**: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
  - If the format is not as above, the line must be skipped.
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
  - **Total file size**: `File size: <total size>`
    - `<total size>` is the sum of all previous `<file size>` values.
  - **Number of lines by status code**:
    - Possible status codes: `200`, `301`, `400`, `401`, `403`, `404`, `405`, `500`
    - If a status code doesn’t appear or is not an integer, don’t print anything for this status code.
    - Format: `<status code>: <number>`
    - Status codes should be printed in ascending order.

### Example

```shell
alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
    for line in sys.stdin:
KeyboardInterrupt
alexa@ubuntu:~/0x03-log_parsing$ 
