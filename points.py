# Create class
class Point:
     def _init_(self, x=0, y=0):
         self.x = x
         self.y = y

         #Method to print points in coordinate format
         def __str__(self):
           return "({0}, {1})".format(self.x, self.y)
      
      
      # Create Object
           P1 = Point(2, 3)
           print(P1)     

     
