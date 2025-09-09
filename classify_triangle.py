class ClassifyTriangle:
    
    def __init__(self, s1, s2, s3):
        self.a = s1
        self.b = s2
        self.c = s3
    
    def right_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        else: 
            return round(((self.a ** 2) + (self.b ** 2)), 2) == round((self.c ** 2), 2)

    def scalene_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        else:
            return round(((self.a) != (self.b)), 2) and round(((self.b) != (self.c)), 2) and round(((self.a) != (self.c)), 2) # condition a != c

    def equilateral_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        else:
            return round(((self.a) == round(self.b)), 2) == round((self.c), 2)

    def isoceles_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        else:
            return round(((self.a) == (self.b)), 2) or round(((self.a) == (self.c)), 2) or round(((self.b) == (self.c)), 2)
    
    # idk
    def scalene_right_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        else: 
            return round(((self.a) != (self.b)), 2) and round(((self.b) != (self.c)), 2) and round(((self.a) != (self.c)), 2) and round(((self.a ** 2) + (self.b ** 2)), 2) == round((self.c ** 2), 2)
    
    # idk
    def isoceles_right_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        else:
            return round(((self.a) == (self.b)), 2) or round(((self.b) == (self.c)), 2) or round(((self.a) == (self.c)), 2) and round(((self.a ** 2) + (self.b ** 2)), 2) == round((self.c ** 2), 2)
    
   