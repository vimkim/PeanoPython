
from typing import cast


class NatNum:
    def add(self, natNum: 'NatNum') -> 'NatNum':
        if isinstance(self, Zero):
            return natNum
        else:
            succ = cast('Succ', self)
            return succ.child.add(Succ(natNum))


class Succ(NatNum):
    def __init__(self, child: 'NatNum') -> None:
        self.child = child

    def __str__(self) -> str:
        return "SUCC " + str(self.child)


class Zero(NatNum):

    def __str__(self) -> str:
        return "ZERO"


def main() -> None:

    zero: NatNum = Zero()
    print("zero:", zero)

    one: NatNum = Succ(Zero())
    print("one:", one)

    two: NatNum = Succ(Succ(Zero()))
    print("two:", two)

    three: NatNum = Succ(Succ(Succ(Zero())))
    print("three:", three)

    four1: NatNum = one.add(three)
    four2: NatNum = two.add(two)
    four3: NatNum = three.add(one)
    four4: NatNum = four3.add(zero)
    four5: NatNum = zero.add(four4)

    print("\nprinting 4...")
    print(four1)
    print(four2)
    print(four3)
    print(four4)
    print(four5)


if __name__ == "__main__":
    main()
