from datetime import datetime, timedelta
from collections import defaultdict

# users = ({'name': 'Jane', 'birthday': '20.02.2000'},
#          {'name': 'Mickael', 'birthday': '21.02.2000'},
#          {'name': 'Susanna', 'birthday': '25.02.2000'},
#          {'name': 'Jackson', 'birthday': '22.02.2000'},
#          {'name': 'Billy', 'birthday': '26.02.2000'},)


def check_b_day(b_day):
    current_day = datetime(2021, 2, 19)  # datetime.now().date()
    next_monday = current_day + timedelta(7) - timedelta(current_day.weekday())
    start_period = next_monday - timedelta(2)
    end_period = next_monday + timedelta(5)
    if start_period <= b_day <= end_period:
        return True
    return False


def group_list(b_list):
    b_dict = {}
    grouped_b_list = defaultdict(list)
    for i in b_list:
        group_f = i[:10]
        grouped_b_list[group_f].append(i[11:])

    for i in grouped_b_list:
        if datetime.strptime(i, '%Y-%m-%d').weekday() > 4:
            b_dict.setdefault('Monday', []).append(grouped_b_list[i])
        else:
            b_dict.setdefault(datetime.strptime(
                i, '%Y-%m-%d').strftime('%A'), []).append(grouped_b_list[i])
    return b_dict


def print_result(b_dict):
    result = ''
    for i in b_dict:
        result += i + ': '
        for m in b_dict[i]:
            result += m[0]
            if m[0] != b_dict[i][-1][0]:
                result += ', '
        result += '\n'
    print(result)


def congratulate(users):

    b_list = []

    for i in (i for i in users):

        b_day = datetime.strptime(i['birthday'], '%d.%m.%Y')

        curent_b_day = datetime(datetime.now().year, b_day.month, b_day.day)

        if check_b_day(curent_b_day):

            b_list.append(f'{curent_b_day.date()}:{i["name"]}')

    print_result(group_list(b_list))
