import unittest
from word2num_de import word_to_number

class TestWord2Num(unittest.TestCase):
    def test_simple_nums(self):
        self.assertEqual(word_to_number("null"), "0")
        self.assertEqual(word_to_number("zwei"), "2")
        self.assertEqual(word_to_number("eins"), "1")
        self.assertEqual(word_to_number("drei"), "3")
        self.assertEqual(word_to_number("vier"), "4")
        self.assertEqual(word_to_number("fünf"), "5")
        self.assertEqual(word_to_number("sechs"), "6")
        self.assertEqual(word_to_number("sieben"), "7")
        self.assertEqual(word_to_number("acht"), "8")
        self.assertEqual(word_to_number("neun"), "9")
        self.assertEqual(word_to_number("zehn"), "10")
        self.assertEqual(word_to_number("elf"), "11")
        self.assertEqual(word_to_number("zwölf"), "12")
        self.assertEqual(word_to_number("dreizehn"), "13")
        self.assertEqual(word_to_number("vierzehn"), "14")
        self.assertEqual(word_to_number("fünfzehn"), "15")
        self.assertEqual(word_to_number("sechszehn"), "16")
        self.assertEqual(word_to_number("siebzehn"), "17")
        self.assertEqual(word_to_number("achtzehn"), "18")
        self.assertEqual(word_to_number("neunzehn"), "19")
        self.assertEqual(word_to_number("zwanzig"), "20")

    def test_two_digits(self):
        self.assertEqual(word_to_number("einundzwanzig"), "21")
        self.assertEqual(word_to_number("zweiundzwanzig"), "22")
        self.assertEqual(word_to_number("dreiundzwanzig"), "23")
        self.assertEqual(word_to_number("vierundzwanzig"), "24")
        self.assertEqual(word_to_number("dreiunddreißig"), "33")
        self.assertEqual(word_to_number("vierunddreissig"), "34")
        self.assertEqual(word_to_number("fünfundvierzig"), "45")
        self.assertEqual(word_to_number("siebenundfünfzig"), "57")
        self.assertEqual(word_to_number("achtundsechzig"), "68")
        self.assertEqual(word_to_number("neunundsiebzig"), "79")
        self.assertEqual(word_to_number("dreiundachtzig"), "83")
        self.assertEqual(word_to_number("neunundneunzig"), "99")

    def test_three_digits(self):
        self.assertEqual(word_to_number("hundert"), "100")
        self.assertEqual(word_to_number("einhundert"), "100")
        self.assertEqual(word_to_number("fünfhundert"), "500")
        self.assertEqual(word_to_number("einhundertacht"), "108")
        self.assertEqual(word_to_number("einhundertundsieben"), "107")
        self.assertEqual(word_to_number("zweihunderteins"), "201")
        self.assertEqual(word_to_number("sechshundertsechsundsechzig"), "666")
        self.assertEqual(word_to_number("neunhundertneunundneunzig"), "999")

    def test_four_digits(self):
        self.assertEqual(word_to_number("tausend"), "1000")
        self.assertEqual(word_to_number("eintausend"), "1000")
        self.assertEqual(word_to_number("zweitausend"), "2000")
        self.assertEqual(word_to_number("dreitausend"), "3000")
        self.assertEqual(word_to_number("viertausendvier"), "4004")
        self.assertEqual(word_to_number("sechstausendsechs"), "6006")
        self.assertEqual(word_to_number("achttausendvierunddreißig"), "8034")
        self.assertEqual(word_to_number("siebentausendeinhundertzweiundachtzig"), "7182")
        self.assertEqual(word_to_number("neuntausendvierhundertdreizehn"), "9413")
        self.assertEqual(word_to_number("zehntausend"), "10000")
        self.assertEqual(word_to_number("fünfzehntausendsieben"), "15007")
        self.assertEqual(word_to_number("zweiunddreißigtausendfünfhundertachtundvierzig"), "32548")
        self.assertEqual(word_to_number("hunderttausend"), "100000")
        self.assertEqual(word_to_number("einhunderttausend"), "100000")
        self.assertEqual(word_to_number("neunhundertneunundneunzigtausendneunhundertneunundneunzig"), "999999")
        
    def test_special(self):
        self.assertEqual(word_to_number("hunderteins"), "101")
        self.assertEqual(word_to_number("tausendundzwei"), "1002")
        self.assertEqual(word_to_number("eintausendzwanzig"), "1020")
        self.assertEqual(word_to_number("Bäckerei"), "Bäckerei")

        
if __name__ == '__main__':
    unittest.main()