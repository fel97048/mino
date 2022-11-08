# coding: utf-8

import datetime

class MouIkutsuNerutoOshogatsu:
    def answer(self, today=None):
        if today is None:
            today = datetime.date.today()

        if (today.month == 1 and today.day in range(1, 4)):
            return 0

        oshogatsu = datetime.date(today.year + 1, 1, 1)
        delta = oshogatsu - today

        return delta.days

def main():
    mino = MouIkutsuNerutoOshogatsu()
    h = mino.answer()
    print("あと{0}回寝るとお正月です。".format(h))

if __name__ == '__main__':
    main()