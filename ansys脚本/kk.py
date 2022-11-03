from __future__ import print_function
import threading
import time

class Concur(threading.Thread):
    def __init__(self):
        super(Concur, self).__init__()
        self.iterations = 0
        self.daemon = True  # Allow main to exit even if still running.
        self.paused = True  # Start out paused.
        self.state = threading.Condition()

    def run(self):
        self.resume()
        while True:
            with self.state:
                if self.paused:
                    self.state.wait()  # Block execution until notified.
            # Do stuff...
            time.sleep(.1)
            self.iterations += 1

    def pause(self):
        with self.state:
            self.paused = True  # Block self.

    def resume(self):
        with self.state:
            self.paused = False
            self.state.notify()  # Unblock self if waiting.


class Stopwatch(object):
    """ Simple class to measure elapsed times. """
    def start(self):
        """ Establish reference point for elapsed time measurements. """
        self.start_time = time.time()
        return self

    @property
    def elapsed_time(self):
        """ Seconds since started. """
        try:
            return time.time() - self.start_time
        except AttributeError:  # Wasn't explicitly started.
            self.start_time = time.time()
            return 0



MAX_RUN_TIME = 5  # Seconds.
concur = Concur()
stopwatch = Stopwatch()

print('Running for {} seconds...'.format(MAX_RUN_TIME))
concur.start()
while stopwatch.elapsed_time < MAX_RUN_TIME:
    concur.resume()
    # Can also do other concurrent operations here...
    concur.pause()
    # Do some other stuff...

# Show Concur thread executed.
print('concur.iterations: {}'.format(concur.iterations))