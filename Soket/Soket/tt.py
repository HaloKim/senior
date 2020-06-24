import socketserver
import datetime
import base64
import numpy as np
import cv2


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print("get....")
        image1 = []
        try:
            while True:
                data = self.request.recv(82100)  # 클라이언트가보낸데이터를가져옵니다
                print('data,', data)
                # data = base64.b64decode(data)
                if not data or len(data) == 0:
                    break
                image1.extend(data)
            print("get over")
            image = np.asarray(bytearray(image1), dtype="uint8")
            # print("1", image)
            # print("2",len(image))  39559
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            cv2.imwrite("./test.jpg", image)
            cv2.namedWindow("Image")
            cv2.imshow("Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print("받았습니다")
            self.request.sendall("get your connet!".encode("utf-8"))
        except Exception:
            print(self.client_address, "연결해제")
        finally:
            self.request.close()  # 异常之后，关闭连接

    # before handle,연결설정：
    def setup(self):
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(now_time)
        print("연결설정：", self.client_address)

    # finish run  after handle
    def finish(self):
        print("연결해제")


if __name__ == "__main__":
    HOST, PORT = "", 7777
    # server=socketserver.TCPServer((HOST,PORT),MyTCPHandler)  #实例对象，传入参数

    # 多线程
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()  # 계속연결