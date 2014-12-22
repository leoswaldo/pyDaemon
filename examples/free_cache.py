#!/python3/bin/python3

import sys
import time
from daemon import Daemon


class FreeCache(Daemon):
    '''
        This class is a daemon that frees the mem cache ever day
    '''

    ## Method: run is overrided from Daemon class
    #  Description: this method will be the code executed as daemon, it frees
    #      mem cache
    def run(self):
        while True:
            with open('/proc/sys/vm/drop_caches', 'w') as f:
                f.write('1')
            f.close()
            time.sleep(86400)

if __name__ == "__main__":
    daemon = FreeCache('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("Usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)