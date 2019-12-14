# coding: utf-8

import datetime

class MouIkutsuNerutoOshogatsu:
    def answer(self, today=datetime.date.today()):
        if (today.month == 1 and today.day in range(1, 4)):
            return 0

        oshogatsu = datetime.date(today.year + 1, 1, 1)
        delta = oshogatsu - today

        return delta.days

def execute(request):
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    mino = MouIkutsuNerutoOshogatsu()
    return str(mino.answer())

def main():
    mino = MouIkutsuNerutoOshogatsu()
    h = mino.answer()
    print("あと{0}回寝るとお正月です。".format(h))

if __name__ == '__main__':
    main()