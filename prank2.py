import winsound
from random import randrange

frequency = randrange(10000)
duration = randrange(5000)
winsound.Beep(frequency, duration)
