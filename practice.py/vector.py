
class Vector:
    
        def __init__(self,values):
             self.values=values

        def  __str__(self):     
            return f"Vector(self.values)"

        def __add__(self,other):
            if len(self.values)!=len(other.values):
               raise {f"Strings don't match"}
            else:
                result_values=[x+y for x,y in zip(self.values,other.values)]
                return Vector.result_values
            
        def _dot_product(self,other):
             if len(self.values)!=len(other.values):
               raise {f"values don't have the same dimension"}
             else:
                result_dot=[x*y for x,y in zip(self.values,other.values)]
                return result_dot
               
        def scalar_multiply(self,scalar):
              result_scalar=[x*scalar for x in self.values]
              return Vector(result_scalar)
vect1=(1,2,3,4,5)
vect2=(6,7,8,9,10) 
print(vect1)
print(vect2)
result_addition=vect1+vect2
print(result_addition)
result_dot_product=vect1._dotproduct(vect2)
print(result_dot_product)
result_scalar_multiply=vect1,10
print(scalar-multiply)

             
               