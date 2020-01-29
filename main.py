import stomp
import time
import os
from subscriber import MySubscriber

host = os.getenv('ACTIVEMQ_HOST', 'localhost')
port = os.getenv('ACTIVEMQ_PORT', 61613)
user = os.getenv('ACTIVEMQ_USER', 'admin')
password = os.getenv('ACTIVEMQ_PASSWORD', 'password')

print('host port user password', host, port, user, password)

conn = stomp.Connection11([(host, port)])
conn.set_listener('', MySubscriber())
conn.start()
conn.connect(user, password, wait=True)
conn.subscribe(destination='My.Fancy.Queue', id=time.time_ns(), ack='auto')
while True:
    time.sleep(5)
conn.disconnect()

