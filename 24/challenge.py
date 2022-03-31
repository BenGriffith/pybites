from abc import ABC, abstractmethod


class Challenge(ABC):
    
    def __init__(self, number, title):
        self.number = number
        self.title = title
        self.pretty_title = self.pretty_title()

    @abstractmethod
    def verify(self):
        return self

    @property
    @abstractmethod
    def pretty_title(self):
        return self


class BlogChallenge(Challenge):
    
    def __init__(self, number, title, merged_prs):
        super().__init__(number, title)
        self.merged_prs = merged_prs

    def verify(self, merged_prs):
        if merged_prs in self.merged_prs:
            return merged_prs

    def pretty_title(self):
        return f"PCC1 - {self.title}"


class BiteChallenge(Challenge):
    
    def __init__(self, number, title, result):
        super().__init__(number, title)
        self.result = result
        
    def verify(self, result):
        if result == self.result:
            return result

    def pretty_title(self):
        return f"Bite {self.number}. {self.title}"


# if __name__ == "__main__":
#     bite = BiteChallenge(24, 'ABC and class inheritance', 'my result')
#     print(bite.number, bite.title)
#     print(bite.pretty_title)
#     print(bite.verify("my result"))