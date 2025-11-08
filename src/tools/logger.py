from datetime import datetime
import pytz

def current_time_str():
    pytz_timezone = pytz.timezone("Europe/Kyiv")
    return datetime.now(pytz_timezone).strftime("%Y-%m-%d %H:%M")