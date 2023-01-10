import time


class Timer:
    def __init__(self, t=30):
        self._time = t

    def countdown(self):
        while self._time:
            print(self._time)
            mins, secs = divmod(self._time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            self._time -= 1
