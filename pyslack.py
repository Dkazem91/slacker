#!/usr/bin/python

import docker
import pprint
import json
from urllib2 import urlopen, Request, HTTPError, URLError

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

    slack_message = {"channel": '#stuffdansays', "username": 'DockBot', "text": 'CPU Memory Usage: ' +  percentage + '%', "icon_emoji": ':whale:'}

    req = Request('https://hooks.slack.com/services/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', json.dumps(slack_message).encode("utf-8"))
try:
    response = urlopen(req)
    response.read()
except HTTPError as e:
    print(repr(e))
except URLError as e:
    print(repr(e))
