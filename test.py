#!/usr/bin/python

import docker
import pprint
import json
from urllib2 import urlopen, Request, HTTPError, URLError    

client = docker.APIClient(base_url='unix://var/run/docker.sock')
client_env = docker.from_env()#!/usr/bin/python


running_containers = client_env.containers.list()
print(running_containers)

for i in running_containers:
    stats = i.stats(stream=False)

    stats = json.dumps(stats, indent=4, sort_keys=True)
    slack_message = {"channel": '#stuffdansays', "username": 'DockBot', "text": stats, "icon_emoji": ':whale:'}

    req = Request('https://hooks.slack.com/services/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', json.dumps(slack_message).encode("utf-8"))
try:
    response = urlopen(req)
    response.read()
except HTTPError as e:
    print(repr(e))
except URLError as e:
    print(repr(e))
