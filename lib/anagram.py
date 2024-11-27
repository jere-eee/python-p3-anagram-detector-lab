# your code goes here!
class Anagram:
    def __init__(self, word) -> None:
        self.word = word

    def match(self, list):
        anagrams = []
        for w in list:
            if (sorted(w) == sorted(self.word)):
                anagrams.append(w)
        return anagrams