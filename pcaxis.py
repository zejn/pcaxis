"""
usage:

from pcaxis import axis_parser

axis_parser.parseString('...')
axis_parser.parseFile(open(fn))


or run with python axis.py <dataset>
"""

import pyparsing
from pyparsing import Keyword, Word, alphas, nums, alphanums, Regex, Literal, OneOrMore, Suppress, Group, Dict, Optional, White

def parseData(s):
	lines = []
	cur = 0
	d = s[0]
	total = len(d)
	
	data_array = []
	dline = []
	while cur < total:
		#print cur
		if d[cur] == '"':
			next = cur + 1
			while next < total and d[next] != '"':
				next += 1
			dline.append(d[cur+1:next])
			cur = next + 1 + 1
		elif d[cur] == " ":
			#pass
			cur += 1
		elif d[cur] in '0123456789.-':
			next = cur
			while next < total and d[next] in '0123456789.-':
				next += 1
			dline.append(float(d[cur:next]))
			cur = next + 1
			#print dline[-1]
		elif d[cur] in '\r\n':
			while d[cur] in '\r\n':
				cur += 1
			#print dline
			data_array.append(dline)
			dline = []
	return data_array

NEWLINE = Literal("\n") | Literal("\r\n")
EQUAL = Suppress(Literal('='))
QUOTE = Suppress(Literal('"'))
SEMI = Suppress(Literal(";"))
BPAREN = Suppress(Literal("("))
EPAREN = Suppress(Literal(")"))
COMMA = Suppress(Literal(","))
YES = Literal("YES")
NO = Literal("NO")
INTEGER = Word(nums+'-', nums)
INTEGER.setParseAction(lambda x: int(x[0]))
FLOAT = Regex('-?[\d\.]+')
FLOAT.setParseAction(lambda x: float(x[0]))
NONQUOTE = Regex('[^"]+')
QSTRING = QUOTE + NONQUOTE + QUOTE # quoted string
MLQSTRING = OneOrMore(QSTRING | NEWLINE) # multiline quoted string
DATE = QUOTE + Word(nums + ': ', exact=14) + QUOTE

BQ = EQUAL + QUOTE
EQ = QUOTE + SEMI
BPQ = BPAREN + QUOTE
EPQ = QUOTE + EPAREN

tlist = Keyword("TLIST") + Group(BPAREN + Word("AHQMW1") + ((COMMA + QSTRING + Literal("-") + QSTRING + EPAREN) | (EPAREN + OneOrMore(QSTRING | COMMA))))

axis_version = Keyword("AXIS-VERSION") + BQ + Word(nums) + EQ
charset = Keyword("CHARSET") + BQ + Literal("ANSI") + EQ
codes = Keyword("CODES") + BPAREN + QSTRING + EPAREN + EQUAL + Group(OneOrMore(QSTRING | NEWLINE | COMMA)) + SEMI
contact = Keyword("CONTACT") + Optional(BPAREN + QSTRING + EPAREN) + EQUAL + MLQSTRING + SEMI
contents = Keyword("CONTENTS") + EQUAL + QSTRING + SEMI
copyright = Keyword("COPYRIGHT") + EQUAL + (YES | NO) + SEMI
creation_date = Keyword("CREATION-DATE") + EQUAL + DATE + SEMI

DATA_VALUES = Regex('[^;]+')
DATA_VALUES.setParseAction(parseData)
data = Keyword("DATA") + EQUAL + Optional(Suppress(White())) + DATA_VALUES + SEMI

