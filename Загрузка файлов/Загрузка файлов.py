import requests
import os


def get_upload_server():
    params_vk = {
        'access_token': "ваш access_token(VK Admin)",
        'album_id': "id альбома",
        'group_id': "id группы",
        'v': 5.199
    }

    result = requests.get('https://api.vk.com/method/photos.getUploadServer', params=params_vk).json()
    return result['response']['upload_url']


def get_result(req):
    params_vk = {
        'access_token': "ваш access_token(VK Admin)",
        'album_id': req['aid'],
        'group_id': req['gid'],
        'server': req['server'],
        'photos_list': req['photos_list'],
        'hash': req['hash'],
        'v': 5.199
    }
    result = requests.get('https://api.vk.com/method/photos.save', params=params_vk).json()
    return result


def main():
    files = {
        'file1': open(os.path.join('static', 'img', 'error.png'), mode='rb'),
        'file2': open(os.path.join('static', 'img', 'kria.png'), mode='rb')
    }

    url = get_upload_server()
    req = requests.post(url, files=files).json()
    get_result(req)


if __name__ == '__main__':
    main()
