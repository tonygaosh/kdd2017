# -*- coding: utf-8 -*-
#!/usr/bin/env python

import math
from datetime import datetime

def time_to_index(date_time):
    return date_time.hour * 3 + int(math.floor(date_time.minute / 20))

def index_to_time():
    if index > 72:
        return None
    hour = index / 3
    minute = index % 3 * 20
    return datetime(hour=hour, minute=minute)