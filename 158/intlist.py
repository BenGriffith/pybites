from decimal import Decimal


class IntList(list):

    @property
    def mean(self):
        return sum(self) / len(self)

    @property
    def median(self):
        if len(self) % 2 == 0:
            index = len(self) // 2
            first_value = self[index - 1]
            second_value = self[index]
            return (first_value + second_value) // 2
        else:
            index = len(self) // 2
            return self[index]

    def append(self, items):
        if isinstance(items, (list)):
            for item in items:
                if not isinstance(item, (int, float, Decimal)):
                    raise TypeError()
            super(IntList, self).extend(items)
            return self

        if not isinstance(items, (int, float, Decimal)):
            raise TypeError()

        super(IntList, self).append(int(items))
        return self

    def __add__(self, other):
        return self.append(other)

    def __iadd__(self, other):
        return self.append(other)