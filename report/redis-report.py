import fire
import redis
import time

class Redisreport(object):
  """Send elastalert data to redis"""
  def __init__(self):
    self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

  def send2redis(self, data, key=time.strftime("%x")):
    ret = self.r.set(key,data)
    return ret



if __name__ == '__main__':
  fire.Fire(Redisreport)