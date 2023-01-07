class Int:
    def __init__(self, n):
        self.n = n

    def is_const(self):
        return True

    def num_nodes(self):
        return 1

    def eval(self):
        return self.n

    def __str__(self):
        return str(self.n)

class BinOp:
    def __init__(self,left,right,op):
        self.left = left
        self.right = right
        self.op = op
    def is_const(self):
        return False
    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()
    def eval(self):
        if self.op == "+":
            return self.left.eval() + self.right.eval()
        elif self.op == "-":
            return self.left.eval() - self.right.eval()
        elif self.op == "*":
            return self.left.eval() * self.right.eval()
        elif self.op == "/":
            return self.left.eval() / self.right.eval()
    def __str__(self):
        leftstr = str(self.left)
        rightstr = str(self.right)
        if self.op == "+":
            return f"({leftstr} + {rightstr})"
        elif self.op == "-":
            return f"({leftstr} - {rightstr})"
        elif self.op == "*":
            return f"({leftstr} * {rightstr})"
        elif self.op == "/":
            return f"({leftstr} / {rightstr})"

expr = BinOp(Int(28),BinOp(Int(2),BinOp(Int(3),Int(4),"*"),"+"),"/")
print(f"{expr} = {expr.eval()}")