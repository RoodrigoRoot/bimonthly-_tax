class Weeks:


    def __init__(self, payments):
        self.__MOTHLY_TOTAL_1 = 0
        self.__MOTHLY_TOTAL_2 = 0
        self.payments = 
        

    def __str__(self):
        return "Weeks"

    def sum_weeks(self):
        if self.payments:
            print("Mes 1")
            for i in range(self.payments):
                self.__MOTHLY_TOTAL_1 += self.obtain_Monthly(i)
        else:
            raise ValueError("""No se ha asignado
                             el valor de los pagons mensuales del primer mes """)
            
        return self.__MOTHLY_TOTAL_1

    def sum_weeks_2(self):
        print("Mes 2")
        for i in range(self.payments):
           self.__MOTHLY_TOTAL_2 += self.obtain_Monthly(i)
        return self.__MOTHLY_TOTAL_2

    def obtain_Monthly(self, i):
        weekly = 0
        weekly = float(input("Total de la semana {}: ".format(str(i+1))))
        return weekly


