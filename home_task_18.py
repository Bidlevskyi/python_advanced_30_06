from multiprocessing import Process, Pipe
from time import sleep
from os import getpid

def ponger(message, parent_conn, child_conn):
    while True:
        parent_conn.recv()
        print(f'Process{getpid()} got message: {message}')
        sleep(2)
        child_conn.send(message)

if __name__ == "__main__":
    parent_conn_1, child_conn_1 = Pipe()
    parent_conn_2, child_conn_2 = Pipe()

    process_1 = Process(target=ponger, args=("pin", parent_conn_1, child_conn_2))
    process_2 = Process(target=ponger, args=("pon", parent_conn_2, child_conn_1))

    process_1.start()
    process_2.start()
    child_conn_1.send("pon")
