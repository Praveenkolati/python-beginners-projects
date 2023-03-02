# Asking the user to enter their email address and then stripping the white spaces.
email_address = input('Enter your email address: ').strip()

# Splitting the email address into three parts.
new = email_address.partition('@')

# Printing the user name and the domain name.
print(f'User name {new[0]} and {new[-1]}')
