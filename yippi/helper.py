import time, requests, yippi.exceptions
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Yippi/1.0 (by Error- on e621)'
}

def RateLimit(maxPerSecond):
    minInterval = 1.0 / float(maxPerSecond)
    def decorate(func):
        lastTimeCalled = [0.0]
        def rateLimitedFunction(*args,**kargs):
            elapsed = time.clock() - lastTimeCalled[0]
            leftToWait = minInterval - elapsed
            if leftToWait>0:
                time.sleep(leftToWait)
            ret = func(*args,**kargs)
            lastTimeCalled[0] = time.clock()
            return ret
        return rateLimitedFunction
    return decorate

@RateLimit(2)
def getAPI(url):
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        pass
    else:
        return r.raise_for_status()
    return r.json()

@RateLimit(2)
def getxmlAPI(url):
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        pass
    else:
        return r.raise_for_status()
    return BeautifulSoup(r.text, 'xml')

@RateLimit(2)
def getTagsInfo(tag):
    r = requests.get("https://e621.net/tag/index.json?name={}&limit=1".format(tag), headers=header)
    if r.status_code == 200:
        pass
    else:
        return r.raise_for_status()
    if not r.json():
        return yippi.exceptions.NoSuchException
    return r.json()[0]
