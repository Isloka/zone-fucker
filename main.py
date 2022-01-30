import random, requests, json

config = json.load(open("config.json"))

while True:
  user_agent = random.choice(config["user_agents"])
  rDefacer = random.choice(config["gays"])
  try:
    finalDomain = requests.get(f"http://{random.choice(config['domains'])}/", timeout=config["timeout"]).url
    res = requests.post("http://www.zone-h.org/notify/single", headers={"User-Agent": user_agent}, data=[("defacer", rDefacer), ("domain1", finalDomain), ("hackmode", random.randint(1, 7)), ("reason", random.randint(1, 7))]).text
    if "You are banned. Probably because you spammed the onhold." in res:
      print("[X] You have been banned from Zone-H, change your IP and try again.")
      break
    else:
      print(f"{rDefacer} > {finalDomain} [{user_agent}]")
  except:
    continue