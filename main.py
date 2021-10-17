from pprint import pprint

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def check_balance(symbolstring):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolstring):
        symbol = symbolstring[index]
        if symbol == '(':
            s.push(symbol)
        elif symbol == '[':
            s.push(symbol)
        elif symbol == '{':
            s.push(symbol)
        elif symbol == ')':
            if s.isEmpty() or s.peek() != '(':
                balanced = False
            else:
                s.pop()
        elif symbol == ']':
            if s.isEmpty() or s.peek() != '[':
                balanced = False
            else:
                s.pop()
        elif symbol == '}':
            if s.isEmpty() or s.peek() != '{':
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return 'Balanced'
    else:
        return 'Unbalanced'

print(check_balance('(((([{}]))))'))
print(check_balance('[([])((([[[]]])))]{()}'))
print(check_balance('{{[()]}}'))
print(check_balance('[[{())}]'))
print(check_balance('{{[(])]}}'))

