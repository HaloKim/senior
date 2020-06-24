import tcpServer
import executer
from multiprocessing import Queue

# make public queue
commandQueue = Queue()

# init module
# 7777 포트에 연결
andRaspTCP = tcpServer.TCPServer(commandQueue, "", 7777)
andRaspTCP.start()

# set module to executer
commandExecuter = executer.Executer(andRaspTCP)

while True:
    try:
        command = commandQueue.get()
        commandExecuter.startCommand(command)
    except:
        pass
