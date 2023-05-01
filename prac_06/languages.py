
"""
CP1404/CP5632 Practical
rogramming Language client code.
Estimate: 10 minutes
Actual:   8 minutes
"""
from programming_language import programming_Language


def main():
    python = programming_Language("Python", "Dynamic", True, 1991)
    ruby = programming_Language("Ruby", "Dynamic", True, 1995)
    visual_basic = programming_Language("Visual Basic", "Static", False, 1991)

    print(python)
    print(ruby)
    print(visual_basic)

    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    for lang in languages:
        if lang.is_dynamic():
            print(lang.name)


if __name__ == "__main__":
    main()
