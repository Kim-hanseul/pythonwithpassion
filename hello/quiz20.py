import random
import threading
import urllib.request

import hello
from hello import Quiz00
from hello.domains import myRandom
from hello.domains import myMembers



from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

class Quiz20:

    def quiz20list(self) -> str: return None

    def quiz21tuple(self) -> str: return None

    def quiz22dict(self) -> str: return None

    def quiz23listcom(self) -> str:
        print('----legacy----')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('----comprehension----')
        a2 = [i for i in range(5)]
        print(a2)
        return None


    def quiz24zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml') # html.parser vs lxml
        ls1 = self.find_music(soup, 'title')
        ls2 = self.find_music(soup, 'artist')
        dt = {i:j for i, j in zip(ls1, ls2)}
        l = [i + j for i,j in zip(ls1, ls2)]
        # l2 = list(ls1,ls2)
        d1 = dict(zip(ls1, ls2))
        '''
        a = [i if i==0 or i==0 else i for i in range(1)]
        b = [i if i ==0 or i==0 else i for i in[]]
        c = [(i,j) for i,j in enumerate([])]
        d = {i:j for i,j in zip(ls1,ls2)}
        e = [i + j for i,j in zip(ls1,ls2)]
        '''
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        # self.dict3(ls1, ls2)
        print(d1)
        return dt

        ''' for i in ['artist','title']:
            print(''.join(i for i in self.bugs(soup, i))) '''
            #b= [i for i in self.bugs(soup, i)]
            #print(''.join(i for i in b))

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i,j in enumerate(ls1):
            dict[j] = ls2[i]


    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[i] = ls2[i]
        print(dict)


    def print_music_list(self,soup):
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))


    def find_rank(self,soup):
        for i,j in enumerate(['artist','title']):
            for i, j in enumerate(self.find_music(soup, j)):
                print((f'{i}위 : {j}'))
            print('#'*100)


    @staticmethod
    def bugs(soup, a) -> str:
        songinf = soup.find_all('p', {'class': a})
        songinf = [i.get_text() for i in songinf]
        # print(''.join(i for i in songinf))
        return songinf

    @staticmethod
    def find_music(soup, cls_nm) -> []:
        ls = soup.find_all('p', {'class': cls_nm})
        return [i.get_text() for i in ls]
        # return [i.get_text() for i in soup.find_all('p', {'class' : cls_nm})]

    def quiz25dictcom(self) -> str :
        # students = random.sample(myMembers(), 5)
        q = Quiz00()
        a = set([q.quiz06member_choice() for i in range(5)])
        while len(a) != 5:
            a.add(q.quiz06member_choice())
        students = list(a)
        scores = [myRandom(0,101) for i in range(5)]
        b = {i:j for i,j in zip(students, scores)}
        print(f'result : {b}')
        return None


        # return myMembers()[myRandom(0,23)]
        # studentslist = random.sample(students, 5)
        # scores = [myRandom(0,101) for i in range(5)]
        # res = dict(zip(a, scores))
        # print(res)
        # return None

    @staticmethod
    def find_grade(ls4, scores) -> None:
        dict = {}
        for i, j in enumerate(ls4):
            dict[j] = f'{scores[i]} 점'
        print(dict)

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent' : 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        melon_title = soup.find_all('div', {'class' : 'ellipsis rank01'})
        melon_title = [i.get_text() for i in melon_title]
        ms1 = self.find_music(soup, 'ellipsis rank01')
        print(''.join(i for i in melon_title))

        return None

    def quiz28dataframe(self) -> str:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')

        return None

        ''' 
        다음 결과 출력
            a   b   c
        1   1   3   5
        2   2   4   6
        '''
    def quiz29_pandas_df(self) -> str:
        d = []
        d1 = []
        columns = [chr(i) for i in range(97,100)]
        e = [d.append(i) if i%2 == 0 else d1.append(i) for i in range(1,7)]
        df = {'1' : d, '2': d1}
        frame = pd.DataFrame.from_dict(df, orient='index', columns=columns)
        # [i if (i,j) for i,j in enumerate([])]
        # df3 = pd.DataFrame.from_dict(d2, orient='index', columns=c)
        print(frame)
