import random
import threading
import urllib.request

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
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)
        return dict


        ''' for i in ['artist','title']:
            print(''.join(i for i in self.bugs(soup, i))) '''
            #b= [i for i in self.bugs(soup, i)]
            #print(''.join(i for i in b))
        return None

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

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent' : 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        melon_title = soup.find_all('div', {'class' : 'ellipsis rank01'})
        melon_title = [i.get_text() for i in melon_title]
        print(''.join(i for i in melon_title))

        return None

    def quiz28dataframe(self) -> str:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        #a = [i if i==0 or i==0 else i for i in range()]
        #b = [i if i==0 or i==0 else i for i in[]] #iterator
        #c = [(i,j) for i,j in enumerate([])] #enumeration
        return None

    def quiz29(self) -> str: return None