from icecream import ic
from context.models import Model
from context.domains import Dataset



class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Surivived']
        this.train = this.train.drop('Survived', axis=1)
        this.test = this.test.drop('Survived', axis=1)
        # Entity 에서 Object 로 변환
        this = self.drop_feature(this)
        '''
        this = self.create_train(this)
        this = self.embarked_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.name_nominal(this)
        this = self.sex_nominal(this)
        this = self.age_ratio(this)
        this = self.fare_ratio(this)
        '''
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        ic(f'1. train 의 type : {type(this.train)}\n')
        ic(f'2. train 의 column : {this.train.columns}\n')
        ic(f'3. train 의 상위 1개 : {this.train.head(1)}\n')
        ic(f'4. train 의 null의 개수 : {this.train.isnull().sum()}\n')
        ic(f'5. test 의 type : {type(this.test)}\n')
        ic(f'6. test 의 column : {this.test.columns}\n')
        ic(f'7. test 의 상위 1개 : {this.test.head(1)}\n')
        ic(f'8. train 의 null의 개수 : {this.test.isnull().sum()}\n')
        ic(f'9. id 의 타입 : {type(this.id)}\n')
        ic(f'10. id 의 상위 10개 : {this.id[:10]}\n')


    def create_this(self, dataset)->object:
        this = dataset
        this.train = self.train
        this.test = self.test
        this.id = self.id
        return this


    @staticmethod
    def create_train(this) -> object:
        return this
    @staticmethod
    def drop_feature(this, *feature) -> object:
        feature = ['Cabin', 'Parch', 'Ticket', 'SibSp']
        this.train = [this.train.drop(i, axis=1) for i in feature]
        this.test = [this.test.drop(i, axis=1) for i in feature]
        [this.drop([*feature], axis=1, inplace=True) for i in [*feature]]

        '''
        self.cabin_garbage(df)
        self.parch_garbage(df)  
        self.ticket_garbage(df)
        self.sib_sp_garbage(df)
        '''
        return this

    '''
    Categorical vs. Quantitative
    Cate -> nominal (이름) vs. ordinal (순서)
    Quan -> interval (상대) vs. ratio (절대)
    '''

    @staticmethod
    def pclass_ordinal(df) -> object:
        return df

    @staticmethod
    def name_nominal(df) -> object:
        return df

    @staticmethod
    def age_ratio(df) -> object:
        return df

    @staticmethod
    def sex_nominal(df) -> object:
        return df

    @staticmethod
    def embarked_nominal(df) -> object:
        return df

    @staticmethod
    def fare_ratio(df) -> object:
        return df
