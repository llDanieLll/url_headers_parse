import urllib.request
import urllib.parse

try:
    url = 'https://pythonprogramming.net/search'
    values = {'q':'url'}
    headers = {}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

    req = urllib.request.Request(url,data=data,headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('url_with_headers_parse.txt','w')
    saveFile.write(str(respData))
    saveFile.close

except Exception as e:
    print (str(e))
