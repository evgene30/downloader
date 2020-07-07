from datetime import datetime

def DataTime():
    now = datetime.now()
    date = now.strftime("%d.%m.%Y (%A)")
    return date