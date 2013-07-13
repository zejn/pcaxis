
import unittest
import os
import pprint

here = lambda x: os.path.join(os.path.dirname(__file__), x)

class TestPCAxis(unittest.TestCase):
    def test_simple(self):
        import pcaxis
        
        px_1 = """CHARSET="ANSI";
AXIS-VERSION="2004";
LANGUAGE="sl";
CREATION-DATE="20050311 10:30";
SUBJECT-AREA="TRG DELA";
SUBJECT-CODE="07010";
MATRIX="0701011";
TIMEVAL("MESEC")=TLIST(M1,"200801"-"201108");"""


        data = pcaxis.pcaxis_parser.parseString(px_1)
        print data
    
    def test_file(self):
        import pcaxis
        
        px_2 = open(here('testdata/imena_moska_05X1005S.px')).read()
        #data = pcaxis.pcaxis_parser.parseString(px_2)
        data = pcaxis.parsePX(px_2, encoding='cp1250')
        pprint.pprint(data)
    
    def test_parseDataLine(self):
        import pcaxis
        struct_len = (5, 2)
        dline = [14.0,16.0,16.0,18.0,22.0,1669.0,1564.0,1610.0,1511.0,1376.0]
        expected = [[14.0, 16.0, 16.0, 18.0, 22.0], [1669.0, 1564.0, 1610.0, 1511.0, 1376.0]]
        dline2 = pcaxis.parseDataLine(dline, struct_len)
        self.assertEqual(dline2, expected)

if __name__ == "__main__":
    unittest.main()