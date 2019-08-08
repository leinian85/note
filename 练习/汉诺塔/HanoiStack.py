class HanoiMove:
    def __init__(self, stack_num, stack_from, stack_to):
        if stack_num <= 0 or stack_from == stack_to or stack_from < 0 or stack_to < 0:
            raise RuntimeError("Invalid parameters")

        self.stack_from = stack_from
        self.stack_to = stack_to
        self.hanoimove = []
        self.moveHanoiStack(self.stack_from, self.stack_to, 1, stack_num)

    def print_move_steps(self):
        if len(self.hanoimove) == 1:
            print(self.hanoimove.pop())
            return

        s = self.hanoimove.pop()
        self.print_move_steps()
        print(s)

    def moveHanoiStack(self, stack_from, stack_to, top, botton):
        s = "移动 " + str(botton) + " 从 " + str(stack_from) + " 到 " + str(stack_to)
        if botton == top:
            self.hanoimove.append(s)
            return

        other = stack_from

        for i in range(1, 4):
            if i != stack_from and i != stack_to:
                other = i
                break

        self.moveHanoiStack(stack_from, other, top, botton - 1)

        self.hanoimove.append(s)

        self.moveHanoiStack(other, stack_to, top, botton - 1)


h = HanoiMove(3, 1, 2)
h.print_move_steps()
