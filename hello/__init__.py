from hello.domains import Member
from hello.models import Quiz01Calculator, Quiz02Bmi, Quiz03Grade, Quiz05Dice, Quiz07RandomChoice, Quiz08Rps, \
    Quiz10LeapYear, Quiz11NumberGolf, Quiz12Lotto, Quiz13Bank, Quiz14Gugudan, Quiz09GetPrime

if __name__ == '__main__':

    while 1:
        menu = input('############################################################################\n'
                     '# 0. Exit 1. Calculator 2. Bmi 3. Grade 5. Dice 6. Random num pick         #\n'
                     '############################################################################\n'
                     '# 7.Random person pick 8. rps 9. prime number 10. Luna year 11. Golf game  #\n'
                     '############################################################################\n'
                     '# 12. Lotto pick 13. bank machine 14. gugudan                              #\n'
                     '############################################################################\n')

        if menu == 0:
            break
        if menu == '1': # 계산기
            q1 = Quiz01Calculator(int(input('first num')), input('opcode'), int(input('second num')))
            print(f'{q1.num1} {q1.op} {q1.num2} = {q1.res()}')
        elif menu == '2': #BMI
            member = Member()
            q2 = Quiz02Bmi
            member.name = input('name : ')
            member.height = float(input('height : '))
            member.weight = float(input('weight : '))
            res = q2.getBmi(member)
            print(f'name : {member.name}, height : {member.height}, '
                  f'weight : {member.weight}, Bmi status : {res} ')
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
            q8 = Quiz08Rps()  # 가위 1 바위 2 보 3
            print({q8.game()})
        elif menu == '9':
            q9 = Quiz09GetPrime()
            print(f'{q9.prime()}')
        elif menu == '10':
            q10 = Quiz10LeapYear(int(input('year')))
            print(f'{q10.leap()}')
        elif menu == '11':
            q11 = Quiz11NumberGolf()
            print(f'{q11.golf()}')
        elif menu == '12':
            q12 = Quiz12Lotto()
            print(f'{q12.lotto}')
        elif menu == '13':
            q13 = Quiz13Bank()
            print(f'{q13.bank()}')
        elif menu == '14':
            q14 = Quiz14Gugudan()
            print(f'{q14.gugudan()}')