
class Vector:
    
        def __init__(self,data):
             self.data=data
             

        def  __str__(self):     
            return f"Vector({self.data})"

        def __add__(self,other):
            if len(self.data)!=len(other.data):
               raise ValueError("Vectors must have the same dimension for addition.")
            result_data = [x + y for x, y in zip(self.data, other.data)]
            return Vector(result_data)
            
        def dot_product(self,other):
             if len(self.data)!=len(other.data):  
                 raise ValueError("Vectors must have the same dimension for dot product.")             
             return sum(x *y  for x,y in zip(self.data,other.data))
                
               
        def scalar_multiply(self,scalar):
              result_data=[x*scalar for x in self.data]
              return Vector(result_data)
vector1=Vector([1,2,3])
vector2=Vector([4,5,6])
print(vector1)
result_vector= vector1 + vector2
print(result_vector)
dot_product_result=vector1.dot_product(vector2)
print(dot_product_result)
scalar_multiply_result=vector1.scalar_multiply(10)
print(scalar_multiply_result)

             
               