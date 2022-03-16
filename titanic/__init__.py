#https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from titanic.views import TitanicView
from titanic.models import TitanicModel
from titanic.templates import TitanicTemplates
from context.domains import Dataset
from context.models import Model
from icecream import ic
if __name__ == '__main__':
    view = TitanicView()
    model = TitanicModel(train_fname='train.csv',
                         test_fname='test.csv')
    template = TitanicTemplates

    while 1:

        menu = input('0. exit 1. template 2. 전처리')
        if menu == '0':
            break

        elif menu == '1':
            print('#### 1. template ####')
            template = TitanicTemplates(train_fname='train.csv', test_fname='test.csv')
            break


        elif menu == '2':
            print('#### 2. 전처리 ####')
            model = TitanicModel(train_fname='train.csv', test_fname='test.csv')

            ic(template)
