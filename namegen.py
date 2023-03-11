import builtins
from random import choice, randint

def repeat_keys(prob_dist: dict) -> list:
    return tuple([x for x in [[k] * prob_dist[k] for k in prob_dist] for x in x])

vowel = repeat_keys({"a": 8, "e": 8, "i": 6, "o": 4, "u": 4, "y": 1, "æ": 1})
trap = repeat_keys({"r": 5, "l": 3, "j": 1})
nasal1 = repeat_keys({"n": 5, "m": 3, "ɲ": 1})
nasal2 = repeat_keys({"n": 5, "m": 3, "ŋ": 1})
fricSibVoiceless = repeat_keys({"f": 2, "þ": 1})
fricSibVoiced = repeat_keys({"v": 2, "w": 1})
fricNsib = repeat_keys({"s": 6, "z": 1, "š": 1})
plosiveVoiceless = repeat_keys({"p": 2, "t": 2, "k": 1, "c": 1})
plosiveVoiced = repeat_keys({"b": 1, "d": 1, "g": 1})

onset = repeat_keys({
    (()): 12,
    (plosiveVoiceless,): 4,
    (plosiveVoiced,): 4,
    (plosiveVoiceless, fricSibVoiceless): 1,
    (plosiveVoiced, fricSibVoiced): 1,
    (plosiveVoiceless, fricNsib): 2,
    (plosiveVoiceless, trap): 1,
    (plosiveVoiced, trap): 1,
    (plosiveVoiceless, fricSibVoiceless, trap): 1,
    (plosiveVoiceless, nasal1): 1,
    (plosiveVoiced, nasal1): 1,
    (fricNsib,): 8,
    (fricNsib, plosiveVoiceless): 2,
    (fricNsib, trap): 2,
    (fricNsib, nasal1): 2,
    (fricSibVoiceless,): 4,
    (fricSibVoiced,): 4,
    (fricSibVoiceless, nasal1): 2,
    (fricSibVoiceless, trap): 1,
    (fricSibVoiced, trap): 1,
    (nasal1,): 8,
    (nasal1, trap): 2,
    (trap,): 8
})
nucleus = [(vowel,)]
coda = repeat_keys({
    (()): 12,
    (trap,): 8,
    (trap, nasal2): 2,
    (trap, fricNsib): 2,
    (trap, fricNsib, plosiveVoiceless): 1,
    (trap, fricSibVoiceless): 2,
    (trap, plosiveVoiceless): 1,
    (trap, plosiveVoiced): 1,
    (nasal2,): 8,
    (nasal2, fricNsib): 2,
    (nasal2, fricSibVoiceless): 2,
    (nasal2, plosiveVoiceless): 1,
    (nasal2, plosiveVoiced): 1,
    (fricSibVoiceless,): 4,
    (fricSibVoiced,): 4,
    (fricNsib,): 8,
    (fricNsib, plosiveVoiceless): 2,
    (plosiveVoiceless,): 4,
    (plosiveVoiced,): 4,
    (plosiveVoiceless, fricNsib): 1,
    (plosiveVoiced, fricNsib): 1
})

def syllable() -> str:
    return "".join("".join(choice(phone) for phone in choice(syl_part)) for syl_part in [onset, nucleus, coda])

# the syllables parameter can be:
# - int for a fixed length
# - (int, int) for a random range
# - None for the default (random length)
def name(syllables = None) -> str:
    match type(syllables):
        case builtins.int:
            length = syllables
        case builtins.tuple | builtins.list:
            length = randint(*(syllables if len(syllables) == 2 else (1, 4)))
        case _:
            length = choice((1, 2, 2, 3, 3, 4))
    return "".join([syllable() for i in range(length)]).capitalize()
