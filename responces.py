from datetime import datetime


def sample_responces(input_text):
    user_message = str(input_text).lower

    if user_message in ("hello", "hi", "sup"):
        return "Hey! how it's going?"

    if user_message in ("who are you", "who are you?"):
        return "I am AI Coder"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

    return str(date_time)


return "Sorry, I don't understand you..."
