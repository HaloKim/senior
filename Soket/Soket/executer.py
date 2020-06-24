class Executer:
    def __init__(self, tcpServer):
        self.andRaspTCP = tcpServer

    def startCommand(self, command):
        if command == "A\n":
            self.andRaspTCP.sendAll("321\n")
        if command == "안녕하세요\n":
            self.andRaspTCP.sendAll("안녕하세요\n")