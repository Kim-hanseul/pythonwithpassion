import random





class Quiz01Calculator(object):

    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2



    def add (self):
        return self.num1 + self.num2

    def min (self):
        return self.num1 - self.num2

    def mul (self):
        return self.num1 * self.num2

    def div (self):
        return self.num1 / self.num2

    def rest (self):
        return self.num1 % self.num2

    def res(self):
             if self.op == '+':
                return self.add()
             elif self.op == '-':
                return self.min()
             elif self.op == '*':
                return self.mul()
             elif self.op == '/':
                return self.div()
             elif self.op == '%':
                return self.rest()
             else:
                return 'wrong message'

class Quiz02Bmi:
    @staticmethod
    def getBmi(member):
        this = member
        res =this.weight/(this.height*this.height)*10000
        if res <= 18.5:
            return '저체중'
        elif res <= 22.9:
            return '정상'
        elif res <= 24.9:
            return '과체중'
        elif res >= 25:
            return '비만'
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
            elif c == 3:
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
    def __init__(self, year):
        self.year = year
    def leap(self):
        y=self.year
        if (y % 4 == 0 and not y % 100 == 0 or y % 400 == 0):
            res='윤년'
        else:
            res='평년'
        return res


class Quiz11NumberGolf(object):
    def __init__(self):
        self.static = myRandom(0, 100)

    def golf(self):
        st = self.static
        print(st)
        while 1:
            se = int(input('number please'))
            if st == se:
                res = 'correct!'
                return res
            elif st > se:
                print('up!')
            elif st < se:
                print('down..')
            else:
                return 'wrong text'



class Quiz12Lotto(object):
    def __init__(self):
        pass


class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass


class Quiz14Gugudan(object): # 책받침 구구단
    def __init__(self):
        pass


