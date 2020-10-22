# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:58:31 2020

@author: nathan barloy
"""
from numbers import Number

class Polynom() :
    def __init__(self, coeffs=[]) :
        self.coeffs = coeffs
        self.simplify()
        
        
    def simplify(self) :
        max_deg = len(self.coeffs)-1
        while max_deg>=0 and self.coeffs[max_deg]==0 :
            max_deg-=1
        self.coeffs = self.coeffs[:max_deg+1]
    
    
    def set_coeff(self, deg, value) :
        for _ in range(len(self.coeffs), deg+1) :
            self.coeffs.append(0)
        self.coeffs[deg] = value
        self.simplify()
        
    
    def get_coeff(self, deg) :
        try :
            return self.coeffs[deg]
        except IndexError :
            return 0
    
    
    def degree(self) :
        return len(self.coeffs)-1
    
    
    def evaluate(self, value) :
        res = 0
        for x in self.coeffs[::-1] :
            res *= value
            res += x
        return res
    
    
    def __iter__(self) :
        self.iter_index=0
        return self
    
    def __next__(self) :
        if self.iter_index>=len(self.coeffs) :
            raise StopIteration
        else :
            while self.coeffs[self.iter_index]==0 :
                self.iter_index += 1
            res = self.coeffs[self.iter_index]
            self.iter_index += 1
            return self.iter_index-1,res
    
    
    def __str__(self) :
        d = self.degree()
        if d<0 :
            return '0'
        s = ""
        for i,val in enumerate(self.coeffs[:]) :
            if val!=0 :
                s += str(val)
                if i==1 :
                    s += '*x'
                elif i>1 :
                    s += '*x^' + str(i)
                s += " + "
        return s[:-3]
    
    
    def __add__(self, other) :
        res = []
        for d in range(max(self.degree(), other.degree())+1) :
            res.append(self.get_coeff(d) + other.get_coeff(d))
        return Polynom(res)
    
    def __iadd__(self, other) :
        res = []
        for d in range(max(self.degree(), other.degree())+1) :
            res.append(self.get_coeff(d) + other.get_coeff(d))
        self.coeffs = res
        self.simplify()
        return self
    
    
    def __mul__(self, other) :
        if isinstance(other, Number) :
            res = [x*other for x in self.coeffs]
            return Polynom(res)
        
        if isinstance(other, Polynom) :
            res = []
            deg1 = self.degree()
            deg2 = other.degree()
            for d in range(deg1+deg2+1) :
                aux = 0
                for i in range(max(0,d-deg2), min(deg1, d)+1) :
                    j = d-i
                    aux += self.get_coeff(i)*other.get_coeff(j)
                res.append(aux)
            return Polynom(res)
        
    def __rmul__(self, other) :
        return self * other
                    
    def __imul__(self, other) :
        if isinstance(other, Number) :
            res = [x*other for x in self.coeffs]
            self.coeffs = res
            self.simplify()
            return self
        
        if isinstance(other, Polynom) :
            res = []
            deg1 = self.degree()
            deg2 = other.degree()
            for d in range(deg1+deg2+1) :
                aux = 0
                for i in range(max(0,d-deg2), min(deg1, d)+1) :
                    j = d-i
                    aux += self.get_coeff(i)*other.get_coeff(j)
                res.append(aux)
            self.coeffs = res
            self.simplify()
            return self
        
    
    def __truediv__(self, other) :
        return self*(1/other)
    
    def __itruediv__(self, other) :
        self *= 1/other
        return self
    
    
    def __sub__(self, other) :
        return self + other*-1
    
    def __isub__(self, other) :
        self += other*-1
        return self
    
    def __len__(self) :
        return len(self.coeffs)
    
    
    def derivate(self) :
        res = []
        for i in range(1, len(self.coeffs)) :
            res.append(self.coeffs[i]*i)
        return Polynom(res)
    
    def integrate(self, c=0) :
        res = [c]
        for i in range(len(self.coeffs)) :
            res.append(self.coeffs[i]/(i+1))
        return Polynom(res)
            







class Polynom2() :
    """
    A polynom of 2 variables
    """
    
    def __init__(self, coeffs=[]) :
        if len(coeffs)>0 and isinstance(coeffs[0], Polynom) :
            self.coeffs = coeffs
        else :
            self.coeffs = []
            for l in coeffs :
                self.coeffs.append(Polynom(l))
        self.simplify()
    
    def simplify(self) :
        max_deg = len(self.coeffs)-1
        while max_deg>=0 and len(self.coeffs[max_deg])==0 :
            max_deg-=1
        self.coeffs = self.coeffs[:max_deg+1]
    
    def degree(self) :
        return len(self.coeffs)-1
    
    def __len__(self) :
        return len(self.coeffs)
    
    def set_coeff(self, x_deg, y_deg, value) :
        for _ in range(len(self.coeffs), x_deg+1):
            self.coeffs.append(Polynom())
        self.coeffs[x_deg].set_coeff(y_deg, value)
    
    def get_coeff(self, x_deg, y_deg=None) :
        if y_deg is None :
            try :
                return self.coeffs[x_deg]
            except IndexError :
                return Polynom()
        try :
            return self.coeffs[x_deg].get_coeff(y_deg)
        except IndexError :
            return 0
    
    def y_evaluate(self, value) :
        res = []
        for p in self.coeffs :
            res.append(p.evaluate(value))
        return Polynom(res)
    
    def x_evaluate(self, value) :
        m = max([e.degree() for e in self.coeffs])
        res = []
        for i in range(m+1) :
            tot = 0
            for j in range(len(self.coeffs)) :
                tot += self.get_coeff(j,i)
            res.append(tot)
        return Polynom(res)
    
    def evaluate(self, x_value, y_value) :
        return self.y_evaluate(y_value).evaluate(x_value)
    
    def __iter__(self) :
        self.iter_index = 0
        self.current_iter = self.coeffs[0].__iter__()
        return self
    
    def __next__(self) :
        try :
            (y,v) = self.current_iter.__next__()
            return self.iter_index, y, v
        except StopIteration :
            self.iter_index +=1
            try :
                while len(self.coeffs[self.iter_index])==0 :
                    self.iter_index += 1
                self.current_iter = self.coeffs[self.iter_index].__iter__()
                (y,v) = self.current_iter.__next__()
                return self.iter_index, y, v
            except IndexError :
                raise StopIteration
    
    def __str__(self) :
        s = ""
        for x,y,v in self :
            s += str(v)
            if x>1 :
                s += '*x^' + str(x)
            elif x==1 :
                s += '*x'
            if y>1 :
                s += '*y^' + str(y)
            elif y==1 :
                s += '*y'
            s += ' + '
        return s[:-3]
            
    
    def __add__(self, other) :
        res = []
        for d in range(max(self.degree(), other.degree())+1) :
            res.append(self.get_coeff(d) + other.get_coeff(d))
        return Polynom2(res)
    
    def __iadd__(self, other) :
        res = []
        for d in range(max(self.degree(), other.degree())+1) :
            res.append(self.get_coeff(d) + other.get_coeff(d))
        self.coeffs = res
        self.simplify()
        return self
    
    def __sub__(self, other) :
        return self + other*-1
    
    def __isub__(self, other) :
        self += other*-1
        return self
    
    def __mul__(self, other) :
        if isinstance(other, Number) :
            res = [x*other for x in self.coeffs]
            return Polynom2(res)
        
        if isinstance(other, Polynom2) :
            res = []
            deg1 = self.degree()
            deg2 = other.degree()
            for d in range(deg1+deg2+1) :
                aux = Polynom()
                for i in range(max(0,d-deg2), min(deg1, d)+1) :
                    j = d-i
                    aux += self.get_coeff(i)*other.get_coeff(j)
                res.append(aux)
            return Polynom2(res)
        
    def __rmul__(self, other) :
        return self * other
                    
    def __imul__(self, other) :
        if isinstance(other, Number) :
            res = [x*other for x in self.coeffs]
            self.coeffs = res
            self.simplify()
            return self
        
        if isinstance(other, Polynom2) :
            res = []
            deg1 = self.degree()
            deg2 = other.degree()
            for d in range(deg1+deg2+1) :
                aux = Polynom()
                for i in range(max(0,d-deg2), min(deg1, d)+1) :
                    j = d-i
                    aux += self.get_coeff(i)*other.get_coeff(j)
                res.append(aux)
            self.coeffs = res
            self.simplify()
            return self
    
    def __truediv__(self, other) :
        return self*(1/other)
    
    def __itruediv__(self, other) :
        self *= 1/other
        return self
        
            