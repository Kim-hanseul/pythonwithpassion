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
    def game(self):
        while 1:
            com = myRandom(0, 2)
            player = int(input('0. rock 1. scissors 2. paper 3. 종료'))
            if player == 3:
                return 'exit'
            if player-com == 0:
                print(f' player : {player} com : {com} result : draw..')
            elif player-com == 1 or player-com == -2:
                print(f' player : {player} com : {com} result : lose :( ')
            elif com-player == 2 or player-com == -1:
                print(f' player : {player} com : {com} result : win! ')






class Quiz09GetPrime(object):
    def prime(self):
        a = int(input('최대값'))
        res = ''
        for i in range(2, a):
            num = 0
            for j in range(2, i + 1):
                if i % j == 0:
                    num += 1
            if num == 1:
                res += str(i) + '\t'
        return res


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
        self.lotto = random.sample(range(1, 45), 6)
        self.lotto.sort()


class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def bank(self):
        total = 100000
        while 1:
            menu = int(input('사용하실 메뉴를 선택해 주세요\n'
                  '0. 종료 1.잔액조회 2.현금인출 3.입금'))
            if menu == 0:
                return ('종료')
            if menu == 1:
                print(f'{total}')
            elif menu == 2:
                output = int(input('출금하실 금액'))
                if total >= output:
                    total = total-output
                    print(f'인출금액: {output}\n 잔액: {total}')
                elif total < output:
                    print('잔액이 부족합니다.')
            elif menu == 3:
                inp = int(input('입금하실 금액'))
                total = inp + total
                print(f'입금 금액:{inp} 잔액:{total}')


class Quiz14Gugudan(object): # 책받침 구구단
    def gugudan(self):
        res = ""
        for i in [2,6] :
            for j in range(1, 10):
                for k in range(0, 4):
                    res += f'{i + k} * {j} = {(i + k) * j}\t'
                res += '\n'
            res += '\n'
        return res


