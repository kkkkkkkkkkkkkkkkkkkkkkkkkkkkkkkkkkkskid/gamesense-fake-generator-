import secrets
import time
import termcolor
from termcolor import colored, cprint

counter = 0

password_length = 40

print(colored("gamesense.pub invite generator", 'red'))
time.sleep(1)
print(colored("connecting to server", 'red'))
time.sleep(3)
print(colored("connected", 'red'))
time.sleep(0.5)
print(colored("creating invites", 'red'))
time.sleep(2)
while counter < 15:
  print(colored(secrets.token_urlsafe(password_length), 'green'))
  time.sleep(1)
  counter = counter + 1
else:
  print("invites generated")
  print(colored("made by trash#3228", 'magenta'))