########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Training-key': '95972f7ae46a4c039639f02df059a7df',
}

params = urllib.parse.urlencode({
    # Request parameters
    'projectId': 'c64d3e16-27f2-495c-8546-dbd4f54072cd',
    'name': 'amiya_forged',
})

try:
    conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/customvision/v3.3/Training/projects/c64d3e16-27f2-495c-8546-dbd4f54072cd/tags?name=amiya_forged&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################