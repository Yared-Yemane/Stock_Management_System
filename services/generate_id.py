from datetime import datetime

def generate_id():
    now = datetime.now()
    id = str(now.day+now.month+now.year+now.hour+now.minute+now.second+now.microsecond)

    return id