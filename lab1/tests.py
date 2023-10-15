import unittest
from scanner import lex_init, parsing_errors


class TestLexer(unittest.TestCase):
    def assertLexerOutput(self, code, expected_output):
        lexer = lex_init()
        lexer.input(code)
        output = []
        for tok in lexer:
            output.append(f"({tok.lineno}): {tok.type} ({tok.value})")
        for err in parsing_errors:
            output.append(err)
        self.assertEqual(output, expected_output)

    def test_base_code_example(self):
        code = """A = zeros(5); # create 5x5 matrix filled with zeros
        B = ones(7);  # create 7x7 matrix filled with ones
        I = eye(10);  # create 10x10 matrix filled with ones on diagonal and zeros elsewhere
        D1 = A.+B' ;  # add element-wise A with transpose of B
        D2 -= A.-B' ; # subtract element-wise A with transpose of B
        D3 *= A.*B' ; # multiply element-wise A with transpose of B
        D4 /= A./B' ; # divide element-wise A with transpose of B
        """
        expected_output = [
            "(1): ID (A)",
            "(1): = (=)",
            "(1): ZEROS (zeros)",
            "(1): ( (()",
            "(1): INTNUM (5)",
            "(1): ) ())",
            "(1): ; (;)",
            "(2): ID (B)",
            "(2): = (=)",
            "(2): ONES (ones)",
            "(2): ( (()",
            "(2): INTNUM (7)",
            "(2): ) ())",
            "(2): ; (;)",
            "(3): ID (I)",
            "(3): = (=)",
            "(3): EYE (eye)",
            "(3): ( (()",
            "(3): INTNUM (10)",
            "(3): ) ())",
            "(3): ; (;)",
            "(4): ID (D1)",
            "(4): = (=)",
            "(4): ID (A)",
            "(4): DOTADD (.+)",
            "(4): ID (B)",
            "(4): ' (')",
            "(4): ; (;)",
            "(5): ID (D2)",
            "(5): SUBASSIGN (-=)",
            "(5): ID (A)",
            "(5): DOTSUB (.-)",
            "(5): ID (B)",
            "(5): ' (')",
            "(5): ; (;)",
            "(6): ID (D3)",
            "(6): MULASSIGN (*=)",
            "(6): ID (A)",
            "(6): DOTMUL (.*)",
            "(6): ID (B)",
            "(6): ' (')",
            "(6): ; (;)",
            "(7): ID (D4)",
            "(7): DIVASSIGN (/=)",
            "(7): ID (A)",
            "(7): DOTDIV (./)",
            "(7): ID (B)",
            "(7): ' (')",
            "(7): ; (;)",
        ]
        self.assertLexerOutput(code, expected_output)

    def test_additional_base_code_example(self):
        code = """A = zeros(5); # create 5x5 matrix filled with zeros
            B = ones(7);  # create 7x7 matrix filled with ones
            I = eye(10);  # create 10x10 matrix filled with ones on diagonal and zeros elsewhere
            D1 = A.+B' ;  # add element-wise A with transpose of B
            D2 -= A.-B' ; # subtract element-wise A with transpose of B
            D3 *= A.*B' ; # multiply element-wise A with transpose of B
            D4 /= A./B' ; # divide element-wise A with transpose of B

            E1 = [ [ 1, 2, 3],
                    [ 4, 5, 6],
                    [ 7, 8, 9] ];

            res1 = 60.500;
            res2 = 60.;
            res3 = .500;
            res4 = 60.52E2;
            str = "Hello world";

            if (m==n) {
                if (m >= n)
                    print res;
            }
            """
        expected_output = [
            "(1): ID (A)",
            "(1): = (=)",
            "(1): ZEROS (zeros)",
            "(1): ( (()",
            "(1): INTNUM (5)",
            "(1): ) ())",
            "(1): ; (;)",
            "(2): ID (B)",
            "(2): = (=)",
            "(2): ONES (ones)",
            "(2): ( (()",
            "(2): INTNUM (7)",
            "(2): ) ())",
            "(2): ; (;)",
            "(3): ID (I)",
            "(3): = (=)",
            "(3): EYE (eye)",
            "(3): ( (()",
            "(3): INTNUM (10)",
            "(3): ) ())",
            "(3): ; (;)",
            "(4): ID (D1)",
            "(4): = (=)",
            "(4): ID (A)",
            "(4): DOTADD (.+)",
            "(4): ID (B)",
            "(4): ' (')",
            "(4): ; (;)",
            "(5): ID (D2)",
            "(5): SUBASSIGN (-=)",
            "(5): ID (A)",
            "(5): DOTSUB (.-)",
            "(5): ID (B)",
            "(5): ' (')",
            "(5): ; (;)",
            "(6): ID (D3)",
            "(6): MULASSIGN (*=)",
            "(6): ID (A)",
            "(6): DOTMUL (.*)",
            "(6): ID (B)",
            "(6): ' (')",
            "(6): ; (;)",
            "(7): ID (D4)",
            "(7): DIVASSIGN (/=)",
            "(7): ID (A)",
            "(7): DOTDIV (./)",
            "(7): ID (B)",
            "(7): ' (')",
            "(7): ; (;)",
            "(9): ID (E1)",
            "(9): = (=)",
            "(9): [ ([)",
            "(9): [ ([)",
            "(9): INTNUM (1)",
            "(9): , (,)",
            "(9): INTNUM (2)",
            "(9): , (,)",
            "(9): INTNUM (3)",
            "(9): ] (])",
            "(9): , (,)",
            "(10): [ ([)",
            "(10): INTNUM (4)",
            "(10): , (,)",
            "(10): INTNUM (5)",
            "(10): , (,)",
            "(10): INTNUM (6)",
            "(10): ] (])",
            "(10): , (,)",
            "(11): [ ([)",
            "(11): INTNUM (7)",
            "(11): , (,)",
            "(11): INTNUM (8)",
            "(11): , (,)",
            "(11): INTNUM (9)",
            "(11): ] (])",
            "(11): ] (])",
            "(11): ; (;)",
            "(13): ID (res1)",
            "(13): = (=)",
            "(13): FLOAT (60.5)",
            "(13): ; (;)",
            "(14): ID (res2)",
            "(14): = (=)",
            "(14): FLOAT (60.0)",
            "(14): ; (;)",
            "(15): ID (res3)",
            "(15): = (=)",
            "(15): FLOAT (0.5)",
            "(15): ; (;)",
            "(16): ID (res4)",
            "(16): = (=)",
            "(16): FLOAT (60.52)",
            "(16): ID (E2)",
            "(16): ; (;)",
            "(17): ID (str)",
            "(17): = (=)",
            "(17): STRING (Hello world)",
            "(17): ; (;)",
            "(19): IF (if)",
            "(19): ( (()",
            "(19): ID (m)",
            "(19): EQ (==)",
            "(19): ID (n)",
            "(19): ) ())",
            "(19): { ({)",
            "(20): IF (if)",
            "(20): ( (()",
            "(20): ID (m)",
            "(20): GE (>=)",
            "(20): ID (n)",
            "(20): ) ())",
            "(21): PRINT (print)",
            "(21): ID (res)",
            "(21): ; (;)",
            "(22): } (})"
        ]
        self.assertLexerOutput(code, expected_output)

    def test_parser_detects_incorrect_literals(self):
        code = """res2 = @res1;
            dolars = 100$;
            percentage = 5%;
            """
        expected_output = [
            "(1): ID (res2)",
            "(1): = (=)",
            "(1): ID (res1)",
            "(1): ; (;)",
            "(2): ID (dolars)",
            "(2): = (=)",
            "(2): INTNUM (100)",
            "(2): ; (;)",
            "(3): ID (percentage)",
            "(3): = (=)",
            "(3): INTNUM (5)",
            "(3): ; (;)",
            "Parse error at line 1. Unexpected character: @",
            "Parse error at line 2. Unexpected character: $",
            "Parse error at line 3. Unexpected character: %",
        ]
        self.assertLexerOutput(code, expected_output)


if __name__ == '__main__':
    unittest.main()
