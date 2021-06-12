import socket as soc
import cv2,pickle,struct
client_soc = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
host_ip="192.168.00.0"
port =  8080
print("Created successfully")
client_soc.connect((host_ip,port))
data = b""
payload_size =  struct.calcsize("Q")
print("SOCKET ACCEPTED")
while True:
    while len(data) < payload_size:
        packet = client_soc.recv(2160)
        if not packet :
            break
        data += packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q",packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_soc.recv(2160)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame= pickle.loads(frame_data)
    cv2.imshow("Video Received",frame)
    key = cv2.waitKey(1) & 0xFF
    if key ==ord('q'):
            break     
client_soc.close()
