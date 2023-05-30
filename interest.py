class DataValidator:
    def validate_data(self, principal, rate, time):
        try:
            principal = float(principal)
            rate = float(rate)
            time = float(time)
            if principal > 0 and time > 0:
                return True
            else:
                return False
        except:
            return False
            
    
class InterestCalculator:
    def calculate_interest(self, prinicpal, rate, time):
        rate = rate / 100
        payment = prinicpal * (rate * pow((1 + rate),time)) / (pow((1 + rate),time) - 1)
        return payment

def CalculateMyPayment():

    validator = DataValidator()
    calculator = InterestCalculator()

    principal = float(input("Kérlek add meg a hitelösszeget: "))
    rate = float(input("Kérlek add meg a kamatlábat: "))
    time = float(input("Kérlek add meg a hitelidőt: "))

    if validator.validate_data(principal, rate, time):
        print("A havi fizetendő összeged a következő: ", calculator.calculate_interest(principal, rate, time))
        print("A pont")
    else:
        print("B pont")
    pass