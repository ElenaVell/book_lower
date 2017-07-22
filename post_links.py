from db import User, Post

def users_url():
    u = User
    b = list()
    for i in range(25):
    	a = u.query.get(i+1)
    	b.append(a.reviews_url)
    return b

if __name__ == "__main__":
    links = users_url()
    print(links)
