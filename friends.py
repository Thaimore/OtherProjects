import json
import datetime
import requests


def calc_age(uid):
    bday = []
    result_days = []
    sec = []
    req = requests.get(
        f'https://api.vk.com/method/friends.get?v=5.71&access_token=317af5ee07f47e684933546f3bc2efed27bdbd5d86c60a4411f31fcd401518b7632a683ac5d54a23aab75&user_ids={uid}&fields=bdate')
    current_year = datetime.datetime.now().year
    req_text = req.text
    req_text = json.loads(req_text)
    for item in req_text['response']['items']:
        try:
            items = item['bdate'].split('.')
            if len(items) == 3:
                bday += [current_year - int(items[2])]
        except:
            continue
    for day in bday:
        if day not in sec:
            result_days += [(day, bday.count(day))]
            sec += [day]
    return sorted(result_days, key=lambda x: (x[1], -x[0]), reverse=True)


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
