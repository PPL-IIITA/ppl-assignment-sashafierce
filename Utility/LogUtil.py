"""
utility class for logging 
"""
from datetime import datetime

"""
Method for logging various events like couple formation and gifting 
"""
def log_events(event_type, event_desc):
    timestamp = datetime.now().strftime('%Y/%m/%d_%H:%M:%S - ')
    outfile = 'logfile.txt'
    with open(outfile , "a") as logfile:
        logfile.write(timestamp + event_type + " " + event_desc + '\n')

