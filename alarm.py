import datetime
import time
from plyer import notification
import os


def set_alarm(alarm_time):
    while True:
        if show_time() == alarm_time:
            # Show notification in Linux
            notification.notify(
                title="Alarma",
                message="¡Ya es hora de levantarse!",
                timeout=5,
            )
            break
        else:
            time.sleep(1)

def show_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return current_time

while True:
    print("Son las:", show_time())
    alarm_input = input("¿A que hora sonara la alarma?(Formato-HH:MM): ")
    # Add seconds to the alarm time
    alarm_time = alarm_input + ":00"
    set_alarm(alarm_time)
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')