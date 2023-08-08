import vk_api
from vk_api.longpoll import VkLongPoll
import requests
from vk_api.upload import VkUpload
from datetime import date
from BD import add_user
from config import vk_token, my_vk_token
from pprint import pprint



my_vk_token = 'vk1.a.u7bFzy6gtq7feV3_Ojm8lxFbn1RVHEJgVP7D4eYglAfTRoRoBBWlvg4elxV9oZIQ6pZc2VD4D01yDrIxdPMV0EyahZQC_OVd2c3OXEKV6acXl4-gi4eCMOfr7DESErZsiO-wG_wronaI_e5CClZq1kgEpcJhjvB7ejJwLa6fFLXjUiJJBWblNc8AVNa3lczDfJP3enozdRCMllAqywxfdw'
vk_token = 'vk1.a._0ZncLWb3CSLzETNzUmSNwGhk5eqaTfy_V8DUrUZCdnJozvpKTqN6wSskvoV14Lxtn2kA4K_4_n3Wy_ce1jtXaLavVf7O9KYb4erW_HEcIfrm6Ds2XnKzqg_X92XuPS5_ke182mHlZTgwjJQa_0cM6oByflWdSvKFjb235-KSXjxezHiJdHMADs83b6rrCTQZ-6ibBUEB3mHHOKM-fUplw'


params = {
        'owner_id': 185876158,
        'album_id': 'profile',
        'access_token': my_vk_token,
        'extended': 1,
        'photo_sizes': 0,
        'offset': 20,
        'count': 10,
        'v': 5.131
    }

response = requests.get('https://api.vk.com/method/photos.get', params=params)
array_photos = response.json()['response']['items']

pprint(array_photos)