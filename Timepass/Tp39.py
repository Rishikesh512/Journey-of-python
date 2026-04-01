class shape :
    def __init__(self,name):
        self.name= name


    def area_Of_rectangle(self,length,breadth):
        return length * breadth 

    def area_of_square(self,side):
        return side * side
    
    def area_of_triangle(self,base,height):
        return base * height
    
    def perimeter_of_square(self,side):
        return 4  * side
    
    def perimeter_of_rectangle(self,length,width):
        return  2 * (length + width)
    
    def perimeter_of_triangle(self,a,b,c):
        return a+b+c

r = shape("Rectangle")
s = shape("Square")
t  = shape("Triangle")


print(r.area_Of_rectangle(2,3))
print(r.perimeter_of_rectangle(2,3))
print(s. area_of_square(4))
print(s.perimeter_of_square(4))
print(t.area_of_triangle(4,5))
print(t.perimeter_of_triangle(4,5,6))





