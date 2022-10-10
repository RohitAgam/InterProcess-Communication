from multiprocessing.connection import Listener
from multiprocessing.connection import wait


database = ['Rohit', 2, 4, 'Nikhil', 'Sachin', 10]

address = ('localhost', 6000)
server = Listener(address, authkey=b'rohit')
print('Server Connection Started....')
print('Waiting for communications....')
conn = server.accept()

while True:
    msg = conn.recv()
    if msg == '5th':
        print('\n Requested data to the client....')
        conn.send(database[4])
        conn.close()
        break

server.close()
print('\n Process closed successfully with no errors !!!!')
