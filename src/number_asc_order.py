class NumberAscOrder:

    def sort(self, stack):
        if stack is None or not hasattr(stack, "is_empty") or not hasattr(stack, "pop"):
            raise TypeError("O argumento 'stack' deve ser uma instância válida de pilha.")

        numbers = []
        while not stack.is_empty():
            numbers.append(stack.pop())

        return sorted(numbers)
