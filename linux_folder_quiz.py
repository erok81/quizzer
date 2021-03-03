import random
import time
import sys

QUESTIONS = {
    'file type –' : 'regular file',
    'file type d' : 'directory',
    'file type c' : 'character device file',
    'file type b' : 'block device file',
    'file type s' : 'local socket file',
    'file type p' : 'named pipe',
    'file type l' : 'symbolic link',
    'folder type /bin': 'user binaries',
    'folder type /sbin': 'system binaries',
    'folder type /etc': 'configuration files',
    'folder type /dev': 'device files',
    'folder type /proc': 'process information',
    'folder type /var': 'variable files',
    'folder type /tmp': 'temporary files',
    'folder type /usr': 'user programs',
    'folder type /home': 'home directories',
    'folder type /boot': 'boot loader files',
    'folder type lib': 'system libraries',
    'folder type /opt': 'optional add on apps',
    'folder type /mnt': 'mount directory',
    'folder type /media': 'removable devices',
    'folder type /srv': 'servie data',
        }

QUIZ = False
START = input('Start update process? y/n \n')
if START == 'y':
    QUIZ = True

elif START == 'n':
    print('Update delayed 30 minutes...')
    time.sleep(15)
    START = input('Start update process? y/n \n')
    if START == 'y':
        QUIZ = True

while QUIZ:

    QUESTION = random.choice(list(QUESTIONS.items()))
    CHOICE = input(f'What is type {QUESTION[0]}? \n')

    if CHOICE == '?':
        print(f'Study harder next time. The answer is {QUESTION[1]}\n')
        time.sleep(2)
        sys.exit()

    elif CHOICE == QUESTION[1]:
        print('That is correct. Good job')
        time.sleep(2)
        sys.exit()

    while CHOICE != QUESTION[1]:
        CHOICE = input(f'That is incorrect. Try again..What is type {QUESTION[0]}? \n')
        if CHOICE == '?':
            print(f'Study harder next time. The answer is {QUESTION[1]}\n')
            time.sleep(2)
            sys.exit()

        elif CHOICE == QUESTION[1]:
            print('That is correct. Good job')
            time.sleep(2)
            sys.exit()
