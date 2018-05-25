import time
from flask import Flask



# Connect to Redis
#redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    #try:
     #   visits = redis.incr("counter")
    #except RedisError:
     #   visits = "<i>cannot connect to Redis, counter disabled</i>"

   # html = "<h3>Hello {name}!</h3>" \
    #       "<b>Hostname:</b> {hostname}<br/>" \
     #      "<b>Visits:</b> {visits}"
   # return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)
     
	msg= time.ctime()
	msg = "<h1>Hello Ahmad Muammar</h1>" + "\n" + "time now is: " + msg
	return msg
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
