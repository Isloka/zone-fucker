import random
import requests
import socket
import domains
import subdomains
import defacers
import useragents
while True:
  hm = str(random.randint(1, 31))
  r = str(random.randint(1, 7))
  ua = random.choice(useragents.list)
  sub = random.choice(subdomains.list)
  domain = random.choice(domains.list)
  try:
    socket.gethostbyname(sub+'.'+domain)
    finalDomain = 'https://'+sub+'.'+domain+'/'
    rDefacer = random.choice(defacers.list)
    r = requests.post('http://www.zone-h.org/notify/single', headers={"User-Agent": ua}, data=[('defacer', rDefacer), ('domain1', finalDomain), ('hackmode', hm), ('reason', r)])
    print(rDefacer+' > '+finalDomain+' ['+ua+']')
  except socket.gaierror:
    continue
