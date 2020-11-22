import sys
from stars import StarsClient

# Python script in charge of creating a client instance and running queries 
client = StarsClient()
repoList = sys.argv
repoList.pop(0)
response = client.submit_API_call(repoList)
print(response)