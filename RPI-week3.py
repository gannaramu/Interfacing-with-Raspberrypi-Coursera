import http.client
connection = http.client.HTTPSConnection("www.uci.edu")
connection.request("GET","/")
res = connection.getresponse()
data = res.read()
print(data)
