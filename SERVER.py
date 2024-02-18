#for 1 client

import socket

INFO_CENTER = (socket.gethostname(), 8000)
print(INFO_CENTER)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(INFO_CENTER) 
server.listen()   #listen to the server port

print("I am listening your connections")

client, address = server.accept()

while True:
    msg = ''
    while True:
        symbol = client.recv(1).decode()
        if symbol in ('|', ''): break
        msg += symbol
    
    #print("Got in server:", msg)

    if msg == 'server,give_tasks': #после первого подключения клиента получает данное сообщение
        client.send(str("tasks" + '|').encode()) #сервер отправляет задания в таком виде crash.189.48,medic_aid.104.158,fire.1.199;
    
    elif msg.startswith('server,reserve_task'):
        task_id = int(msg.split(',')[-1])
        print("task_id", task_id)

        
        client.sendall('ok|'.encode())
         
            
    
    elif msg == 'hub,offload':
            client.sendall('ok|'.encode())
            
        
    
    # elif msg.startswith('hub,give'):  
    #     if current_equipment == equipments[0]: #'no_equipment'
    #         eq_id = int(msg.split(',')[-1])
    #         current_equipment = equipments[eq_id] 
    #         client.sendall('ok|'.encode())
    #     else:
    #         client.sendall('error|'.encode())
    #         fail = True
            
    
    # elif msg == 'equip_ready':
    #     sock.close()
    #     if current_equipment == need_equipment and reserved_task == nearest_task_id and not fail:
    #         return True
    #     else:
    #         return False
    
    else:
        server.close()
        break
        
