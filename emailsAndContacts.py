# Regular Expressions
import re, pyperclip

text = pyperclip.paste()
phone = re.compile(r"""
((\+?\d{3})?
([ -]?)
(\d{2,3})
([ -]?)
(\d{3})
([ -]?)
(\d{3,4}))
""", re.VERBOSE|re.I)

email = re.compile(r"""
([a-z][a-z0-9-]+@
([a-z]+\.[.a-z]+)+)
""", re.VERBOSE|re.I)

contacts = [contact[0]  for contact in phone.findall(text)]
emails = [mail[0] for mail in email.findall(text)]

result = "EMAILS\n"
for email in emails:
    result += f"{email}\n"

result += "\nCONTACTS\n"
for contact in contacts:
    result += f"{contact}\n"

pyperclip.copy(result)
