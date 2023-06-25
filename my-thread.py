import threading
import time

class BankAccount(threading.Thread):
    acctBal = 1000
    def __init__(self, name, amount):
        threading.Thread.__init__(self)
        self.name = name
        self.amount = amount

    def run(self):
        threadlock.acquire()

        BankAccount.getMoney(self)

        threadlock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdraw {} dollars at {}".format(customer.name, customer.amount, time.strftime("%H:%M:%S", time.gmtime())))
        if BankAccount.acctBal >= customer.amount:
            BankAccount.acctBal -= customer.amount
            print("New balance is {} dollars".format(BankAccount.acctBal))

        else:
            print("Insufficient Balance")
            print("Current Balance is {}".format(BankAccount.acctBal))


        time.sleep(3)

threadlock = threading.Lock()

susan = BankAccount("Susan", 200)
vic = BankAccount("Vic", 600)
fay = BankAccount("Fay", 700)
samy = BankAccount("Samy", 200)

susan.start()
vic.start()
fay.start()
samy.start()

susan.join()
vic.join()
fay.join()
samy.join()

print("Transaction Complete!!!")


