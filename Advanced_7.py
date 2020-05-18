class BasicCalculator:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def execute(self, arg1, arg2):
        if self.strategy is None:
            raise NotImplementedError(f'Strategy is not implemented. \n Select right strategy!')

        else:
            self.strategy.execute(arg1, arg2)


class AdditionStrategy:
    def execute(self, arg1, arg2):
        print(f'Adding {arg1} and {arg2}: {arg1 + arg2}')


class SubtractionStrategy:
    def execute(self, arg1, arg2):
        print(f'Subtracting {arg1} from {arg2}: {arg1 - arg2}')


class MultiplyStrategy:
    def execute(self, arg1, arg2):
        print( f'Multiplying {arg1} and {arg2}: {arg1 * arg2}')


class DivideStrategy:
    def execute(self, arg1, arg2):
        print(f'Dividing {arg1} and {arg2}: {arg1 / arg2}')


class PowerToStrategy:
    def execute(self, arg1, arg2):
        print( f'Power {arg1} to {arg2}: {arg1 ** arg2}')


class LeastCommonMultiple:
    def execute(self, arg1, arg2):
        m = arg1 * arg2
        a, b = arg1, arg2
        while arg1 != 0 and arg2 != 0:
            if arg1 > arg2:
                arg1 %= arg2
            else:
                arg2 %= arg1
        print(f'Least common Multiply {a} and {b}: {m // (arg1 + arg2)}')


def main():
    # Choosing right strategy depending on your goal
    no_strategy = BasicCalculator()
    addition_strategy = BasicCalculator(AdditionStrategy())
    subtraction_strategy = BasicCalculator(SubtractionStrategy())
    multiply_strategy = BasicCalculator(MultiplyStrategy())
    division_strategy = BasicCalculator(DivideStrategy())
    power_strategy = BasicCalculator(PowerToStrategy())
    lcm_strategy = BasicCalculator(LeastCommonMultiple())

    # Test calculations choosing different strategies 
    # no_strategy.execute(4, 6)
    addition_strategy.execute(4, 6)
    subtraction_strategy.execute(4, 6)
    multiply_strategy.execute(4, 6)
    division_strategy.execute(4, 6)
    power_strategy.execute(4, 6)
    lcm_strategy.execute(4, 6)


if __name__ == "__main__":
    main()
