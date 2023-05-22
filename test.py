import requests

key = "9sj5vLzGsJGBewFgf8ArMVs0ptNUPQVfhWy0gQv7akS9%2BzrGAs%2F%2B%2BQfu3o%2FGlMX3IM8vExev7ETu%2F0dNirxRpQ%3D%3D"

url = f'http://apis.data.go.kr/6260000/FoodService/getFoodKr?serviceKey={key}'
params = {
    'pageNo': '1',
    'numOfRows': '10',
    'resultType': 'json',
    # 'UC_SEQ': ''
}

response = requests.get(url, params=params)
print(response.content.decode('utf-8'))
