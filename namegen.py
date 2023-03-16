import builtins
from random import choice, randint

def repeat_keys(prob_dist: dict) -> list:
    return tuple([x for x in [[k] * prob_dist[k] for k in prob_dist] for x in x])

class SyllableScheme:
    def __init__(self, phone_classes, onset, nucleus, coda):
        """phone_classes is a string-dictionary dictionary mapping phone
        classes to a mapping of their members to their frequencies, e.g.
        "vowel": {"a": 1}. onset, nucleus, and coda are dictionaries
        mapping tuples of phone classes to their frequencies.
        """
        self.phone_classes = {pc: repeat_keys(phone_classes[pc]) for pc in phone_classes}
        self.onset = repeat_keys(onset)
        self.nucleus = repeat_keys(nucleus)
        self.coda = repeat_keys(coda)

def syllable(scheme: SyllableScheme) -> str:
    syllable_parts = [scheme.onset, scheme.nucleus, scheme.coda]
    return "".join("".join(choice(scheme.phone_classes[phone]) for phone in choice(sp)) for sp in syllable_parts)

# the schemes parameter is a tuple of three SyllableSchemes,
# where the first is used for the first syllable, the second
# for syllables between the first and last, and the third
# for the last syllable, unless there is only one syllable
#
# the syllables parameter can be:
# - int for a fixed length
# - (int, int) for a random range
# - None for the default (random length)
def name(schemes: tuple[SyllableScheme], syllables = None) -> str:
    match type(syllables):
        case builtins.int:
            length = syllables
        case builtins.tuple | builtins.list:
            length = randint(*(syllables if len(syllables) == 2 else (1, 4)))
        case _:
            length = choice((1, 2, 2, 3, 3, 4))
    n = ""
    for i in range(length):
        n += syllable(schemes[0 if i == 0 else (2 if i == length - 1 else 1)])
    return n.capitalize()

if __name__ == '__main__':
    example_scheme_f = SyllableScheme(
        {"vowel": {"a": 15, "e": 10, "i": 8, "o": 7, "u": 5, "y": 1, "æ": 4},
         "trap": {"r": 5, "l": 3, "j": 1},
         "nasal1": {"n": 1, "m": 3, "ɲ": 1},
         "nasal2": {"n": 3, "m": 1, "ŋ": 1},
         "fricSibVoiceless": {"f": 1, "þ": 1},
         "fricSibVoiced": {"v": 1, "w": 1, "h": 2},
         "fricNsib": {"s": 5, "z": 1, "š": 3},
         "plosiveVoiceless": {"p": 1, "t": 3, "k": 1, "c": 3},
         "plosiveVoiced": {"b": 3, "d": 1, "g": 3}},
        {(()): 13,
         ("plosiveVoiceless",): 1,
         ("plosiveVoiced",): 8,
         ("plosiveVoiced", "fricSibVoiced"): 1,
         ("plosiveVoiceless", "trap"): 1,
         ("plosiveVoiced", "trap"): 1,
         ("plosiveVoiced", "fricSibVoiced", "trap"): 1,
         ("fricNsib",): 3,
         ("fricNsib", "fricSibVoiced"): 1,
         ("fricNsib", "trap"): 1,
         ("fricSibVoiceless",): 4,
         ("fricSibVoiced",): 5,
         ("fricSibVoiceless", "trap"): 1,
         ("nasal1",): 5,},
        {("vowel",): 1},
        {(()): 16,
         ("trap",): 9,
         ("trap", "nasal2"): 1,
         ("trap", "fricNsib"): 1,
         ("trap", "plosiveVoiceless"): 1,
         ("nasal2",): 7,
         ("fricSibVoiceless",): 1,
         ("fricNsib",): 1,
         ("plosiveVoiceless",): 3})

    example_scheme_m = SyllableScheme(
        {"vowel": {"a": 4, "e": 8, "i": 5, "o": 3, "u": 2, "y": 1, "æ": 1},
         "trap": {"r": 5, "l": 3, "j": 1},
         "nasal1": {"n": 6, "m": 3, "ɲ": 1},
         "nasal2": {"n": 8, "m": 1, "ŋ": 1},
         "fricSibVoiceless": {"f": 1, "þ": 1},
         "fricSibVoiced": {"v": 1, "w": 1, "h": 2},
         "fricNsib": {"s": 8, "z": 1, "š": 1},
         "plosiveVoiceless": {"p": 2, "t": 12, "k": 1, "c": 1},
         "plosiveVoiced": {"b": 1, "d": 4, "g": 4}},
        {(()): 1,
         ("plosiveVoiceless",): 2,
         ("plosiveVoiced",): 18,
         ("plosiveVoiceless", "fricSibVoiced"): 1,
         ("plosiveVoiceless", "trap"): 4,
         ("plosiveVoiced", "trap"): 1,
         ("plosiveVoiced", "nasal1"): 1,
         ("fricNsib",): 2,
         ("fricSibVoiceless",): 1,
         ("fricSibVoiced",): 2,
         ("fricSibVoiced", "trap"): 1,
         ("nasal1",): 4,
         ("trap",): 6},
        {("vowel",): 1},
        {(()): 16,
         ("trap",): 3,
         ("nasal2",): 2})

    example_scheme_l = SyllableScheme(
        {"vowel": {"a": 15, "e": 13, "i": 10, "o": 5, "u": 4, "y": 1, "æ": 1},
         "trap": {"r": 5, "l": 3, "j": 1},
         "nasal1": {"n": 9, "m": 9, "ɲ": 1},
         "nasal2": {"n": 10, "m": 1, "ŋ": 1},
         "fricSibVoiceless": {"f": 1, "þ": 1},
         "fricSibVoiced": {"v": 1, "w": 1, "h": 2},
         "fricNsib": {"s": 6, "z": 2, "š": 1},
         "plosiveVoiceless": {"p": 1, "t": 8, "k": 3, "c": 4},
         "plosiveVoiced": {"b": 1, "d": 6, "g": 1}},
        {(()): 1,
         ("plosiveVoiceless",): 2,
         ("plosiveVoiced",): 21,
         ("plosiveVoiceless", "trap"): 1,
         ("plosiveVoiced", "trap"): 1,
         ("fricNsib",): 4,
         ("fricNsib", "fricSibVoiced"): 1,
         ("fricSibVoiceless",): 2,
         ("fricSibVoiced",): 4,
         ("fricSibVoiceless", "trap"): 1,
         ("nasal1",): 4,
         ("trap",): 8},
        {("vowel",): 1},
        {(()): 8,
         ("trap",): 5,
         ("trap", "fricSibVoiceless"): 2,
         ("trap", "plosiveVoiceless"): 3,
         ("trap", "plosiveVoiced"): 6,
         ("nasal2",): 3,
         ("nasal2", "fricSibVoiceless"): 1,
         ("nasal2", "plosiveVoiced"): 2,
         ("fricSibVoiced",): 1,
         ("fricNsib",): 3,
         ("fricNsib", "plosiveVoiceless"): 1,
         ("plosiveVoiceless",): 4,
         ("plosiveVoiced",): 4})
    
    for i in range(10):
        print(name((example_scheme_f, example_scheme_m, example_scheme_l)))
