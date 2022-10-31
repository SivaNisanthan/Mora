a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))

# In order to form a triangle, the angles should sum up to 180 degrees
# and all three angles should be greater than zero.
if ((a + b + c) != 180) or (a <= 0 or b <= 0 or c <= 0):
    print("Angles do not form a triangle")
elif a == 90 or b == 90 or c == 90:
    print("Right angled")
elif a > 90 or b > 90 or c > 90:
    print("Obtuse angled")
elif a < 90 and b < 90 and c < 90:
    print("Acute angled")
