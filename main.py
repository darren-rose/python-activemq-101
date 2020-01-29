import stomp
import time
import os
from subscriber import MySubscriber

conn = stomp.Connection11([('localhost', 61613)])
conn.start()
conn.set_listener('', MySubscriber())

user = os.getenv('ACTIVEMQ_USER', 'admin')
password = os.getenv('ACTIVEMQ_PASSWORD', 'password')

print('user password', user, password)

conn.connect(user, password, wait=True)
conn.subscribe(destination='My.Fancy.Queue', id=1, ack='auto')
while True:
    time.sleep(5)
conn.disconnect()

