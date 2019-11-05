class tasks:
    @staticmethod
    def count_words(sentence):
        counts = dict()
        words = sentence.split()

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts