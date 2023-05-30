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
#print(validator.validate_data(0.0, 0.0, 0.0))
#print(validator.validate_data(10000, 10, 0))
#print(validator.validate_data(10000.0, 10.0, 12.0))
#print("-------------")


#print(calculator.calculate_interest(0.0, 0.0, 0.0))
#print(calculator.calculate_interest(10000.0, 10.0, 12.0))
#print(calculator.calculate_interest(12000.0, 5.0, 12.0))
#print(calculator.calculate_interest(0.0, 5.0, 12.0))