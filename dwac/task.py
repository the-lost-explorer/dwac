class tasks:

    test_string = "I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn’t really happy.\
    Hatred was spreading everywhere, blood was being spilled everywhere, wars were breaking out everywhere.\
    Almost nothing was more annoying than having our wasted time wasted on something not worth wasting it on.\
    The depressed person was in terrible and unceasing emotional pain, and the impossibility of sharing or articulating this pain was itself a component of the pain and a contributing factor in its essential horror.\
    You’re an insomniac, you tell yourself: there are profound truths revealed only to the insomniac by night like those phosphorescent minerals veined and glimmering in the dark but coarse and ordinary otherwise; you have to examine such minerals in the absence of light to discover their beauty, you tell yourself."

    @staticmethod
    def count_words(sentence):
        counts = dict()
        words = sentence.split()

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        print(counts)