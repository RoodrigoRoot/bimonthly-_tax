class Months:
    def __init__(self, first_month, second_month):
        self.first_month = first_month
        self.second_month = second_month
        self.get_tax()

    def __str__(self):
        return "Month"

    def get_tax(self):
        print("Total a pagar este bimestre: ${}".format(self.first_month + self.second_month))
