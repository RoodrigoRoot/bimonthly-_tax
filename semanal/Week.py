class Weeks():

    MOTHLY_TOTAL_1 = 0
    MOTHLY_TOTAL_2 = 0

    def __init__(self, payments):
        self.payments = payments

    def __str__(self):
        return "Weeks"

    def sum_weeks(self):
        
        for i in range(self.payments):
           self.MOTHLY_TOTAL_1 += self.obtain_Monthly(i)
        return self.MOTHLY_TOTAL_1

    def obtain_Monthly(self, i):
        weekly=0
        weekly = float(
                        input("Total de la semana {}: ".format(str(i+1))))
        return  weekly

    def obtain_Monthly_2(self, i):

        self.WEEKLY_TOTAL += float(
            input("Total de la semana {}: ".format(str(i+1))))
        return 0
