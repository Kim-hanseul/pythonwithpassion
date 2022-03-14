import random
import string

import pandas as pd
from icecream import ic
import numpy as np
from domains import myMembers
from domains import myRandom
from titanic.models import Model


class Quiz30:
    '''
        데이터프레임 문제 Q02
    ic| df:     A   B   C
            1   1   2   3
            2   4   5   6
            3   7   8   9
            4  10  11  12
    '''
    def quiz30_df_4_by_3(self) -> str:
        d = {'1' : range(1,4), '2' : range(4,7), '3' : range(7,10), '4' : range(10,13)}
        df2 = pd.DataFrame.from_dict(d, orient="index", columns=['A', 'B', 'C'])
        ic(df2)
        return None



        df = pd.DataFrame([[1,2,3],
                          [4,5,6],
                          [7,8,9],
                          [10,11,12]], index=range(1,5), columns=['A','B','C'])
        # 위 식을 리스트 결합 형태로 분해해서 조립하시오

        ic(df2)
        return None
    def quiz31_rand_2_by_3(self) -> str:
        # l1 = [[myRandom(10,100) for i in range(3)] for i in range(2)]
        # l2 = [i for i in range(2)]
        df = pd.DataFrame(np.random.randint(10, 100, size=(2,3)))
        ic(df)
        return None


        '''
                데이터프레임 문제 Q03.
                두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
                ic| df:     0   1   2
                        0  97  57  52
                        1  56  83  80
                '''
        return None

    '''
                       데이터프레임 문제 Q04.
                       국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
                        단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기

                         ic| df4:        국어  영어  수학  사회
                                   lDZid  57  90  55  24
                                   Rnvtg  12  66  43  11
                                   ljfJt  80  33  89  10
                                   ZJaje  31  28  37  34
                                   OnhcI  15  28  89  19
                                   claDN  69  41  66  74
                                   LYawb  65  16  13  20
                                   QDBCw  44  32   8  29
                                   PZOTP  94  78  79  96
                                   GOJKU  62  17  75  49
               '''
    @staticmethod
    def id(chr_size) -> str: return ''.join([random.choice(string.ascii_letters) for i in range(5)])
    def col(self) -> str: return ['국어', '영어', '수학', '사회']
    def quiz32_df_grade(self) -> object:
        # cho = [[random.choice(string.ascii_letters) for i in range(5)] for i in range(10)]
        # data1 = [[np.random.randint(0,100) for i in range(4)] for i in range(10)]
        data1 = np.random.randint(0,100, (10,4))
        idx = [self.id(chr_size=5) for i in range(10)]
        df1 = pd.DataFrame(data1, index=idx, columns=self.col())
        data2 = {i:j for i,j in zip(idx, data1)}
        df2 = pd.DataFrame.from_dict(data2, orient='index', columns=self.col())
        ic(df1)
        ic('*' * 100)
        ic(df2)

        return None
    #(''.join([myRandom(0,101) for i in range(4)]) for i in range(10))


    def quiz33_df_loc(self) -> str:
        '''subjects = ['a', 'b', 'c', 'd']'''
        # df = pd.DataFrame([{i: j for i, j in zip(['a', 'b', 'c', 'd'], np.random.randint(0,100,4))} for _ in range(3)])
        '''df = self.creatDf(keys=['a','b','c','d'],
                          vals=np.random.randint(0,100,4),
                          len=3)'''
        # ic(temp)


        # stud = myMembers()
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
        # grade.csv
        model = Model()
        grade_df = model.new_model('grade.csv')
        ic(grade_df)

        d = np.random.randint(0,100, (24,4))
        idx = myMembers()
        col = ['자바', '파이썬', '자바스크립트', 'SQL']
        df1 = pd.DataFrame(d, index=idx, columns=col)
        ic(df1)
        df1.to_csv('./save/grade.csv', sep=',', na_rep='NaN')
        '''
        ic| df2:      자바  파이썬  자바스크립트  SQL
         홍정명  74   49      93   48
         노홍주  96   22      42   44
         전종현  24   33      75   51
         정경준  14   11      29   81
         양정오  75   68      49   88
         권혜민  25   26      49   45
         서성민  12   22      64   54
         조현국  41    0      67   84
         김한슬  91   61      91   33
         김진영  37   71      76   18
         심민혜   7   72       0   96
         권솔이  62   28      65    3
         김지혜  76   36      67   58
         하진희  16   75      25   37
         최은아  11   46       1   45
         최민서   6   51      58   57
         한성수  51   41      15   33
         김윤섭  32   72      65   44
         김승현  77    1      62   96
         강 민  53   14      19   35
         최건일  25   59      48   12
         유재혁  18   27      38    7
         김아름  37   44      57   37
         장원종  29   34      58   19
        '''


        #df = pd.DataFrame([{i: j for i, j in zip(['자바', '파이썬', '자바스크립트', 'SQL'], np.random.randint(0, 100, 4))} for _ in range(3)])
        return None




        return None
    @staticmethod
    def creatDf(keys, vals, len):
        return pd.DataFrame([dict(zip(keys,vals)) for _ in range(len)])

    def quiz34_df_iloc(self) -> str:
        # ic(df.iloc[0])
        '''
        ic| df.iloc[0]: a    56
                b    86
                c    19
                d    85
                Name: 0, dtype: int32
        '''
        # ic(df.iloc[[0]])
        '''
        ic| df.iloc[[0]]:     a  b   c   d
                            0  42  1  58  57
        '''
        # ic(df.iloc[[0,1]])
        '''
        ic| df.iloc[[0,1]]:     a   b  c   d
                            0  23  86  7  31
                            1  23  86  7  31
        '''
        # ic(df.iloc[:3])
        '''
        ic| df.iloc[:3]:     a   b  c   d
                        0  38  53  6  95
                        1  38  53  6  95
                        2  38  53  6  95
        '''
        # ic(df.iloc[[True, False, True]])
        '''
        ic| df.iloc[[True, False, True]]:    a  b   c   d
                                            0  1  2  49  22
                                            2  1  2  49  22
        '''
        # ic(df.iloc[lambda x: x.index % 2 == 0])
        '''
        ic| df.iloc[lambda x: x.index % 2 == 0]:     a   b   c   d
                                                0  29  48  64  28
                                                2  29  48  64  28
        '''
        # ic(df.iloc[0,1])
        ''' ic| df.iloc[0,1]: 86 - 좌표값'''

        # ic(df.iloc[[0,2],[1,3]])
        '''ic| df.iloc[[0,2],[1,3]]:     b   d
                                    0  72  16
                                    2  72  16 '''

        # ic(df.iloc[:, [True, False, True, False]])
        '''ic| df.iloc[:, [True, False, True, False]]:     a   c
                                                        0  26  30
                                                        1  26  30
                                                        2  26  30'''

        # ic(df.iloc[:, lambda df: [0, 2]])
        '''ic| df.iloc[:, lambda df: [0, 2]]:     a  c
                                            0  68  2
                                            1  68  2
                                            2  68  2'''

        return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None