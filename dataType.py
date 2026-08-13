eee="hello" + " " + "world"
print(eee)

print(type(eee))

try:
    x = "Hello"
    sum = x + " " + 5
    print(sum)
except:
    print("Error occurred")

sval = "123"
print(type(sval))

print("Value of sval:", int(sval) + 1)

age = "25"
age_str = str(age)
message = "You are " + age_str + " years old."
print(message)

temp_str = "98.6"
temp = float(temp_str)
celcius = (temp - 32) * 5 / 9
print("Temperature in Celsius:", round(celcius, 2))

boolean_str = "True"
boolean_value = boolean_str == "True"
print("Boolean value:", boolean_value)
print("Type of boolean_value:", type(boolean_value))