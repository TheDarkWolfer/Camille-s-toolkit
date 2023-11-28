#use threads to make a non-blocking input
import threading
import time

class InputThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.input = None

    def run(self):
        self.input = input("Enter something: ")

    def get_input(self):
        return self.input
    
def main():
    thread = InputThread()
    thread.start()
    time.sleep(5)
    print("You entered: %s" % thread.get_input())