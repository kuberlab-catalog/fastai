from mlboardclient.api import client
import sys

data = ""
for line in sys.stdin:
    data += line

client.update_task_info({'#documents.report.html':data})
