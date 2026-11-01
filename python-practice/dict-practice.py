server = {"name": "web1", "port": 80}

server["port"] = 8080
server["os"] = "ubuntu"
del server["name"]


for key in server:
	if server[key] == 8080:
		print("port is :",server[key])
print("Finished")


stock = {"apples": 5, "pears": 0, "plums": 12}

for fruit in stock:
	if stock[fruit] == 0:
		print(fruit)

for fruit in stock:
	if stock[fruit] > 3:
		print(fruit)



line = "db2,5432,debian"

parts = line.split(",")

print(f"Server {parts[0]} uses {parts[2]} on port {parts[1]}")

