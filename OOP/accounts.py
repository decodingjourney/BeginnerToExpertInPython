import datetime
import pytz


class Account:
    """Simple accounts class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_history = [(Account._current_time(), balance)]
        print("Account has been created for " + self._name)
        # self.showBalance()


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_history.append((Account._current_time(), amount))
            self.showBalance()

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_history.append((Account._current_time(), -amount))
        else:
            print("The amount should be greater than 0 and no more than your account balance")
        self.showBalance()


    def showBalance(self):
        print("Balance is {}".format(self.__balance))

    def show_transaction(self):
        for date, amount in self._transaction_history:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

if __name__ == '__main__':
    anand = Account("Anand", 0)
    anand.showBalance()
    anand.deposit(10000)
    anand.withdraw(5000)
    anand.withdraw(6000)
    anand.show_transaction()

    sonam = Account("Sonam", 800)
    sonam.deposit(200)
    sonam.withdraw(300)
    sonam.show_transaction()
    sonam.__balance = 50
    sonam.showBalance()
    print(sonam.__dict__)
