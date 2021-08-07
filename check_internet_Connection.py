import urllib.request
import urllib

def connect(host='http://iitdeveloper.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
#print( "connected" if connect() else "no internet!" )