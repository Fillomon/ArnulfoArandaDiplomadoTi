import requests
r= requests.get("https://api.github.com/search/repositories?q=language:python")
data=r.json( )

print(type(data))
#print(data.items())

for k,v in data.items():
    print(k,'->',v,'\n')

print(data['total_count'])
