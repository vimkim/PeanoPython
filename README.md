# PeanoPython
 Most Elegant Peano Arithmatic Implementation in Python


``` python
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
```

```bash
$ py main.py
zero: ZERO
one: SUCC ZERO
two: SUCC SUCC ZERO
three: SUCC SUCC SUCC ZERO

printing 4...
SUCC SUCC SUCC SUCC ZERO
SUCC SUCC SUCC SUCC ZERO
SUCC SUCC SUCC SUCC ZERO
SUCC SUCC SUCC SUCC ZERO
SUCC SUCC SUCC SUCC ZERO
```
