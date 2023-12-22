import requests
import json

TOKEN = ('vk1.a.5uo2UiTqlqhs31azkJkqhNSVMtMM5QV5bgIkjEC4tllEpng5TMgjdO32TZglIT5qSrT9ULkhfGaMNIb6my61t5wVqo9ymGiOLIu-soP'
         'uWxNw4pMjU1i7VtAz3-i0PjOgifqM8QlG9R6Vm6INeXjWZRejNrOLp2uPHg7K9PaOclLpUJ8T7QOwCjeQujI3P91lk9vVJYd-f_C_nI_0_kFXwA')

session = requests.Session()

user_id = 155379
class getUsersInfo():
    r = session.get('https://api.vk.com/method/users.get', params={
        'access_token': TOKEN,
        'v': 5.154,
        'lang': 0,
        'user_ids': user_id,
        'fields': 'bdate, city',
    })

    dataGetUsers = r.json()
    with open('userInfo.json', 'w', encoding='utf8') as f:
        json.dump(dataGetUsers, f, indent=2, ensure_ascii=False)

    first_name = dataGetUsers['response'][0]['first_name']
    last_name = dataGetUsers['response'][0]['last_name']
    id = dataGetUsers['response'][0]['id']
    # bdate = dataGetUsers['response'][0]['bdate']
    # city = dataGetUsers['response'][0]['city']['title']
    bdate = dataGetUsers.get('bdate', '')
    city = dataGetUsers.get('city', '')

class getFriends():
    r = session.get('https://api.vk.com/method/friends.get', params={
        'access_token': TOKEN,
        'v': 5.154,
        'lang': 0,
        'user_id': user_id,
    })

    dataGetFriends = r.json()
    with open('friends.json', 'w', encoding='utf8') as f:
        json.dump(dataGetFriends, f, indent=2, ensure_ascii=False)

    countFriends = dataGetFriends['response']['count']

class getAlbumCounts():
    r = session.get('https://api.vk.com/method/photos.getAlbums', params={
        'access_token': TOKEN,
        'v': 5.154,
        'lang': 0,
        'owner_id': user_id,
    })

    dataAlbumCounts = r.json()
    AlbumCounts = dataAlbumCounts['response']['count']