database = Keyword("DATABASE") + EQUAL + QSTRING + SEMI
datanotesum = Keyword("DATANOTESUM") + EQUAL + QSTRING + SEMI
datasymbol1 = Keyword("DATASYMBOL1") + EQUAL + QSTRING + SEMI
datasymbol2 = Keyword("DATASYMBOL2") + EQUAL + QSTRING + SEMI
datasymbol3 = Keyword("DATASYMBOL3") + EQUAL + QSTRING + SEMI
datasymbol4 = Keyword("DATASYMBOL4") + EQUAL + QSTRING + SEMI
datasymbol5 = Keyword("DATASYMBOL5") + EQUAL + QSTRING + SEMI
datasymbol6 = Keyword("DATASYMBOL6") + EQUAL + QSTRING + SEMI
datasymbolsum = Keyword("DATASYMBOLSUM") + EQUAL + QSTRING + SEMI
datasymbolnil = Keyword("DATASYMBOLNIL") + EQUAL + QSTRING + SEMI
decimals = Keyword("DECIMALS") + EQUAL + INTEGER + SEMI
description = Keyword("DESCRIPTION") + EQUAL + QSTRING + SEMI
descriptiondefault = Keyword("DESCRIPTIONDEFAULT") + EQUAL + YES + SEMI
directory_path = Keyword("DIRECTORY-PATH") + EQUAL + QSTRING + SEMI
domain = Keyword("DOMAIN") + BPAREN + QSTRING + EPAREN + EQUAL + QSTRING + SEMI
elimination = Keyword("ELIMINATION") + BPAREN + QSTRING + EPAREN + EQUAL + (QSTRING | YES) + SEMI
euro = Keyword("EURO") + EQUAL + QSTRING + SEMI
heading = Keyword("HEADING") + EQUAL + OneOrMore(QSTRING | COMMA) + SEMI
infofile = Keyword("INFOFILE") + EQUAL + QSTRING + SEMI
language = Keyword("LANGUAGE") + BQ + Word(alphas, exact=2) + EQ
last_updated = Keyword("LAST-UPDATED") + EQUAL + DATE + SEMI
matrix = Keyword("MATRIX") + EQUAL + QSTRING + SEMI
note = Keyword("NOTE") + EQUAL + MLQSTRING + SEMI
notex = Keyword("NOTEX") + Optional(BPAREN + QSTRING + EPAREN) + EQUAL + MLQSTRING + SEMI
precision = Keyword("PRECISION") + BPAREN + QSTRING + COMMA + QSTRING + EPAREN + EQUAL + INTEGER + SEMI
showdecimals = Keyword("SHOWDECIMALS") + EQUAL + INTEGER + SEMI
source = Keyword("SOURCE") + EQUAL + QSTRING + SEMI
stub = Keyword("STUB") + EQUAL + OneOrMore(QSTRING | COMMA) + SEMI
subject_area = Keyword("SUBJECT-AREA") + EQUAL + QSTRING + SEMI
subject_code = Keyword("SUBJECT-CODE") + EQUAL + QSTRING + SEMI
timeval = Keyword("TIMEVAL") + BPAREN + QSTRING + EPAREN + EQUAL + tlist + SEMI
title = Keyword("TITLE") + EQUAL + QSTRING + SEMI
units = Keyword("UNITS") + EQUAL + QSTRING + SEMI
valuenotex = Keyword("VALUENOTEX") + BPAREN + QSTRING + COMMA + QSTRING + EPAREN + EQUAL + MLQSTRING + SEMI
values = Keyword("VALUES") + BPAREN + QSTRING + EPAREN + EQUAL + Group(OneOrMore(QSTRING | NEWLINE | COMMA)) + SEMI
variable_type = Keyword("VARIABLE-TYPE") + BPAREN + QSTRING + EPAREN + EQUAL + QSTRING + SEMI



axis_parser = OneOrMore(
	Group(axis_version("AXIS-VERSION")) | \
	Group(charset("CHARSET")) | \
	Group(codes("CODES")) | \
	Group(contact("CONTACT")) | \
	Group(contents("CONTENTS")) | \
	Group(copyright("COPYRIGHT")) | \
	Group(creation_date("CREATION-DATE")) | \
	Group(data("DATA")) | \
	Group(database("DATABASE")) | \
	Group(datanotesum("DATANOTESUM")) | \
	Group(datasymbol1("DATASYMBOL1")) | \
	Group(datasymbol2("DATASYMBOL2")) | \
	Group(datasymbol3("DATASYMBOL3")) | \
	Group(datasymbol4("DATASYMBOL4")) | \
	Group(datasymbol5("DATASYMBOL5")) | \
	Group(datasymbol6("DATASYMBOL6")) | \
	Group(datasymbolsum("DATASYMBOLSUM")) | \
	Group(datasymbolnil("DATASYMBOLNIL")) | \
	Group(decimals("DECIMALS")) | \
	Group(description("DESCRIPTION")) | \
	Group(descriptiondefault("DESCRIPTIONDEFAULT")) | \
	Group(directory_path("DIRECTORY-PATH")) | \
	Group(domain("DOMAIN")) | \
	Group(elimination("ELIMINATION")) | \
	Group(euro("EURO")) | \
	Group(heading("HEADING")) | \
	Group(infofile("INFOFILE")) | \
	Group(language("LANGUAGE")) | \
	Group(last_updated("LAST-UPDATED")) | \
	Group(matrix("MATRIX")) | \
	Group(note("NOTE")) | \
	Group(notex("NOTEX")) | \
	Group(precision("PRECISION")) | \
	Group(showdecimals("SHOWDECIMALS")) | \
	Group(source("SOURCE")) | \
	Group(stub("STUB")) | \
	Group(subject_area("SUBJECT-AREA")) | \
	Group(subject_code("SUBJECT-CODE")) | \
	Group(timeval("TIMEVAL")) | \
	Group(title("TITLE")) | \
	Group(units("UNITS")) | \
	Group(valuenotex("VALUENOTEX")) | \
	Group(values("VALUES")) | \
	Group(variable_type("VARIABLE-TYPE")) | \
	NEWLINE
	)



if __name__ == "__main__":
	
	tests = """CHARSET="ANSI";
AXIS-VERSION="2004";
LANGUAGE="sl";
CREATION-DATE="20050311 10:30";
SUBJECT-AREA="TRG DELA";
SUBJECT-CODE="07010";
MATRIX="0701011";
TIMEVAL("MESEC")=TLIST(M1,"200801"-"201108");"""
	#for testcase in tests.split("\n"):
		#print [testcase]
		#print axis_parser.parseString(testcase)
	
	import sys
	outfile = hasattr(sys, 'pypy_version_info') and 'pypy' or 'cpython'
	fn = sys.argv[1]
	d = open(fn).read()
	result = axis_parser.parseString(d)
	#print >> open(outfile + '_repr.txt', 'w'), repr(result)
	#print >> open(outfile + '_str.txt', 'w'), str(result)
	#print >> open(outfile + '.txt', 'w'), result
	print result

