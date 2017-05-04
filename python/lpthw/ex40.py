import time

class Song(object):
    """Modified demo class."""
    def __init__(self, lyrics, timing=2):
        self.lyrics = lyrics
        self.timing = timing

    def sing(self):
        print("\n\n")
        for line in self.lyrics:
            print(line)
            time.sleep(self.timing)

bday = [
    "Happy birthday to you",
    "I don't want to get sued",
    "so I'll make up some lyrics",
    "and leave that with you"
    ]

uncle = [
    "Whoa... are we moving to slow",
    "Have you seen us, uncle Rhemus?",
    "We look pretty sharp in these clothes",
    "(Yes we do)",
    "Unless we get sprayed with a hose."
    ]

first = Song(bday)
second = Song(uncle)
