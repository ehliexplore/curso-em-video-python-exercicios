import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print("I couldn't open the website.")
else:
    print("I am able to successfully open the website.")
    print(site.read())

