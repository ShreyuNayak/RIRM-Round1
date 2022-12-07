
def fetch(dic):
	x=input("input string: ")

	if x in dic.keys():
		print("Social links -")
		print(dic[x.strip()][1])
		print(dic[x.strip()][2])
		print("Email/s-")
		print(dic[x.strip()][3])
		print("Contact:")
		print(dic[x.strip()][4])
	else:
		print("no data found")
		return

def write(dic):
	name=input("name: ").strip()
	facebook=input("facebook: ").strip()
	linkdin=input("linkdin: ").strip()
	email=input("email: ").strip()
	contact=input("contact: ").strip()
	if len(name) == 0 and len(facebook) == 0 and len(linkdin) == 0 and len(email) == 0 and len(contact) == 0:
		print("invalid input")
	else: 
		dic[name] = [name, facebook, linkdin, email, contact]
		s=""
		for key in dic:
			list = dic[key]
			s=s+"\n".join(list).strip()+"\n"
		f = open('test.txt', 'w+')
		f.write(s)
		f.close()


f = open('test.txt', 'r')
Lines = f.readlines()
  
dic={}
i=0
x=["","","","",""]
for line in Lines:
	x[i]=line.strip()
	i+=1
	if i==5:
		i=0
		dic[x[0]]=x
		x=["","","","","",""]
	
f.close()

option = int(input("select option 1. fetch data  2. write data: "))
if option == 1:
	fetch(dic)
else:
	write(dic)