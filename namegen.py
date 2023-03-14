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

example_scheme = SyllableScheme(
    {"vowel": {"a": 8, "e": 8, "i": 6, "o": 4, "u": 4, "y": 1, "æ": 1},
     "trap": {"r": 5, "l": 3, "j": 1},
     "nasal1": {"n": 5, "m": 3, "ɲ": 1},
     "nasal2": {"n": 5, "m": 3, "ŋ": 1},
     "fricSibVoiceless": {"f": 2, "þ": 1},
     "fricSibVoiced": {"v": 2, "w": 1},
     "fricNsib": {"s": 6, "z": 1, "š": 1},
     "plosiveVoiceless": {"p": 2, "t": 2, "k": 1, "c": 1},
     "plosiveVoiced": {"b": 1, "d": 1, "g": 1}},
    {(()): 12,
     ("plosiveVoiceless",): 4,
     ("plosiveVoiced",): 4,
     ("plosiveVoiceless", "fricSibVoiceless"): 1,
     ("plosiveVoiced", "fricSibVoiced"): 1,
     ("plosiveVoiceless", "fricNsib"): 2,
     ("plosiveVoiceless", "trap"): 1,
     ("plosiveVoiced", "trap"): 1,
     ("plosiveVoiceless", "fricSibVoiceless", "trap"): 1,
     ("plosiveVoiceless", "nasal1"): 1,
     ("plosiveVoiced", "nasal1"): 1,
     ("fricNsib",): 8,
     ("fricNsib", "plosiveVoiceless"): 2,
     ("fricNsib", "trap"): 2,
     ("fricNsib", "nasal1"): 2,
     ("fricSibVoiceless",): 4,
     ("fricSibVoiced",): 4,
     ("fricSibVoiceless", "nasal1"): 2,
     ("fricSibVoiceless", "trap"): 1,
     ("fricSibVoiced", "trap"): 1,
     ("nasal1",): 8,
     ("nasal1", "trap"): 2,
     ("trap",): 8},
    {("vowel",): 1},
    {(()): 12,
     ("trap",): 8,
     ("trap", "nasal2"): 2,
     ("trap", "fricNsib"): 2,
     ("trap", "fricNsib", "plosiveVoiceless"): 1,
     ("trap", "fricSibVoiceless"): 2,
     ("trap", "plosiveVoiceless"): 1,
     ("trap", "plosiveVoiced"): 1,
     ("nasal2",): 8,
     ("nasal2", "fricNsib"): 2,
     ("nasal2", "fricSibVoiceless"): 2,
     ("nasal2", "plosiveVoiceless"): 1,
     ("nasal2", "plosiveVoiced"): 1,
     ("fricSibVoiceless",): 4,
     ("fricSibVoiced",): 4,
     ("fricNsib",): 8,
     ("fricNsib", "plosiveVoiceless"): 2,
     ("plosiveVoiceless",): 4,
     ("plosiveVoiced",): 4,
     ("plosiveVoiceless", "fricNsib"): 1,
     ("plosiveVoiced", "fricNsib"): 1})

def syllable(scheme: SyllableScheme) -> str:
    syllable_parts = [scheme.onset, scheme.nucleus, scheme.coda]
    return "".join("".join(choice(scheme.phone_classes[phone]) for phone in choice(sp)) for sp in syllable_parts)

# the syllables parameter can be:
# - int for a fixed length
# - (int, int) for a random range
# - None for the default (random length)
def name(scheme: SyllableScheme, syllables = None) -> str:
    match type(syllables):
        case builtins.int:
            length = syllables
        case builtins.tuple | builtins.list:
            length = randint(*(syllables if len(syllables) == 2 else (1, 4)))
        case _:
            length = choice((1, 2, 2, 3, 3, 4))
    return "".join([syllable(scheme) for i in range(length)]).capitalize()
