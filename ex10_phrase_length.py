class TestPhraseLength:
    phrase = input("set a phrase: ")

    def test_length_prase(self):
        number = 15
        assert len(self.phrase) < number, f"Phrase length is {number} symbols at least"