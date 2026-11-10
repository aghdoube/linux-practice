cloud_servers = [
    {"name": "web01", "cpu": 45},
    {"name": "db01", "cpu": 98},
    {"name": "api01", "cpu": "invalid_data"},  
    {"name": "web02", "cpu": 12}
]







def monitor_servers(server_list):
    for server in server_list:
        try:
           
            if server["cpu"] > 90:
                print(f"Server {server['name']} is CRITICAL!")
            else:
                print(f"Server {server['name']} is healthy.")
        except TypeError:
            print(f"Server {server['name']} has invalid data!")

monitor_servers(cloud_servers)
