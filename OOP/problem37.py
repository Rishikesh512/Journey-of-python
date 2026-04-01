class student :
    def __init__(self,name):

        self.name = name 


    def total_Marks(self,m1,m2,m3):
        return m1 + m2 + m3 
    
    def percentage(self,m1,m2,m3):
        return(m1 + m2 + m3) / 3
    
    def grade(self,m1,m2,m3):
        per = self.percentage(m1,m2,m3)
        if per >= 90:
            return "A"
        
        elif per >= 70:
            return "B"
        
        else:
            return "C"
        


s = student ("Rahul")

print(s.total_Marks(80,90,60))
print(s.percentage(80,90,60))
print(s.grade(80,90,60))