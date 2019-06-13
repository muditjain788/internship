
#!/usr/bin/python2

import  socket 
recv_ip="127.0.0.1"
recv_port=4444  

#  creating  udp socket with ip as ipv4  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  fitting    ip and port  with udp socket 
s.bind((recv_ip,recv_port))

#   receiving  data  from  sender  
while  6>3 :
    data=s.recvfrom(100)  
    print("message  from sender  ",data[0])
    print("sender IP + port --socket  ",data[1])
    #  reply to sender  
    rply=raw_input("type your rply  : ")
    s.sendto(rply,data[1])


s.close()

