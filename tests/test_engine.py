import unittest
from engine import SearchEngine

class TestMiniSearchEngine(unittest.TestCase):
    
    def setUp(self):
        """Initialize a fresh search engine before each test"""
        self.engine = SearchEngine()
        self.engine.add(1, "Explore the hidden trails in the Drakensberg mountains")
        self.engine.add(2, "Join us for a weekend braai in Johannesburg with friends")
        self.engine.add(3, "Discover Table Mountain and the beaches of Cape Town")
        self.engine.add(4, "Listen to Kwaito and Afrobeat music on SA Radio")
        self.engine.add(5, "Braais and live music make Durban weekends special")

    def test_single_match(self):
        self.assertEqual(self.engine.search("durban"), [5])
        self.assertEqual(self.engine.search("cape"), [3])
        self.assertEqual(self.engine.search("kwaito"), [4])

    def test_multiple_matches(self):
        self.assertEqual(self.engine.search("braai"), [2, 5])
        self.assertEqual(self.engine.search("music"), [4, 5])
        self.assertEqual(self.engine.search("weekend"), [2, 5])

    def test_case_insensitive(self):
        self.assertEqual(self.engine.search("BRAAI"), [2, 5])
        self.assertEqual(self.engine.search("MuSiC"), [4, 5])

    def test_not_found(self):
        self.assertEqual(self.engine.search("soccer"), [])

    def test_punctuation_ignored(self):
        self.engine.add(6, "Cape Town, beaches & mountains!")
        self.assertIn(6, self.engine.search("cape"))
        self.assertIn(6, self.engine.search("mountains"))

    # if u pass the ones above ur good but
    # --- robusttttttttttttt -----
    
    def test_duplicate_words_in_doc(self):
        self.engine.add(7, "Braai braai braai")
        results = self.engine.search("braai")
        self.assertIn(7, results)
        self.assertEqual(results.count(7), 1)  # doc ID appears only once

    def test_empty_document(self):
        self.engine.add(8, "")
        self.assertEqual(self.engine.search(""), [])

    def test_empty_query(self):
        self.assertEqual(self.engine.search(""), [])

    def test_numbers_and_special_chars(self):
        self.engine.add(9, "Version 2.0 of the app is live!")
        self.assertEqual(self.engine.search("version"), [9])
        self.assertEqual(self.engine.search("2.0"), [])  # numbers with punctuation ignored

    def test_adding_same_doc_id_twice(self):
        self.engine.add(10, "Hello world")
        self.engine.add(10, "Hello world again")
        results = self.engine.search("hello")
        self.assertIn(10, results)
        self.assertEqual(results.count(10), 1)  # doc ID should not duplicate

if __name__ == "__main__":
    unittest.main()
