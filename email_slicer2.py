# Asking the user to enter their email address and then stripping the white spaces.
email = input('Enter your email address: ').strip()

# Slicing the email address from the beginning to the index of the @ symbol.
email_address = email[:email.index('@')]

# Slicing the email address from the index of the @ symbol to the end of the string.
domain_address = email[email.index('@') + 1:]

# A string literal.
output = f'Your email_address is {email_address} and domain name is {domain_address} '

print(output)
