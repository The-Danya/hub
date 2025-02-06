from script.main.dev import comm
from script.main import main

class Dev:
    res = 0
    imp = None

    def __init__(self):
        self.dev = True
        self.d = open("E:/.documents (arh)/.project/hub/hub/data/Devmode.txt", "r")
        self.Error = open("E:/.documents (arh)/.project/hub/hub/data/Err.txt", "r")
        [_, self.command, _, self.WIP] = self.d.read().split("{}")
        self.Err = self.Error.read().split("\n")
        self.command = self.command.split('\n')
        self.WIP = self.WIP.split("\n")

    def doingcommand(self, command):
        if command == 1: comm.edit()
        if command == 2: comm.help()
        if command == 3: comm.do(self.imp)
        if command == 4: comm.exit()
        main.run()

    def srh(self, imp):
        self.imp = imp
        try:
            self.command.index(imp[1:])
        except ValueError:
            try:
                self.WIP.index(imp[1:])
            except ValueError:
                print(self.Err[0])
            except Exception:
                self.WIP.index(imp[1:])
                print(self.Err[0])
            else:
                print(self.Err[3])
        except Exception:
            print(self.Err[0])
        else:
            print("trying to do '", imp[1:], "'", sep="")
            self.doingcommand(self.command.index(imp[1:]))


    def finich(self):
        self.Error.close()
    def run(self, imp):
        #print(imp[1])
        self.srh(imp)
        self.finich()

def runDev(imp):
    main = Dev()
    main.run(imp)