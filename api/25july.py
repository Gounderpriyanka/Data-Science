import requests

url ="https://jsonplaceholder.typicode.com/comments"

"""
params = {
    "postId": 1
}
"""
params = {
    "id": [1,2,3,4,5]
}
response = requests.get(url,params=params)

print(response.url)
print(response.status_code)

comments = response.json()

# for i in comments:
#     print(i['email'])

# name , email  for post_id 1,2,3,4,5
for i in range(5):
    print(comments[i]["name"])
    print(comments[i]["email"])
    print("-"*40)