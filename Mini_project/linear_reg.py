x_coe = []
y_coe = []
element1 = int(input("How many element you want to add:"))

element2 = int(input("How many element you want to add:"))

for i in range (element1):
    x = int(input("Enter the coefitient of x:"))
    x_coe.append(x)

for j in range(element2):
    y = int(input("Enter the coefitient of y :"))
    y_coe.append(y)

print("x_coe =",x_coe)
print("y_coe =",y_coe)

sum_x =sum( x_coe)

sum_y = sum(y_coe)

print(sum_x)

print(sum_y)

mean_x = sum_x / len(x_coe)
print(mean_x)

mean_y = sum_y / len(y_coe)
print(mean_y)

sum_x_mean_x = x_coe - mean_x
print(sum_x_mean_x)

sum_y_mean_y = y_coe - mean_y
print(sum_y_mean_y )

covarience_x,y = 1 / len(x_coe)-1 * (sum_x_mean_x) * (sum_y_mean_y)
print(covarience_x,y)

var_x = 1 / len(x_coe) - 1 * (sum_x_mean_x)^2