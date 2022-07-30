import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        if not re.search(r'.*\.[a-z]{2,3}$', name):
            raise DomainException
        self.name = name
        
    # next add a __str__ method and write 2 class methods
    # called parse_url and parse_email to construct domains
    # from an URL and email respectively
    def __str__(self):
        return self.name

    @classmethod
    def parse_url(cls, url):
        domain = url.split("/", 2)[2]
        has_slash = domain.find("/")
        if has_slash > 0:
            return cls(domain[:has_slash])
        return cls(domain)
    
    @classmethod
    def parse_email(cls, email):
        at_symbol = email.find("@")
        return cls(email[at_symbol + 1:])
        

if __name__ == "__main__":
    #amazon = Domain.parse_url("http://google.com")
    email = Domain.parse_email("ben@gmail.com")
    print(email)