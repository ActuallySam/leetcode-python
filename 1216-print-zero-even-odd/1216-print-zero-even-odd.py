from threading import Lock

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.even_lock = Lock()
        self.odd_lock = Lock()
        self.zero_lock = Lock()

        self.even_lock.acquire()
        self.odd_lock.acquire()    
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            self.zero_lock.acquire()
            printNumber(0)
            if i % 2 == 1:
                self.odd_lock.release()
            else:
                self.even_lock.release()
        
        
    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(2, self.n + 1, 2):
            self.even_lock.acquire()
            printNumber(i)
            self.zero_lock.release()
        
        
        
    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1, 2):
            self.odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()