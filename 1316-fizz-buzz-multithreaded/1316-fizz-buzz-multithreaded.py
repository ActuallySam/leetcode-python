from threading import Lock

class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.fizz_lock = Lock()
        self.buzz_lock = Lock()
        self.fb_lock = Lock()
        self.num_lock = Lock()

        self.fizz_lock.acquire()
        self.buzz_lock.acquire()
        self.fb_lock.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for _ in range(self.n//3-self.n//15):
            self.fizz_lock.acquire()
            printFizz()
            self.num_lock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for _ in range(self.n//5-self.n//15):
            self.buzz_lock.acquire()
            printBuzz()
            self.num_lock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for _ in range(self.n//15):
            self.fb_lock.acquire()
            printFizzBuzz()
            self.num_lock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            self.num_lock.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.fb_lock.release()
            elif i % 3 == 0:
                self.fizz_lock.release()
            elif i % 5 == 0:
                self.buzz_lock.release()
            else:
                printNumber(i)
                self.num_lock.release()
            

        