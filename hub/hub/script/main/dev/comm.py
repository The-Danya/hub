import os
import sys

def edit():

    txt = os.listdir("../../data")

    rq = open("E:/.documents (arh)/.project/hub/hub/data/request.txt", "r")
    rs = open("E:/.documents (arh)/.project/hub/hub/data/response.txt", "r")
    d = open("E:/.documents (arh)/.project/hub/hub/data/do.txt", "r")
    Error = open("E:/.documents (arh)/.project/hub/hub/data/Err.txt", "r")
    dev = open("E:/.documents (arh)/.project/hub/hub/data/Devmode.txt", "r")
    Q = rq.read().split("\n")
    A = rs.read().split("\n")
    do = d.read().split("\n")
    Err = Error.read().split("\n")
    [_, command, _, WIP] = dev.read().split("{}")
    Err = Error.read().split("\n")
    command = command.split('\n')
    WIP = WIP.split("\n")

    print("which category u want chance?", txt)
    while True:
        n = input()
        try:
            txt.index(n)
        except Exception:
            pass
        else:
            break
    rq.close()
    rs.close()
    d.close()
    Error.close()
    dev.close()

def help():
    dev = open("E:/.documents (arh)/.project/hub/hub/data/Devmode.txt", "r")
    print(dev.read())
    dev.close()

def do(st):
    d = open("E:/.documents (arh)/.project/hub/hub/data/do.txt", "r")
    dotxt = d.read().split("\n")
    print("what do you want to do?", dotxt)
    n = "notepad"
    while True:
        n = input()
        try:
            dotxt.index(n)
        except Exception:
            pass
        else:
            path = 'C:/Windows' + "/ "[0]  + str(n) + ".exe"
            os.startfile(path)
            break
    d.close()

def exit():
    print("shut down")
    sys.exit()
