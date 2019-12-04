# Exceptions in Python

# for i in range(5):
#     print("Hello, World!")

"""
    Exceptions Clauses

try:
    # Runs first
    < code >
except:
    # Runs if exception occurs in try block
    < code >
else:
    # Executes if try block *succeeds*
    < code >
finally:
    # This code *always* executes
    < code >
"""

import logging
import time

# Create logger
logging.basicConfig(filename="/home/joel/Desktop/Python/Socratica/logs/problems.log", level=logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time required."""
    start_time = time.time()
    try:
        f = open(path, mode="rb")
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("Time required for {file} = {time}".format(file=path, time=dt))

data = read_file_timed("/home/joel/Desktop/Python/Socratica/logs/info.txt")
