from datetime import datetime, timedelta
import os
import time
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    line_split = line.split(" ")
    for word in line_split:
        try:
            line_ts = datetime.strptime(word, "%Y-%m-%dT%H:%M:%S")
            return line_ts
        except:
            continue

    return None


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_events = [line.strip("\n") for line in loglines if "Shutdown initiated" in line]
    first_shutdown = convert_to_datetime(shutdown_events[0])
    last_shutdown = convert_to_datetime(shutdown_events[1])
    return last_shutdown - first_shutdown


#if __name__ == "__main__":
    #print(convert_to_datetime('INFO 2014-07-03T23:27:51 supybot Shutdown initiated.\n'))
    #print(time_between_shutdowns(loglines))