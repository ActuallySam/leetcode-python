from threading import Lock

class H2O:
    def __init__(self):
        self.h_lock=Lock()
        self.o_lock=Lock()
        self.count=0

        self.o_lock.acquire()


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_lock.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.count += 1
        if self.count % 2 == 0:
            self.o_lock.release()
        else:
            self.h_lock.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_lock.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.h_lock.release()