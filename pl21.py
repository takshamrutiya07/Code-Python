# import requests
# url = 'https://jsonplaceholder.typicode.com/posts'
# response = requests.get(url)

# if response.status_code == 200:
#     posts = response.json()
#     print("Fetched Posts:")
#     for post in posts[:5]: 
#         print(f"Title: {post['title']}")
# else:
#     print(f"Failed to retrieve posts. Status code: {response.status_code}")

# import requests
# url = 'https://jsonplaceholder.typicode.com/posts'

# new_post = {
#     "title": "My New Post",
#     "body": "This is the content of my new post.",
#     "userId": 1
# }
# response = requests.post(url, json=new_post)
# if response.status_code == 201:
#     created_post = response.json()
#     print("Created Post:")
#     print(f"Title: {created_post['title']}")
#     print(f"Body: {created_post['body']}")
# else:
#     print(f"Failed to create post. Status code: {response.status_code}")


# import requests
# url = 'https://jsonplaceholder.typicode.com/posts/1000' 

# response = requests.get(url)
# if(response.status_code == 200):
#     post = response.json()
#     print("Fetched Post:", post)
# else:
#     print(f"Error: {response.status_code} - {response.reason}")


import requests
class APIClient:
    def __init__(self):
        self.url = "https://jsonplaceholder.typicode.com/posts"
    def get_posts(self):
        response = requests.get(self.url)
        return response.json()

    def create_post(self, title, body, user_id):
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = requests.post(self.url, json=data)
        return response.json()
    
client = APIClient()
posts = client.get_posts()
print(posts[:3]) 
new_post = client.create_post("Hello", "This is a test post", 1)
print(new_post)

