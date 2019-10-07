import re

def email_validator(email):

    email_checker = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,64}$'

    if re.search(email_checker,email):
        print('{} is a valid email address.'.format(email))
    else:
        print('{} is not a valid email address.'.format(email))

print("-----------------------------------")
print("Printing valid e-mail addresses...")
print("-----------------------------------")

# Valid e-mails
email_validator('email@domain.com')
email_validator('firstname.lastname@domain.com')
email_validator('email@subdomain.domain.com')
email_validator('firstname+lastname@domain.com')
email_validator('1234567890@domain.com')
email_validator('email@domain-one.com')
email_validator('_______@domain.com')
email_validator('email@domain.name')
email_validator('email@domain.co.jp')
email_validator('firstname-lastname@domain.com')

print("-----------------------------------")
print("Printing invalid e-mail addresses...")
print("-----------------------------------")

# Invalid e-mails
email_validator('plainaddress')
email_validator('#@%^%#$@#$@#.com')
email_validator('@domain.com')
email_validator('Joe Smith <email@domain.com>')
email_validator('email.domain.com')
email_validator('email@domain@domain.com')
email_validator('email..email@domain.com')
email_validator('あいうえお@domain.com')