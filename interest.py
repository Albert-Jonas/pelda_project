class DataValidator:
    def validate_data(self, prinicpal, rate, time):
        if isinstance(prinicpal, float) and isinstance(rate, float) and isinstance(time, float) and prinicpal > 0 and time > 0:
            return True
        else:
            return False
    

class InterestCalculator:
    def calculate_interest(self, prinicpal, rate, time):
        rate = rate / 100
        payment = prinicpal * (rate * pow((1 + rate),time)) / (pow((1 + rate),time) - 1)
        return payment
    

validator = DataValidator()
calculator = InterestCalculator()

principal = input("Kérlek add meg a hitelösszeget: ")
rate = input("Kérlek add meg a kamatlábat: ")
time = input("Kérlek add meg a hitelidőt: ")

if validator.validate_data(principal, rate, time):
    print("A havi fizetendő összeged a következő: ", calculator.calculate_interest(principal, rate, time))
else:
    pass

