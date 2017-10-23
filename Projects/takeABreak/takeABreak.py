import time
import webbrowser

totalBreaks = 3
breakCount = 0

print "This program started on " + time.ctime()

while breakCount < totalBreaks:
    # Test time for now, finished will be 2 hours
    time.sleep(1)
    webbrowser.open("https://www.google.com")
    breakCount += 1