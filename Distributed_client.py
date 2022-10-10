from multiprocessing.connection import Client

address = ('localhost', 6000)
receiver = Client(address, authkey=b'rohit')

receiver.send('5th')
print('Data request sent to server')

while True:
    msg = receiver.recv()
    if msg == 'Sachin':
        print('Data fetched successfully ...')
        print(msg)
        break


receiver.close()
print('Process closed')
