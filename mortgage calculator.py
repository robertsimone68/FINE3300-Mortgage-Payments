class Mortgage_Payments:
    def __init__ (self, principal, rate, amortization):
#class object setup and initialization
        self.principal = principal
        self.nominal_rate = rate / 100
#convert to percentage to decimal
        self.amortization = amortization
        self.EAR = (1 + self.nominal_rate / 2) ** 2 - 1
#convert quoted rate to effective annual rate

    def monthly_payment(self):
#implement mortgage_payment method return result
        self.monthly_rate = (1 + self.EAR) ** (1/12) - 1
#convert EAR to monthly rate
        r = self.monthly_rate 
        n = self.amortization * 12
#convert years to months
        return round((self.principal * r) / (1- (1+r) ** -n), 2)
#defining relationship between principal, rate, and amortization

    def semi_monthly_payment(self):
#implement mortgage_payment method return result
        self.semi_monthly_rate = (1 + self.EAR) ** (1/24) - 1
#convert EAR to semi-monthly rate
        r = self.semi_monthly_rate
        n = self.amortization * 24
#convert years to semi-months
        return round((self.principal * r) / (1- (1+r) ** -n), 2)
#defining relationship between principal, rate, and amortization

    def bi_weekly_payment(self):
#implement mortgage_payment method return result
        self.bi_weekly_rate = (1 + self.EAR) ** (1/26) - 1
#convert EAR to bi-monthly rate
        r = self.bi_weekly_rate
        n = self.amortization * 26
#convert years to bi-weekly
        return round((self.principal * r) / (1- (1+r) ** -n), 2)
#defining relationship between principal, rate, and amortization

    def weekly_payment(self):
#implement mortgage_payment method return result
        self.weekly_rate = (1 + self.EAR) ** (1/52) - 1
#convert EAR to weekly rate
        r = self.weekly_rate
        n = self.amortization * 52
#convert years to weekly
        return round((self.principal * r) / (1- (1+r) ** -n), 2)
#defining relationship between principal, rate, and amortization

    def rapid_bi_weekly_payment(self):
#implement mortgage_payment method return result
        self.rapid_bi_weekly_rate = (1 + self.EAR) ** (1/12) - 1
#convert EAR to monthly rate
        r = self.rapid_bi_weekly_rate
        n = self.amortization * 12
#convert years to months
        return round(((self.principal * r) / (1- (1+r) ** -n))/2, 2)
#monthly payment divided by 2

    def rapid_weekly_payment(self):
#implement mortgage_payment method return result
        self.rapid_weekly_rate = (1 + self.EAR) ** (1/12) - 1
#convert EAR to monthly rate
        r = self.rapid_weekly_rate
        n = self.amortization * 12
#convert years to months
        return round(((self.principal * r) / (1- (1+r) ** -n))/4, 2)
#monthly payment divided by 4

    def payment_schedule(self):
        return {
            "monthly payment": self.monthly_payment(),
            "semi-monthly payment": self.semi_monthly_payment(),
            "bi-weekly payment": self.bi_weekly_payment(),
            "weekly payment": self.weekly_payment(),
            "rapid bi-weekly payment": self.rapid_bi_weekly_payment(),
            "rapid weekly payment": self.rapid_weekly_payment()
        }
#return payment schedule in dictionary format

print(Mortgage_Payments(500000, 5.5, 25).payment_schedule())
