from datetime import datetime
from dateutil.rrule import *

dtstart = datetime(2018, 12, 24)
weekdays = rrule(WEEKLY, byweekday=(SA, SU, MO, TU, WE), dtstart=dtstart)
# laborday = rrule(DAILY, dtstart=datetime(2018, 12, 7), count=1)
# offsite_training = rrule(DAILY, dtstart=datetime(2018, 12, 10), count=4)

rules = [
    # (laborday,  0),
    # (offsite_training, 3),
    (weekdays, 8),
]
