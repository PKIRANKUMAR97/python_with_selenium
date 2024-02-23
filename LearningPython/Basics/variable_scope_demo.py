# LEGB Rule : Local -> Enclosing ->Global -> Builtin
# scope : defines the boundary of the variables
"""
# Local
def scope_variable():
    x = 50
    print(x)


scope_variable()

# Global
y = 100


def scope_variable_global():
    print(y)

scope_variable_global()
"""

def scope_parent():
    z= 200
    print(z)
    def scope_child():
        z= 150
        print(z)
        def scope_grand_child():
            z = 100
            print(z)
        scope_grand_child()
    scope_child()

scope_parent()
