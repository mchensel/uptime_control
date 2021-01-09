import datetime
from os import path
import time, os
import winsound

FILE_NAME = path.realpath(r"C:\Anwendungen\Admin_Raffi\using.txt")
CANCEL = "STOP"
COMPUTERZEIT = 25
PAUSENZEIT = 60


def delta(in_time, full_time=None, hours=0, minutes=0, seconds=0):
    if full_time is None:
        return in_time - datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
    else:
        return in_time - full_time


def now(hours=0, minutes=0, seconds=0):
    return delta(datetime.datetime.now(), hours=hours, minutes=minutes, seconds=seconds)


def sleep(seconds=0):
    try:
        with open(FILE_NAME) as f:
            content = f.read().strip()
        if content == CANCEL:
            exit()
    except:
        exit()
    time.sleep(seconds)


def shutdown(in_time=None):

    if in_time is not None:
        seconds = in_time.total_seconds()
        frame = 5
        warning = 300
        while seconds > frame*2:
            if seconds < warning and seconds > warning - frame*2:
                winsound.Beep(1500, 100)
            if seconds < warning/10:
                winsound.Beep(1500, 300)
                winsound.Beep(1500, 150)
            seconds -= frame
            sleep(frame)
    winsound.Beep(1500, 300)	
    winsound.Beep(1500, 300)	
    winsound.Beep(1500, 300)	
    sleep(10)
    os.system("shutdown /s")
    return True


def innerhalb_der_zeit(last_time):
    if now(minutes=2) > last_time:
        return False
    return shutdown(last_time - now(minutes=COMPUTERZEIT))


def schon_1_stunde_pause(last_time):
    if now(minutes=PAUSENZEIT) < last_time:
        return False
    with open(FILE_NAME, "w") as f:
        f.write(str(now()))
    return shutdown(now() - now(minutes=COMPUTERZEIT))


def main():
    last_time = now()
    try:
        with open(FILE_NAME) as f:
            for line in f:
                content = line.strip()
                if content:
                    last_time = datetime.datetime.strptime(
                        content,  "%Y-%m-%d %H:%M:%S.%f")
    except Exception as e:
        with open(FILE_NAME, "w") as f:
            f.write(str(now()))
    checks = [
        innerhalb_der_zeit,
        schon_1_stunde_pause]
    for func in checks:
        if not func(last_time):
            continue
        exit()
    shutdown()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
