import random

class distributions:

    @staticmethod
    def custom_30_70():
        '''
        static method to return 0 or 1, with 30% and 70% chance (on average) respectively
        '''
        return(round((1+2*random.random())/3.25))

    @staticmethod
    def custom_10_90():
        '''
        static method to return 0 or 1, with 10% and 90% chance (on average) respectively
        '''
        return(round((1+random.random())/2.18))
