import json

with open('/content/drive/My Drive/Colab Notebooks/24-25Mar.jsonl', 'r') as json_file:
    json_list = list(json_file)

temp= []
for i in json_list:
  if i != '\n':
    temp.append(i)
json_list= temp

result={}
k=0
try:
  while k < len(json_list):
      if json.loads(json_list[k])['user']['location'].split(",")[-1] == 'India':
        result[str(k)] = json.loads(json_list[k])
      k+=1
except:
  pass
