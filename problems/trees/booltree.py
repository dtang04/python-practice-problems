class Bool:
    def __init__(self,b):
        self.b = b
    def isBool(self):
        return True
    def num_nodes(self):
        return 1
    def eval(self):
        return self.b
    def __str__(self):
        return str(self.b)
    
class BoolOp:
    def __init__(self,left,right,op):
        self.left = left
        self.right = right
        self.op = op
    def is_const(self):
        return False
    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()
    def eval(self):
        if self.op == "and":
            return self.left.eval() and self.right.eval()
        elif self.op == "or":
            return self.left.eval or self.right.eval()
    def __str__(self):
        leftstr = str(self.left)
        rightstr = str(self.right)
        if self.op == "and":
            return f"({leftstr} and {rightstr})"
        elif self.op == "or":
            return f"({leftstr} or {rightstr})"

class Not:
    def __init__(self, b):
        self.b = b
    def is_const(self):
        return False
    def num_nodes(self):
        return 1 + self.b.num_nodes()
    def eval(self):
        return not(self.b)
    def __str__(self):
        bstr = str(self.b)
        return f"not({bstr})"

expr = Not(BoolOp(Bool(True),BoolOp(BoolOp(Bool(True),Bool(False),"and"),BoolOp(Bool(True),Bool(False),"or"),"or"),"and"))
print(f"{expr} = {expr.eval()}")
print("num_nodes:", expr.num_nodes())