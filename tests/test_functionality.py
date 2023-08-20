import unittest

from app import detect_language, named_entities


class LanguageDetectionTestCase(unittest.TestCase):

    def test_english_sentence(self):
        sentence = "The quick brown fox jumps over the lazy dog."
        expected_output = 'en'
        self.assertEqual(detect_language(sentence), expected_output)

    def test_spanish_sentence(self):
        sentence = "El zorro rápido salta sobre el perro perezoso."
        expected_output = 'es'
        self.assertEqual(detect_language(sentence), expected_output)

    def test_french_sentence(self):
        sentence = "Le renard rapide saute par-dessus le chien paresseux."
        expected_output = 'fr'
        self.assertEqual(detect_language(sentence), expected_output)

    def test_german_sentence(self):
        sentence = "Der schnelle Fuchs springt über den faulen Hund."
        expected_output = 'de'
        self.assertEqual(detect_language(sentence), expected_output)

    def test_chinese_sentence(self):
        sentence = "快狐跳懒狗。"
        expected_output = 'zh'
        self.assertEqual(detect_language(sentence), expected_output)


class NamedEntitiesTestCase(unittest.TestCase):

    def test_single_occurrence(self):
        text = "Nelson Mandela was the president of South Africa."
        expected_output = ['Nelson Mandela (1)', 'South Africa (1)']
        self.assertEqual(named_entities(text), expected_output)

    def test_multiple_occurrences(self):
        text = "Amazon is headquartered in Seattle, Washington. Amazon is an e-commerce company."
        expected_output = ['Amazon (2)', 'Seattle (1)', 'Washington (1)']
        self.assertEqual(named_entities(text), expected_output)

    def test_mixed_entities(self):
        sentence = "In 1969, Neil Armstrong set foot on the Moon, marking the success of Apollo 11."
        expected_output = ['1969 (1)', 'Neil Armstrong (1)', 'Moon (1)', 'Apollo 11 (1)']
        self.assertEqual(named_entities(sentence), expected_output)

    def test_no_named_entities(self):
        text = "The weather is really nice today."
        expected_output = []
        self.assertEqual(named_entities(text), expected_output)

    def test_empty_string(self):
        text = ""
        expected_output = []
        self.assertEqual(named_entities(text), expected_output)


if __name__ == '__main__':
    unittest.main()
