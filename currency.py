from decimal import Decimal
from bs4 import BeautifulSoup


def convert(amount, cur_from, cur_to, data, requests,):
    amount = float(amount)
    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={data}'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    if cur_from == 'RUR':
        find_money = soup.find(name='charcode', text=cur_to)
        if int(find_money.parent.nominal.text) != '1':
            decimal_convert = find_money.parent.value.text.split(',')
            decimal_convert = decimal_convert[0] + '.' + decimal_convert[1]
            decimal_convert = float(decimal_convert)
            find_value = decimal_convert / int(find_money.parent.nominal.text)
        else:
            decimal_convert = find_money.parent.value.text.split(',')
            decimal_convert = decimal_convert[0] + '.' + decimal_convert[1]
            decimal_convert = float(decimal_convert)
            find_value = decimal_convert
        end_value = amount / find_value
        number = Decimal(str(end_value))
        end_num = number.quantize(Decimal("1.0000"))
        return end_num
    elif cur_to == 'RUR':
        find_money = soup.find(name='charcode', text=cur_from)
        if int(find_money.parent.nominal.text) != '1':
            decimal_convert = find_money.parent.value.text.split(',')
            decimal_convert = decimal_convert[0] + '.' + decimal_convert[1]
            decimal_convert = float(decimal_convert)
            find_value = decimal_convert / int(find_money.parent.nominal.text)
        else:
            decimal_convert = find_money.parent.value.text.split(',')
            decimal_convert = decimal_convert[0] + '.' + decimal_convert[1]
            decimal_convert = float(decimal_convert)
            find_value = decimal_convert
        end_value = amount * find_value
        number = Decimal(str(end_value))
        end_num = number.quantize(Decimal("1.0000"))
        return end_num
    curr_money = soup.find(name='charcode', text=cur_from)
    find_money = soup.find(name='charcode', text=cur_to)
    if int(curr_money.parent.nominal.text) != 1:
        decimal_convert = curr_money.parent.value.text.split(',')
        decimal_convert = decimal_convert[0] + '.' + decimal_convert[1]
        decimal_convert = float(decimal_convert)
        curr_value = decimal_convert / int(curr_money.parent.nominal.text)
    else:
        decimal_convert = curr_money.parent.value.text.split(',')
        decimal_convert = decimal_convert[0] + '.' + decimal_convert[1]
        decimal_convert = float(decimal_convert)
        curr_value = decimal_convert
    if int(find_money.parent.nominal.text) != 1:
        decimal_convert = find_money.parent.value.text.split(',')
        decimal_convert = decimal_convert[0] + '.' + decimal_convert[1]
        decimal_convert = float(decimal_convert)
        find_value = decimal_convert / int(find_money.parent.nominal.text)
    else:
        decimal_convert = find_money.parent.value.text.split(',')
        decimal_convert = decimal_convert[0] + '.' + decimal_convert[1]
        decimal_convert = float(decimal_convert)
        find_value = decimal_convert
    end_value = (curr_value * amount) / find_value
    number = Decimal(str(end_value))
    end_num = number.quantize(Decimal("1.0000"))
    return end_num
