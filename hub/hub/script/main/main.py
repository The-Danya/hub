from script.main.dev import mode


class main:
    def __init__(self):
        self.Devmode = False
        self.str = None
        self.out = None
        self.rq = open("../../data/request.txt", "r")
        self.rs = open("../../data/response.txt", "r")
        self.d = open("../../data/do.txt", "r")
        self.Error = open("../../data/Err.txt", "r")
        self.Q = self.rq.read().split("\n")
        self.A = self.rs.read().split("\n")
        self.do = self.d.read().split("\n")
        self.Err = self.Error.read().split("\n")

    def impstr(self):
        self.str = input()

    def output(self, x):
        print(x)
        if self.Devmode:
            print(self.Q)
            print(self.A)
            print(self.Err)

    def working(self):
        ind = "None"
        while True:
            self.impstr()
            try:
                ind = self.Q.index(self.str)
            except ValueError:
                try:
                    if self.str[0] == "/":
                        mode.runDev(self.str)
                        ind = mode.Dev.res
                        break
                except IndexError:
                    print(self.Err[2])
                else: print(self.Err[1])
            except Exception:
                print(self.Err[0], "repeat? y/n")
                if input() == "n": break
                elif input() == "y": pass
                else: print(self.Err[0])
            else:
                break
        self.out = self.A[ind]

    def finish(self):
        print("work complete")
        self.rq.close()
        self.rs.close()
        self.d.close()
        self.Error.close()

    def run(self):
        print("starting work")
        self.working()
        self.output(self.out)


def run():
    hub = main()
    hub.run()
if __name__ == '__main__':
    run()