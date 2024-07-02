# Define a base exception class UserError and two subclasses AuthenticationError and AuthorizationError. 
# Write a function that simulates user login and raises AuthenticationError for invalid credentials and AuthorizationError 
# for insufficient permissions. Handle these exceptions with appropriate messages.

class UserError(Exception):
    list_of_allowed_users = ['redyodarocky', 'whiplashheat', 'neorushgenie', 'neogrootheat', 'timondoryran', 'incendiesred', 'pathsofglory']
    domain_name = 'moviebuff.com'
    def __init__(self, username, domain, message=None) -> None:
        self.username = username
        self.domain = domain
        super().__init__(message)
        
    def checkID(self):
        if not self.username in UserError.list_of_allowed_users:
            raise AuthenticationError(self.username, self.domain)
        elif not self.domain == UserError.domain_name:
            raise AuthorizationError(self.username, self.domain)
        return f'You have successfully logged in as {self.username}@{self.domain}!'

class AuthenticationError(UserError):
    def __init__(self, username, domain, message='ERROR: Your username/password is incorrect.') -> None:
        self.message = message
        super().__init__(username, domain, message)

class AuthorizationError(UserError):
    def __init__(self, username, domain, message='ERROR: You are not authorized to view this page.') -> None:
        self.message = message
        super().__init__(username, domain, message)

def login():
    try:
        credentials = input('Email ID: ')
        l = credentials.partition('@')
        username = l[0]
        domain = l[2]
        per1 = UserError(username, domain)
        print(per1.checkID())
    except AuthenticationError as u:
        print(u)
    except AuthorizationError as d:
        print(d)

login()
