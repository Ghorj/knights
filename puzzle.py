from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

Asays = Symbol("A says")
# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Basic sintax "Aknight or Aknave, but not both"
    Or(AKnight, AKnave),
    Or(Not(AKnight), Not(AKnave)),
    

    # puzzle
    # A says "I am both a knight and a knave."
    # AKnight <=> (Aknight ^ AKnave)
    Or(Not(AKnight), AKnave)

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Basic sintax "Aknight or Aknave, but not both"
    Or(AKnight, AKnave),
    Or(Not(AKnight), Not(AKnave)),

    # Basic sintax "Bknight or Bknave, but not both"
    Or(BKnight, BKnave),
    Or(Not(BKnight), Not(BKnave)),

    # puzzle
    # A says "We are both knaves."
    # AKnight <=> (AKnave ^ BKnave)
    Or(Not(AKnight), AKnave),
    Or(Not(AKnight), BKnave),
    Or(Not(AKnave), Not(BKnave), AKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Basic sintax "Aknight or Aknave, but not both"
    Or(AKnight, AKnave),
    Or(Not(AKnight), Not(AKnave)),

    # Basic sintax "Bknight or Bknave, but not both"
    Or(BKnight, BKnave),
    Or(Not(BKnight), Not(BKnave)),

    # puzzle
    # A says "We are the same kind."
    # AKnight <=> [(AKnight ^ BKnight) v (AKnave ^ BKnave)]
    Or(Not(AKnight), BKnight, AKnave),
    Or(Not(AKnight), BKnight, BKnave),
    Or(Not(AKnave), Not(BKnave), AKnight),

    # B says "We are of different kinds."
    # BKnight <=> [(AKnight ^ BKnave) v (AKnave ^ BKnight)]
    Or(Not(BKnight), AKnight, AKnave),
    Or(Not(BKnight), BKnave, AKnave),
    Or(Not(AKnight), Not(BKnave), BKnight)
    

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Basic sintax "Aknight or Aknave, but not both"
    Or(AKnight, AKnave),
    Or(Not(AKnight), Not(AKnave)),

    # Basic sintax "Bknight or Bknave, but not both"
    Or(BKnight, BKnave),
    Or(Not(BKnight), Not(BKnave)),

    # Basic sintax "Cknight or Cknave, but not both"
    Or(CKnight, CKnave),
    Or(Not(CKnight), Not(CKnave)),


    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    # AKnight v (AKnight <=> AKnave)
    Or(Not(AKnave), AKnight),    

    # B says "A said 'I am a knave'."
    # BKnight <=> (AKnight <=> AKnave)
    Or(Not(BKnight), Not(AKnight), AKnave),
    Or(Not(BKnight), Not(AKnave), AKnight),
    Or(AKnight, AKnave, BKnight),
    Or(Not(AKnave), Not(AKnight), BKnight),

    # B says "C is a knave."
    # BKnight <=> CKnave
    Or(Not(BKnight), CKnave),
    Or(Not(CKnave), BKnight),

    # C says "A is a knight."
    # CKnight <=> AKnight
    Or(Not(CKnight), AKnight),
    Or(Not(AKnight), CKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
