import pandas as pd
from icecream import ic


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
        df = pd.DataFrame([[1,2,3],
                          [4,5,6],
                          [7,8,9],
                          [10,11,12]], index=range(1,5), columns=['A','B','C'])
        # 위 식을 리스트 결합 형태로 분해해서 조립하시오
        ic(df)
        return None

    '''
        데이터프레임 문제 Q03.
        두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df:     0   1   2
                0  97  57  52
                1  56  83  80
        
        
        
        
        '''

    def quiz31(self) -> str: return None

    def quiz32_df_grade(self) -> object: return None

    def quiz33(self) -> str: return None

    def quiz34(self) -> str: return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None