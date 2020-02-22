"""
logging implementation
"""


def log(*messages):
    with open("log.log", 'w') as log:
        print(*messages, file=log)
