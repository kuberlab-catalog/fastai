from mlboardclient.api import client
import sys

with open(sys.argv[1], 'r') as in_file:
    data=in_file.read()
    client.update_task_info({'#documents.report.html':data})