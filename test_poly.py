# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:20:23 2020

@author: nathan barloy
"""

import unittest
from poly import Polynom, Polynom2


class Test_Polynom(unittest.TestCase) :
    
    def test_create_empty(self) :
        p = Polynom()
        self.assertIsNotNone(p)
        
    def test_create_not_empty(self) :
        p = Polynom([0,-1,2])
        self.assertIsNotNone(p)
    
    def test_len(self) :
        p = Polynom([0,-1,2])
        res = len(p)
        self.assertEqual(res, 3)
    
    def test_simplify(self) :
        p = Polynom([0,-1,2,0,0,0])
        res = len(p)
        self.assertEqual(res, 3)
    
    def test_degree(self) :
        p = Polynom([0,-1,2,8])
        res = p.degree()
        self.assertEqual(res, 3)
    
    def test_get_value1(self) :
        p = Polynom([0,-1,2])
        res = p.get_coeff(1)
        self.assertEqual(res, -1)
    
    def test_get_value2(self) :
        p = Polynom([0,-1,2])
        res = p.get_coeff(5)
        self.assertEqual(res, 0)
        
    def test_set_value1(self) :
        p = Polynom([0,-1,2])
        p.set_coeff(4,6)
        res = p.get_coeff(4)
        self.assertEqual(res, 6)
        
    def test_set_value2(self) :
        p = Polynom([0,-1,2])
        p.set_coeff(1,6)
        res = p.get_coeff(1)
        self.assertEqual(res, 6)
        
    def test_string(self) :
        p = Polynom([0,-1,2])
        res = str(p)
        self.assertEqual(res, "-1*x + 2*x^2")
    
    def test_add1(self) :
        p1 = Polynom([0,-1,2])
        p2 = Polynom([1,1,0,-3])
        res = (p1+p2).coeffs
        self.assertEqual(res, [1,0,2,-3])
    
    def test_add2(self) :
        p1 = Polynom([0,-1,2,3])
        p2 = Polynom([1,1,0,-3])
        res = (p1+p2).coeffs
        self.assertEqual(res, [1,0,2])
    
    def test_iadd(self) :
        p1 = Polynom([0,-1,2,3])
        p2 = Polynom([1,1,0,-3])
        p1 += p2
        res = p1.coeffs
        self.assertEqual(res, [1,0,2])
    
    def test_sub(self) :
        p1 = Polynom([0,-1,2,3])
        p2 = Polynom([1,1,0,-3])
        res = (p1-p2).coeffs
        self.assertEqual(res, [-1,-2,2,6])
    
    def test_isub(self) :
        p1 = Polynom([0,-1,2,3])
        p2 = Polynom([1,1,0,-3])
        p1 -= p2
        res = p1.coeffs
        self.assertEqual(res, [-1,-2,2,6])
        
    def test_mul_int1(self) :
        p1 = Polynom([0,-1,2,3])
        res = (p1*3).coeffs
        self.assertEqual(res, [0,-3,6,9])
        
    def test_mul_int2(self) :
        p1 = Polynom([0,-1,2,3])
        res = (p1*0).coeffs
        self.assertEqual(res, [])
        
    def test_mul_poly1(self) :
        p1 = Polynom([0,-1,2,3])
        p2 = Polynom([2,0,1])
        res = (p1*p2).coeffs
        self.assertEqual(res, [0,-2,4,5,2,3])
        
    def test_mul_poly2(self) :
        p1 = Polynom([0,-1,2,3])
        p2 = Polynom()
        res = (p1*p2).coeffs
        self.assertEqual(res, [])
        
    def test_imul_int(self) :
        p1 = Polynom([0,-1,2,3])
        p1 *= 3
        res = p1.coeffs
        self.assertEqual(res, [0,-3,6,9])
        
    def test_imul_poly(self) :
        p1 = Polynom([0,-1,2,3])
        p2 = Polynom([2,0,1])
        p1 *= p2
        res = p1.coeffs
        self.assertEqual(res, [0,-2,4,5,2,3])
        
    def test_truediv(self) :
        p1 = Polynom([0,-1,2,3])
        res = (p1/2).coeffs
        self.assertEqual(res, [0,-0.5,1,1.5])
    
    def test_itruediv(self) :
        p1 = Polynom([0,-1,2,3])
        p1 /= 2
        res = p1.coeffs
        self.assertEqual(res, [0,-0.5,1,1.5])
        
    def test_iter(self) :
        p = Polynom([0,-2,4,0,2,3])
        res = []
        for deg, coef in p :
            res.append((deg,coef))
        self.assertEqual(res, [(1,-2),(2,4),(4,2),(5,3)])
    
    def test_evaluate(self) :
        p = Polynom([0,-1,2,3])
        res = p.evaluate(-2)
        self.assertEqual(res, -14)
        
    def test_derivate(self) :
        p = Polynom([2,-1,0,6])
        res = p.derivate().coeffs
        self.assertEqual(res, [-1,0,18])
    
    def test_integrate(self) :
        p = Polynom([2,-1,0,6])
        res = p.integrate(7).coeffs
        self.assertEqual(res, [7,2,-0.5,0,1.5])
        
    def test_equal1(self) :
        p1 = Polynom([1,0,2,6])
        p2 = Polynom([1,0,2,6,0,0])
        self.assertEqual(p1,p2)
    
    def test_equal2(self) :
        p1 = Polynom([1,0,2,6])
        p2 = Polynom([1,0,2])
        self.assertNotEqual(p1,p2)
        
        
        
        


class Test_Polynom2(unittest.TestCase) :
    
    def test_create_empty(self) :
        p = Polynom2()
        self.assertIsNotNone(p)
        
    def test_create_not_empty1(self) :
        p = Polynom2([[0,-1], [1,1]])
        self.assertIsNotNone(p)
        
    def test_create_not_empty2(self) :
        p = Polynom2([Polynom([0,-1]), Polynom([1,1])])
        self.assertIsNotNone(p)
        
    def test_get_matrix(self) :
        p = Polynom2([[0,-1], [1,1]])
        res = p.get_matrix()
        self.assertEqual(res, [[0,-1], [1,1]])
        
    def test_constructor(self) :
        p = Polynom2([Polynom([0,-1]), Polynom([1,1])])
        res = p.get_matrix()
        self.assertEqual(res, [[0,-1], [1,1]])
        
    def test_simplify(self) :
        p = Polynom2([[0,0],[1,0],[2,1],[0,0],[]])
        res = p.get_matrix()
        self.assertEqual(res, [[],[1],[2,1]])
        
    def test_get_value1(self) :
        p = Polynom2([[0,-1], [1,1]])
        res = p.get_coeff(1,0)
        self.assertEqual(res, 1)
        
    def test_get_value2(self) :
        p = Polynom2([[0,-1], [1,1]])
        res = p.get_coeff(4,2)
        self.assertEqual(res, 0)
    
    def test_set_value(self) :
        p = Polynom2([[0,-1], [1,1]])
        p.set_coeff(0,1,0)
        p.set_coeff(3,1,1)
        p.set_coeff(1,3,-1)
        res = p.get_matrix()
        exp = [[],[1,1,0,-1],[],[0,1]]
        self.assertEqual(res, exp)
        
    def test_x_degree(self) :
        p = Polynom2([[1,2],[],[-1,0,8],[4]])
        res = p.x_degree()
        self.assertEqual(res, 3)
        
    def test_y_degree(self) :
        p = Polynom2([[1,2],[],[-1,0,8],[4]])
        res = p.y_degree()
        self.assertEqual(res, 2)
        
    def test_len(self) :
        p = Polynom2([[1,2],[],[-1,0,8],[4]])
        res = len(p)
        self.assertEqual(res, 4)
        
    def test_y_evaluate(self) :
        p1 = Polynom2([[1,2,3],[],[2,-1],[3]])
        p2 = Polynom([2,0,3,3])
        res = p1.y_evaluate(-1)
        self.assertEqual(res, p2)
        
    def test_x_evaluate(self) :
        p1 = Polynom2([[1,2,3],[],[2,-1],[3]])
        res = p1.x_evaluate(-1).coeffs
        self.assertEqual(res, [0,1,3])
        
    def test_evaluate(self) :
        p = Polynom2([[1,2,3],[],[2,-1],[3]])
        res = p.evaluate(2,-1)
        self.assertEqual(res, 38)
        
    def test_string(self) :
        p = Polynom2([[1,2,3],[],[2,-1],[3]])
        res = str(p)
        exp = "1 + 2*y + 3*y^2 + 2*x^2 + -1*x^2*y + 3*x^3"
        self.assertEqual(res, exp)
        
    def test_iter(self) :
        p = Polynom2([[1,0,3],[],[2,-1],[3]])
        res = []
        for x,y,v in p :
            res.append((x,y,v))
        exp = [(0,0,1),(0,2,3),(2,0,2),(2,1,-1),(3,0,3)]
        self.assertEqual(res, exp)
        
    def test_add1(self) :
        p1 = Polynom2([[0,2],[],[1,0,-1],[0,4]])
        p2 = Polynom2([[1],[0,4],[2,2]])
        res = (p1+p2).get_matrix()
        self.assertEqual(res, [[1,2],[0,4],[3,2,-1],[0,4]])
    
    def test_add2(self) :
        p1 = Polynom2([[0,2],[],[1,0,-1],[0,4]])
        p2 = Polynom2([[1],[0,4],[2,2], [0,-4]])
        res = (p1+p2).get_matrix()
        self.assertEqual(res, [[1,2],[0,4],[3,2,-1]])

if __name__ == '__main__' :
    unittest.main()