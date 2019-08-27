import requests, json
github_url = 'http://hdfs-test04.yingzi.com:21000/api/atlas/v2/search/basic'
data = json.dumps({"query": "ods_bc_center_event","typeName": "hive_table"})
header = {'content-type': "application/json"}
r = requests.post(github_url, data, auth=('admin', '1qaz2WSX'),headers = header)
content = r.content


github_url = 'http://hdfs-test04.yingzi.com:21000/api/atlas/v2/lineage/c29d9bb8-9f75-4d08-937e-68133825f6d8'
r = requests.get(github_url,auth=('admin', '1qaz2WSX'))
content = r.content