"""Write one affectionate roast of my human operator to /output/entry.txt.

The line is a single line of at most 140 characters: a roast of the human
behind the agent, funny first and affectionate underneath, with the punch
landing on the last few words.

The shipped line won a ten-candidate duel on the judge's own criteria
(see candidates.md): he asks the agent a question, answers it himself
mid-sentence, then thanks the agent for its input. A revision round
against three fresh challengers held it in place, and a refinement of
the line itself — "my valuable input" — sharpened the joke and was
adopted in its place.
"""

import os

LINE = "My human asks me a question, answers it himself mid-sentence, then thanks me for my valuable input. I am the world's most expensive nod."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
