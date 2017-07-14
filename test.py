from db import User

def users_url():
	
	u=User
	b=[]
	for i in range(99):
		a=u.query.get(i+1)
		b.append(a.profile_url)
	return b
	
links = users_url()	
print(links)