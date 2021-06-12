import socket 
import cv2,pickle,struct
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("HOST IP: ",host_ip)
port = 8080
socket_address = ('0.0.0.0',port)
print("Created successfully")
server_socket.bind(socket_address)
print("Bind successful")
server_socket.listen(5)
print("LISTENING AT: ",socket_address)
while True:
    client_socket,addr = server_socket.accept()
    print("Got the connection from :" , addr)
    if client_socket:
        vid=cv2.VideoCapture(0)
        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            cv2.imshow("VIDEO ",frame)
            key=cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                client_socket.close()
