import docker
client = docker.APIClient(base_url='unix:///var/run/docker.sock')
client_env= docker.from_env()
run_cl = client_env.containers.list()
for x in run_cl:
    # print the streaming statistics
    for y in client.stats(x.name,decode=True):
        memUse = y['memory_stats']['usage']
        memLim = y['memory_stats']['limit']
        break
    a = float(memUse)
    b = float(memLim)
    percentage = '{0:.2f}'.format((a / b * 100))
    print(percentage)
