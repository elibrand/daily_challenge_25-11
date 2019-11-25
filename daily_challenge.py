import string


class Text:
    def __init__(self, stringy):
        self.stringy = stringy

    def freq_word(self, word):
        x = self.stringy.split(' ')
        count = 0
        for item in x:
            if item == word:
                count += 1
        if count == 0:
            return None
        elif count == 1:
            print(f"'{word}' showed up one time")
            return count
        else:
            print(f"'{word}' showed up {count} times")
            return count

    def unique(self):
        x = self.stringy.split(' ')
        y = []
        for item in x:
            y.append(item)
        z = set(y)
        return list(z)


class TextModification(Text):
    def no_punc(self):
        x = list(self.stringy)
        for item in x:
            if item not in string.ascii_letters and item != " ":
                x.remove(item)
        return ''.join(x)

    def no_key(self):
        x = self.stringy.split(' ')
        for item in x:
            if item in ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
                        "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself",
                        "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which",
                        "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be",
                        "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
                        "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for",
                        "with", "about", "against", "between", "into", "through", "during", "before", "after",
                        "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
                        "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all",
                        "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
                        "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don",
                        "should", "now"]:
                x.remove(item)
        return ' '.join(x)

    def no_spesh(self):
        x = list(self.stringy)
        for item in x:
            if item in string.punctuation:
                x.remove(item)
        return ''.join(x)



