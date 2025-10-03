'''
SSW 567 Classify Triangle Triangle Test Module
@author: Justin Phan
Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''
import math
from classify_triangle import ClassifyTriangle

def test_init():
    """Sides stored properly in __init__()"""
    triangle = ClassifyTriangle(3,4,5)
    assert triangle.a == 3
    assert triangle.b == 4
    assert triangle.c == 5
def test_right_triangle():
    """test right triangle detection"""
    triangle_1 = ClassifyTriangle(3,4,5) # right triangle
    triangle_2 = ClassifyTriangle(3,3,3) # equilateral triangle, not right
    triangle_3 = ClassifyTriangle(-3,-4,-5)
    triangle_4 = ClassifyTriangle(3.0001,4.0001,5.0001) # right triangle with floating point numbers
    assert triangle_1.right_triangle()
    assert not triangle_2.right_triangle()
    assert not triangle_3.right_triangle()
    assert triangle_4.right_triangle()
def test_scalene_right_triangle():
    """test scalene right triangle detection"""
    triangle_1 = ClassifyTriangle(3,4,5) # scalene right triangle
    triangle_2 = ClassifyTriangle(3,3,3) # equilateral triangle, not right
    triangle_3 = ClassifyTriangle(-3,-4,-5) # scalene right triangle but numbers are negative
    assert triangle_1.scalene_right_triangle()
    assert not triangle_2.scalene_right_triangle()
    assert not triangle_3.scalene_right_triangle()
def test_isoceles_right_triangle():
    """test isoceles right triangle detection"""
    triangle_1 = ClassifyTriangle(1,1,math.sqrt(2)) # isoceles right triangle
    triangle_2 = ClassifyTriangle(3,3,3) # equilateral triangle, not right
    triangle_3 = ClassifyTriangle(-1,-1,math.sqrt(2))
    triangle_4 = ClassifyTriangle(0,0,0) # isoceles right triangle with negative values
    assert triangle_1.isoceles_right_triangle()
    assert not triangle_2.isoceles_right_triangle()
    assert not triangle_3.isoceles_right_triangle()
    assert not triangle_4.isoceles_right_triangle()
def test_scalene_triangle():
    """test scalene triangle detection"""
    triangle_1 = ClassifyTriangle(1,7,9) # all three sides are different
    triangle_2 = ClassifyTriangle(3,3,3) # equilateral triangle, not scalene
    triangle_3 = ClassifyTriangle(-1,-7,-9) # scalene but negative numbers
    assert triangle_1.scalene_triangle()
    assert not triangle_2.scalene_triangle()
    assert not triangle_3.scalene_triangle()
def test_equilateral_triangle():
    """test equilateral triangle detection"""
    triangle_1 = ClassifyTriangle(1,1,1) # all three sides are the same
    triangle_2 = ClassifyTriangle(1,7,9) # scalene triangle, not equilateral
    triangle_3 = ClassifyTriangle(0,0,0) # side lengths are all equal but zero
    assert triangle_1.equilateral_triangle()
    assert not triangle_2.equilateral_triangle()
    assert not triangle_3.equilateral_triangle()
def test_isoceles_triangle():
    """test isoceles triangle detection"""
    triangle_1 = ClassifyTriangle(1,1,9) # two sides are the same
    triangle_2 = ClassifyTriangle(1,7,9) # scalene triangle, not isoceles
    triangle_3 = ClassifyTriangle(-1,-1,-9) # isoceles but negative numbers
    assert triangle_1.isoceles_triangle()
    assert not triangle_2.isoceles_triangle()
    assert not triangle_3.isoceles_triangle()
