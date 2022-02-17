import requests
#addr = "http://52.149.157.221:5001"
addr = "http://20.196.224.221:8090"

r = requests.get(f'{addr}/employee/mike')
print(r.text)

r = requests.post(f'{addr}/employee', data={'name': 'mike'})
print(r.text)

r = requests.put(f'{addr}/employee', data={'name': 'mike', 'new_name': 'taehun'})
print(r.text)

r = requests.delete(f'{addr}/employee', data={'name': 'taehun'})
print(r.text)

"""
r = requests.get (
     "http://localhost:8090/rest/server/containers/business-application-kjar/processes"
)
print(r.text)

headers={
    'Content-type':'application/json', 
    'Accept':'application/json'
}

r = requests.post (
     "http://localhost:8090/rest/server/containers/business-application-kjar/processes/business-application-kjar.my_sample_process/instances",
     headers=headers
)
print(r.text)
"""