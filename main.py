import random
import requests
import socket
import domains
import defacers
import useragents
while True:
  hm = str(random.randint(1, 31))
  r = str(random.randint(1, 7))
  ua = random.choice(useragents.list)
  domain = random.choice(domains.list)
  try:
    socket.gethostbyname(domain)
    finalDomain = 'https://'+domain+'/'
    rDefacer = random.choice(defacers.list)
    r = requests.post('http://www.zone-h.org/notify/single', headers={"User-Agent": ua}, data=[('defacer', rDefacer), ('domain1', finalDomain), ('hackmode', hm), ('reason', r)])
    if "You are banned. Probably because you spammed the onhold." in r.text:
      print("[X] You have been banned from Zone-H, change your IP and try again.")
      break
    else:
      print(rDefacer+' > '+finalDomain+' ['+ua+']')
  except socket.gaierror:
    continue
