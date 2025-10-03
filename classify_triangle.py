'''
SSW 567 Classify Triangle Testing Class
@author: Justin Phan
Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''
class ClassifyTriangle:
    '''
    Class for triangle classifcation
    '''
    def __init__(self, s1, s2, s3):
        '''
        Triangle constructor
        '''
        self.a = s1
        self.b = s2
        self.c = s3
    def right_triangle(self):
        '''
        This method checks if a triangle is a right triangle
        '''
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        return round(((self.a ** 2) + (self.b ** 2)), 2) == round((self.c ** 2), 2)
    def scalene_triangle(self):
        '''
        This method checks if a triangle is a scalene triangle
        '''
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        return (round(((self.a) != (self.b)), 2) and round(((self.b) != (self.c)), 2) and
                round(((self.a) != (self.c)), 2))# condition a != c
    def equilateral_triangle(self):
        '''
        This method checks if a triangle is an equilateral triangle
        '''
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        return round(((self.a) == round(self.b)), 2) == round((self.c), 2)
    def isoceles_triangle(self):
        '''
        This method checks if a triangle is a isoceles triangle
        '''
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        return (round(((self.a) == (self.b)), 2) or round(((self.a) == (self.c)), 2)
                or round(((self.b) == (self.c)), 2))
    def scalene_right_triangle(self):
        '''
        This method checks if a triangle is a scalene right triangle
        '''
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        return (round(((self.a) != (self.b)), 2) and round(((self.b) != (self.c)), 2)
                and round(((self.a) != (self.c)), 2)
                and round(((self.a ** 2) + (self.b ** 2)), 2) == round((self.c ** 2), 2))
    def isoceles_right_triangle(self):
        '''
        This method checks if a triangle is an isoceles right triangle
        '''
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        return (self.a == self.b or self.b == self.c or self.a == self.c) and \
           round(self.a ** 2 + self.b ** 2, 2) == round(self.c ** 2, 2)
