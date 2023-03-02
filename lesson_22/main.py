# import json
# writeF = open("file.json", "w", enconding="utf-8")
# # writeF.write("True")
# content = [None, True (1, 2, 3),  [1, 2, 3], "hello", "прифки"]
# json.dump(content, writeF, ensure_ascii=False)
# writeF.close

# readF = open("file.json", 'r', enconding="utf-8")
# # print(readF.read())
# print(json.load(readF))
# readF.close()


# Задача 1
# import json
#
# readF = open("file.txt", "r", encoding="utf-8")
# content = readF.readlines()
# readF.close
# print(content)
# for record in content:
#     splited = record.split(": ")
# print(content)
# d = {}
# for record in content:
#     splited = record.split(": ")
#     d[splited[0]] = splited[1].rstrip()
# print(d)
#
# f = open("file.json", "w", enconding="utf-8")
# json.dump(d, f, ensure_asclii=False)
# f.close()

# import requests
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# data = response.json()["iss_position"]
# print(f"Широта:{data['latitude']}. Долго, да: {data['longitude']}")






































