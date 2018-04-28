#!/usr/bin/python3



import docker



client = docker.APIClient(base_url='unix://var/run/docker.sock')
client_env = docker.from_env()

running_containers = client_env.containers.list()

for x in clients.stats(container.name, decode=True):
    print(x)
