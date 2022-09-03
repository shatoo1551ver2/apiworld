# import requests



# headers = {'X-Api-Key': 'API Key 文字列'}
# url = 'https://newsapi.org/v2/everything'
# params = {
#     'q': 'コロナウイルス AND ワクチン',
#     'sortBy': 'publishedAt',
#     'pageSize': 100
# }

# response = requests.get(url, headers=headers, params=params)
# print(response)

# print(response.json())

# import pandas as pd
# pd.options.display.max_colwidth = 25

# if response.ok:
#     data = response.json()
#     df = pd.DataFrame(data['articles'])
#     print('totalResults:', data['totalResults'])

# print(df[[ 'publishedAt', 'title', 'url']])


# def apido(data):
#     response = requests.get(url, headers=headers, params=params)
#     datas = [data]
#     with open(os.getcwd()+'/myapp/application/'+'data.csv','a') as f:
#         writer = csv.writer(f, lineterminator='\n')
#         writer.writerow(datas)