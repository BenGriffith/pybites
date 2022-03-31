from abc import ABC, abstractmethod


class Challenge(ABC):
    
    def __init__(self, number, title):
        self.number = number
        self.title = title

    @abstractmethod
    def verify(self):
        return "Subclassed obj should verify"

    @abstractmethod
    def pretty_title(self):
        return "Subclassed obj should pretty_title"


class BlogChallenge(Challenge):
    
    def __init__(self, number, title, merged_prs):
        super().__init__(number, title)
        self.merged_prs = merged_prs

    def verify(self, merged_prs):
        if merged_prs in self.merged_prs:
            return merged_prs

    @property
    def pretty_title(self):
        return f"PCC1 - {self.title}"


class BiteChallenge(Challenge):
    
    def __init__(self, number, title, result):
        super().__init__(number, title)
        self.result = result
        
    def verify(self, result):
        if result == self.result:
            return result

    @property
    def pretty_title(self):
        return f"Bite {self.number}. {self.title}"