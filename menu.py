import sys
import random


def rot_n_encode(message="", n=0):

    # if missing message then exit(1)
    if message == "blank":
        print("ERROR: Missing message")
        sys.exit(1)

    # If missing n-key then pick randomly
    if n == 0:
        n = random.randrange(1, 27)

    

    # encode the message

    # return the message














































if __name__ == "__main__":
    print("Hello World")
    
    # debug
    unicode_num = 61
    for i in range(26):
        unicode_num += i
        unicode_str = '\u' + str(unicode_num)
        print(unicode_str)