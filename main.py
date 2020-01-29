import stomp
import time

from subscriber import MySubscriber

conn = stomp.Connection11([('localhost', 61613)])
conn.start()
conn.set_listener('', MySubscriber())
conn.connect('admin', 'p4cm4n', wait=True)
conn.subscribe(destination='My.Fancy.Queue', id=1, ack='auto')
while True:
    time.sleep(5)
conn.disconnect()

