import json 

try:

	with open("server.json", "r") as f:
		data = json.load(f)
		print(f"Server {data['server']} runs {data['os']} on port {data['port']}")

except FileNotFoundError:
	print("file not found")



