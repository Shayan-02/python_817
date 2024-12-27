class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0


t1 = Temperature()
print(t1.celsius_to_fahrenheit(0))  # 32.0
print(t1.fahrenheit_to_celsius(32))  # 0.0
print(t1.is_freezing(0))  # True
