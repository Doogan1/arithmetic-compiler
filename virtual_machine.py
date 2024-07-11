class VirtualMachine:
    def __init__(self):
        self.stack = []

    def execute(self, bytecode):
        print("Starting VM execution...")
        for instruction in bytecode:
            print(f"Executing instruction: {instruction}")
            if instruction.startswith("PUSH"):
                _, value = instruction.split()
                self.stack.append(int(value))
                print(f"Stack after PUSH {value}: {self.stack}")
            elif instruction == "ADD":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
                print(f"Stack after ADD: {self.stack}")
            elif instruction == "SUB":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)
                print(f"Stack after SUB: {self.stack}")
            elif instruction == "MUL":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a * b)
                print(f"Stack after MUL: {self.stack}")
            elif instruction == "DIV":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a // b)  # Integer division
                print(f"Stack after DIV: {self.stack}")
            else:
                raise Exception(f"Unknown instruction: {instruction}")

        result = self.stack.pop()
        print(f"Final result: {result}")
        return result

