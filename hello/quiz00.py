from hello import Member
from hello.domains import my100, myRandom, myMembers


class Quiz00:
    def quiz00calculator(self) -> float:
        a = my100()
        b = my100()
        o = ['+', '-', '*', '/', '%']
        op = o[myRandom(0, 4)]
        if (op == '+'):
            print(f' {a} {op} {b} = {self.add(a, b)}')
        elif (op == '-'):
            print(f' {a} {op} {b} = {self.sub(a, b)}')
        elif (op == '*'):
            print(f' {a} {op} {b} = {self.mul(a, b)}')
        elif (op == '/'):
            print(f' {a} {op} {b} = {self.div(a, b)}')
        elif (op == '%'):
            print(f' {a} {op} {b} = {self.mod(a, b)}')

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        this = Member()
        this.name = '홍길동'
        this.height = 170.8
        this.weight = 120.8
        res = this.weight / (this.height * this.height) * 10000
        if res > 25:
            print(f'{this.name}, {this.height}, {this.weight} = 비만')
        elif res > 23:
            print(f'{this.name}, {this.height}, {this.weight} = 과체중')
        elif res > 18.5:
            print(f'{this.name}, {this.height}, {this.weight} = 정상')
        else:
            print(f'{this.name}, {this.height}, {this.weight} = 저체중')

    def quiz02dice(self):
        print(myRandom(1, 6))

    def quiz03rps(self):
        com = myRandom(0, 2)
        player = int(input('0. rock 1. scissors 2. paper 3. 종료'))
        if player == 3:
            return 'exit'
        if player - com == 0:
            print(f' player : {player} com : {com} result : draw..')
        elif player - com == 1 or player - com == -2:
            print(f' player : {player} com : {com} result : lose :( ')
        elif com - player == 2 or player - com == -1:
            print(f' player : {player} com : {com} result : win! ')
        else:
            print('wrong number')

    def quiz04leap(self):
        y = myRandom(2000, 2022)
        '''
        s1 = "윤년" if y % 4 == 0 and y % 100 != 0 else "평년"
        s2 = "윤년" if y % 400 == 0 else "평년"
        Java style ==> String s = : () ? : ;
        s = (y%4==0 && y % 100 !=0) ? "윤년" : (y%400==0) ? "윤년" : "평년";
        Python style ==> s = "" if else ""
        s = "윤년" if y % 4 == 0 and y % 100 != 0 or y % 400 ==0 else "평년"
        '''
        s = "윤년" if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else "평년"

        print(f' {y} 년은 {s} 입니다.')

    def quiz05grade(self):
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        total = kor + eng + math
        avg = total / 3
        if avg >= 80:
            grade = 'pass'
        else:
            grade = 'fail'

        return print(f'** kor grade : {kor}\n '
                     f'** eng grade : {eng}\n'
                     f'** math grade : {math}\n'
                     f'** total grade : {total}\n'
                     f'** avg = {avg}\n'
                     f'** pass or fail = {grade}')

    def quiz06memberChoice(self):
        members = myMembers()
        return print(members)


    def quiz07lotto(self):
        pass

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        Account().main

        '''
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
                    total = total - output
                    print(f'인출금액: {output}\n 잔액: {total}')
                elif total < output:
                    print('잔액이 부족합니다.')
            elif menu == 3:
                inp = int(input('입금하실 금액'))
                total = inp + total
                print(f'입금 금액:{inp} 잔액:{total}')
            '''


    def quiz09gugudan(self):  # 책받침구구단
        res = ""
        for i in [2, 6]:
            for j in range(1, 10):
                for k in range(0, 4):
                    res += f'{i + k} * {j} = {(i + k) * j}\t'
                res += '\n'
            res += '\n'
        print(res)



'''
은행이름은 Bitbank
입금자 이름(name), 계좌번호(acc_num), 금액(money) 속성 값으로 계좌를 생성 한다.
계좌번호는 3자리-2자리-6자리 형태로 이루어져 있음 (랜덤하게 생성)
ex : 123-12-123456
금액은 100만원 ~ 999만원 사이로 랜덤하게 입금된다.
'''


class Account(object):
    def __init__(self, acc_num, money):
        self.BANK_NAME = 'Bitbank'
        self.name = myMembers()
        # self.acc_num = f'{str(myRandom(0,999)).rjust(3,"0")}-{str(myRandom(0,99)).rjust(2,"0")}-{str(myRandom(0,99999)).rjust(5,"0")}' #
        self.acc_num = self.create_acc_numb()
        self.money = myRandom(100, 1000)

    def to_string(self):
        return f'** 은행 : {self.BANK_NAME}\n' \
               f'** 입금자 : {self.name}\n' \
               f'** 계좌번호 : {self.acc_num}\n' \
               f'** 금액 : {self.money} 만원'

    @staticmethod
    def create_acc_numb():
        '''
        ls = []
        ls += [str(myRandom(0, 10)) for i in range(3)]
        ls.append("-")
        ls += [str(myRandom(0, 10)) for i in range(2)]
        ls.append("-")
        ls += [str(myRandom(0, 10)) for i in range(6)]
        return "".join(ls)
        '''
        return ''.join("-" if i==3 or i==6 else str(myRandom(0,10)) for i in range(13))

    def del_account(self, ls, acc_num):
        for i,j in enumerate(ls):
            if j.acc_num == acc_num:
                del ls[i]


    def main(self):
        ls = []
        while 1:
            menu = input('0. 종료 1. 계좌개설 2. 계좌정보 3. 입금 4. 출금 5. 계좌해지')
            if menu == '0':
                break
            if menu == '1':
                acc = Account()
                print(f'{acc.to_string()} ... 개설 되었습니다. ')
                ls.append(acc)
            elif menu == '2':
                a = ''.join(i.to_string() for i in ls)
                print(a)
            elif menu == '3':
                acc_numb = input('입금할 계좌번호')
                deposit = input('입금액')
                for i, j in enumerate(ls):
                    if j.acc_num == acc_numb:
                       replace =


            elif menu == '4':
                acc_numb = input('출금할 계좌번호')
                money = input('출금액')
                # 추가 코드 완성
            elif menu == '5':
                acc_numb = input('탈퇴할 계좌번호')
            else:
                print('wrong number. try again')
                continue



