# 1) Create a class named `Point`.

# 2) Define a constructor method `__init__(self, x=0, y=0)`:
#    a) This constructor should accept two parameters `x` and `y`.
#    b) Assign default values `0` to both parameters.
#    c) Store the values in instance variables:
#       `self.x = x`
#       `self.y = y`

# 3) Define a special method `__str__(self)`:
#    a) This method is used to return the object in string format.
#    b) Return the point in coordinate form:
#       "(x, y)"
#    c) Use the `format()` function to insert values of `self.x` and `self.y`.

# 4) Create an object named `p1` of class `Point`:
#    a) Pass values `2` and `3` while creating the object.

# 5) Print the object `p1`:
#    a) This will automatically call the `__str__()` method.
#    b) The output will be displayed in coordinate form.

class point:
    def __init__(self, x=0,y=0):
        
        self.x = x
        self.y = y
    def __str__(self):
        return"({0},{1})".format(self.x,self.y)
p1 = point(2,3)
print(p1)
