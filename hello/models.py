import random

def main():
    while 1:
        menu = input(' 0.Exit 1.Calculator 2. bmi 3. Grade 5.Dice 6. random num pick 7.random person pick 8. rps')
        if menu == 0:
            break
        if menu == '1': # 계산기
            q1 = Quiz01Calculator(int(input('first num')), int(input('second num')) )
            print(f'{q1.num1} {q1.op} {q1.num2} = {q1.res}')
        elif menu == '2': #BMI
            q2 = Quiz02Bmi((input('name')), float(input('height')), float(input('weight')))
            print(f'name : {q2.name}, height : {q2.height}, '
                  f'weight : {q2.weight}, Bmi status : {q2.getBmi()} ')
        elif menu == '3':
            q3 = Quiz03Grade(input('이름'), int(input('국어점수')), int(input('영어점수')), int(input('수학점수')))
            print(f'name: {q3.name} kor: {q3.kor} 점 eng: {q3.eng} 점 math: {q3.math} 점 total: {q3.total()}점 avg: {q3.avg()} pass: {q3.gradePass()}')

        elif menu == '4':
            pass
            """q4 = Quiz04GradeAuto()
            for i in []:
                print(i)
            kor = int(input('kor : '))
            eng = int(input('eng : '))
            math = int(input('math : '))"""

            #grade=Quiz03Grade(input('name'), int(input('kor grade')), int(input('eng grade')), int(input('math grade')))
        elif menu == '5':
            print(Quiz05Dice.cast())
        elif menu == '6':
            q6 = None
        elif menu == '7':
            q7 = Quiz07RandomChoice()
            print(q7.chooseMember())

        elif menu == '8':
            q8 = Quiz08Rps(1)  # 가위 1 바위 2 보 3
            print(q8.game())


class Quiz01Calculator(object):

    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def calc(self):
        self.add()
        self.sub()
        self.mul()
        self.div()
        self.rest()

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def rest(self):
        return self.num1 % self.num2

    def res(self):
       if self.op == '+':
           return self.add()

       elif self.op == '-':
           return self.sub()

       elif self.op == '*':
           return self.mul()

       elif self.op == '/':
           return self.div()

       elif self.op == '%':
           return self.rest()
       else:
           print('wrong type')

class Quiz02Bmi(object):

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def res(self):
        return self.weight / (self.height * self.height / 10000)

    def getBmi(self):
        if self.res() <= 18.5:
            return f'저체중'
        elif self.res() <= 22.9:
            return f'정상'
        elif self.res() <= 24.9:
            return f'과체중'
        elif self.res() >= 25:
            return f'비만'
        else:
            return 'wrong number'


class Quiz03Grade(object):

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total (self):
        return self.kor + self.eng + self.math

    def avg (self):
        return self.total()/3

    def getGrade(self):
        if self.avg() >= 90:
            return 'A'
        elif self.avg() >= 80:
            return 'B'
        elif self.avg() >= 70:
            return 'C'
        elif self.avg() >= 65:
            return 'D'
        elif self.avg() >= 60:
            return 'E'
        else:
            return 'F'

    def gradePass(self):
        if self.getGrade() == 'F':
            return '불합격'
        else:
            return '합격'


class Quiz04GradeAuto(object):
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

        def sum(self):
            return self.kor + self.eng + self.math

        def avg(self):
            return self.kor + self.eng + self.math / 3

        def pas(self):  # 60 이상 이면 합격
            if self.avg() >= 60:
                return 'pass'
            else:
                return 'fail'

        def chkPass(self):  # 60점 이상이면 합격
            pass


def myRandom(start, end):
    return random.randint(start, end)


class Quiz05Dice(object):
    @staticmethod
    def cast():
        return myRandom(1, 6)


class Quiz06RandomChoice(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def random(self):
        return myRandom(1, 6)


class Quiz07RandomChoice(object):
    def __init__(self): # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜' , '권솔이', '김지혜' , '하진희' , '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]

    def chooseMember(self):
        return self.members[myRandom(0, 23)]


class Quiz08Rps(object):
    def __init__(self, player):
        self.player = player
        self.computer = myRandom(1,3)

    def game(self):
        c = self.computer
        p = self.player
        # 1 가위 2  바위 3 보
        rps = ['가위', '바위', '보']
        if p == 1:
            if c == 1:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[0]}, 결과: 무승부'
            elif c == 2:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[1]}, 결과: 패배'
            elif c == '3':
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[2]}, 결과: 승리'
        elif p == 2:
            if c == 1:
                res = '승리'
            elif c == 2:
                res = '무승부'
            elif c == 3:
                res = '패배'
        elif p == 3:
            if c == 1:
                res = '패배'
            elif c == 2:
                res = '승리'
            elif c == 3:
                res = '무승부'
        else:
            res = '1~3 입력'

        return res





class Quiz09GetPrime(object):
    def __init__(self):
        pass


class Quiz10LeapYear(object):
    def __init__(self):
        pass


class Quiz11NumberGolf(object):
    def __init__(self):
        pass


class Quiz12Lotto(object):
    def __init__(self):
        pass


class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass


class Quiz14Gugudan(object): # 책받침 구구단
    def __init__(self):
        pass


if __name__ == '__main__':
    main()

