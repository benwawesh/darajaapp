from datetime import datetime
def date_generator():
    unformatted_time =datetime.now()
    formatted_time= unformatted_time.strftime("%Y%m%d%H%M%S")
    return formatted_time