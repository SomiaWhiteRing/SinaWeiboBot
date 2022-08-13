from random import randint

from func.Func import Func


class poemFunc(Func):
    def __init__(self, client, data_path):
        super().__init__(client, data_path, {})

    def func(self):
        res = open('../data/poem.txt', 'r',encoding='utf-8')
        # 从poem.txt中随机选取一行
        line = res.readlines()[randint(0, len(line) - 1)]
        # 把<br />替换成\n
        status = line.replace('<br />', '\n')
        # 打印出来
        print(status)
        self.client.post(status=status)
        self.log('Successfully post!')
