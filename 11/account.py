class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __len__(self):
        return len(self._transactions)

    def __gt__(self, other):
        if self.balance > other.balance:
            return True
        return False

    def __lt__(self, other):
        if self.balance < other.balance:
            return True
        return False

    def __ge__(self, other):
        if self.balance >= other.balance:
            return True
        return False

    def __le__(self, other):
        if self.balance <= other.balance:
            return True
        return False

    def __eq__(self, other):
        if self.balance == other.balance:
            return True
        return False

    def __add__(self, other):
        if not isinstance(self.balance, int) or not isinstance(other, int):
            raise TypeError

        return self._transactions.append(other)

    def __sub__(self, other):
        if not isinstance(self.balance, int) or not isinstance(other, int):
            raise TypeError

        return self._transactions.append(-other)

    def __getitem__(self, position):
        return self._transactions[position]

    def __repr__(self):
        return f"{self.name.capitalize()} account - balance: {self.balance}"


if __name__ == "__main__":
    checking = Account("checking")
    print(len(checking))