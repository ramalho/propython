#!/usr/bin/env python
# -*- coding: iso-8859-1 -*- 

from string import maketrans, translate

dic_cp1252 = {  # char : (unicode, mac, ascii, entity)
    '\x80':(u'\u20AC', '\xDB', '_', 'euro'  ), #euro sign (CP1252); added by LR
    '\x82':(u'\u201A', '\xE2', '_', 'sbquo' ), #single low-9 quotation mark, u+201A NEW 
    '\x83':(u'\u0192', '\xC4', 'f', 'fnof'  ), #latin small f with hook, =function, =florin, u+0192 ISOtech 
    '\x84':(u'\u201E', '\xE3', '_', 'bdquo' ), #double low-9 quotation mark, u+201E NEW 
    '\x85':(u'\u2026', '\xC9', '_', 'hellip'), #horizontal ellipsis, =three dot leader, u+2026 ISOpub  
    '\x86':(u'\u2020', '\xA0', '_', 'dagger'), #dagger, u+2020 ISOpub 
    '\x87':(u'\u2021', '\xE0', '_', 'Dagger'), #double dagger, u+2021 ISOpub 
    '\x88':(u'\u02C6', '\xF6', '^', 'circ'  ), #modifier letter circumflex accent, u+02C6 ISOpub 
    '\x89':(u'\u2030', '\xE4', '_', 'permil'), #per mille sign, u+2030 ISOtech 
    '\x8A':(u'\u0160', None  , 'S', 'Scaron'), #latin capital letter s with caron, u+0160 ISOlat2 
    '\x8B':(u'\u2039', '\xDC', '<', 'lsaquo'), #single left-pointing angle quotation mark, u+2039 ISO proposed 
    '\x8C':(u'\u0152', '\xCE', '_', 'OElig' ), #latin capital ligature oe, u+0152 ISOlat2 
    '\x91':(u'\u2018', '\xD4', "'", 'lsquo' ), #left single quotation mark, u+2018 ISOnum 
    '\x92':(u'\u2019', '\xD5', "'", 'rsquo' ), #right single quotation mark, u+2019 ISOnum 
    '\x93':(u'\u201C', '\xD2', '"', 'ldquo' ), #left double quotation mark, u+201C ISOnum 
    '\x94':(u'\u201D', '\xD3', '"', 'rdquo' ), #right double quotation mark, u+201D ISOnum 
    '\x95':(u'\u2022', '\xA5', '-', 'bull'  ), #bullet, =black small circle, u+2022 ISOpub  
    '\x96':(u'\u2013', '\xD0', '-', 'ndash' ), #en dash, u+2013 ISOpub 
    '\x97':(u'\u2014', '\xD1', '-', 'mdash' ), #em dash, u+2014 ISOpub 
    '\x98':(u'\u02DC', '\xF7', '~', 'tilde' ), #small tilde, u+02DC ISOdia 
    '\x99':(u'\u2122', '\xAA', '_', 'trade' ), #trade mark sign, u+2122 ISOnum 
    '\x9A':(u'\u0161', None  , 's', 'scaron'), #latin small letter s with caron, u+0161 ISOlat2 
    '\x9B':(u'\u203A', '\xDD', '>', 'rsaquo'), #single right-pointing angle quotation mark, u+203A ISO proposed 
    '\x9C':(u'\u0153', '\xCF', '_', 'oelig' ), #latin small ligature oe, u+0153 ISOlat2 
    '\x9F':(u'\u0178', '\xD9', 'Y', 'Yuml'  ), #latin capital letter y with diaeresis, u+0178 ISOlat2 
    '\xA0':(u'\u00A0', '\xCA', '_', 'nbsp'  ), #no-break space 
    '\xA1':(u'\u00A1', '\xC1', '_', 'iexcl' ), #inverted exclamation mark 
    '\xA2':(u'\u00A2', '\xA2', '_', 'cent'  ), #cent sign 
    '\xA3':(u'\u00A3', '\xA3', '_', 'pound' ), #pound sterling sign 
    '\xA4':(u'\u00A4', None  , '_', 'curren'), #general currency sign 
    '\xA5':(u'\u00A5', '\xB4', '_', 'yen'   ), #yen sign 
    '\xA6':(u'\u00A6', None  , '_', 'brvbar'), #broken (vertical) bar 
    '\xA7':(u'\u00A7', '\xA4', '_', 'sect'  ), #section sign 
    '\xA8':(u'\u00A8', '\xAC', '_', 'uml'   ), #umlaut (dieresis) 
    '\xA9':(u'\u00A9', '\xA9', '_', 'copy'  ), #copyright sign 
    '\xAA':(u'\u00AA', '\xBB', '_', 'ordf'  ), #ordinal indicator, feminine 
    '\xAB':(u'\u00AB', '\xC7', '_', 'laquo' ), #angle quotation mark, left 
    '\xAC':(u'\u00AC', '\xC2', '_', 'not'   ), #not sign 
    '\xAD':(u'\u00AD', None  , '_', 'shy'   ), #soft hyphen 
    '\xAE':(u'\u00AE', '\xA8', '_', 'reg'   ), #registered sign 
    '\xAF':(u'\u00AF', '\xF8', '_', 'macr'  ), #macron 
    '\xB0':(u'\u00B0', '\xA1', '_', 'deg'   ), #degree sign 
    '\xB1':(u'\u00B1', '\xB1', '_', 'plusmn'), #plus-or-minus sign 
    '\xB2':(u'\u00B2', None  , '_', 'sup2'  ), #superscript two 
    '\xB3':(u'\u00B3', None  , '_', 'sup3'  ), #superscript three 
    '\xB4':(u'\u00B4', '\xAB', '_', 'acute' ), #acute accent 
    '\xB5':(u'\u00B5', '\xB5', '_', 'micro' ), #micro sign 
    '\xB6':(u'\u00B6', '\xA6', '_', 'para'  ), #pilcrow (paragraph sign) 
    '\xB7':(u'\u00B7', '\xE1', '_', 'middot'), #middle dot 
    '\xB8':(u'\u00B8', '\xFC', '_', 'cedil' ), #cedilla 
    '\xB9':(u'\u00B9', None  , '_', 'sup1'  ), #superscript one 
    '\xBA':(u'\u00BA', '\xBC', '_', 'ordm'  ), #ordinal indicator, masculine 
    '\xBB':(u'\u00BB', '\xC8', '_', 'raquo' ), #angle quotation mark, right 
    '\xBC':(u'\u00BC', None  , '_', 'frac14'), #fraction one-quarter 
    '\xBD':(u'\u00BD', None  , '_', 'frac12'), #fraction one-half 
    '\xBE':(u'\u00BE', None  , '_', 'frac34'), #fraction three-quarters 
    '\xBF':(u'\u00BF', '\xC0', '_', 'iquest'), #inverted question mark 
    '\xC0':(u'\u00C0', '\xCB', 'A', 'Agrave'), #capital A, grave accent 
    '\xC1':(u'\u00C1', '\xE7', 'A', 'Aacute'), #capital A, acute accent 
    '\xC2':(u'\u00C2', '\xE5', 'A', 'Acirc' ), #capital A, circumflex accent 
    '\xC3':(u'\u00C3', '\xCC', 'A', 'Atilde'), #capital A, tilde 
    '\xC4':(u'\u00C4', '\x80', 'A', 'Auml'  ), #capital A, dieresis or umlaut mark 
    '\xC5':(u'\u00C5', '\x81', 'A', 'Aring' ), #capital A, ring 
    '\xC6':(u'\u00C6', '\xAE', '_', 'AElig' ), #capital AE diphthong (ligature) 
    '\xC7':(u'\u00C7', '\x82', 'C', 'Ccedil'), #capital C, cedilla 
    '\xC8':(u'\u00C8', '\xE9', 'E', 'Egrave'), #capital E, grave accent 
    '\xC9':(u'\u00C9', '\x83', 'E', 'Eacute'), #capital E, acute accent 
    '\xCA':(u'\u00CA', '\xE6', 'E', 'Ecirc' ), #capital E, circumflex accent 
    '\xCB':(u'\u00CB', '\xE8', 'E', 'Euml'  ), #capital E, dieresis or umlaut mark 
    '\xCC':(u'\u00CC', '\xED', 'I', 'Igrave'), #capital I, grave accent 
    '\xCD':(u'\u00CD', '\xEA', 'I', 'Iacute'), #capital I, acute accent 
    '\xCE':(u'\u00CE', '\xEB', 'I', 'Icirc' ), #capital I, circumflex accent 
    '\xCF':(u'\u00CF', '\xEC', 'I', 'Iuml'  ), #capital I, dieresis or umlaut mark 
    '\xD0':(u'\u00D0', None  , '_', 'ETH'   ), #capital Eth, Icelandic 
    '\xD1':(u'\u00D1', '\x84', 'N', 'Ntilde'), #capital N, tilde 
    '\xD2':(u'\u00D2', '\xF1', 'O', 'Ograve'), #capital O, grave accent 
    '\xD3':(u'\u00D3', '\xEE', 'O', 'Oacute'), #capital O, acute accent 
    '\xD4':(u'\u00D4', '\xEF', 'O', 'Ocirc' ), #capital O, circumflex accent 
    '\xD5':(u'\u00D5', '\xCD', 'O', 'Otilde'), #capital O, tilde 
    '\xD6':(u'\u00D6', '\x85', 'O', 'Ouml'  ), #capital O, dieresis or umlaut mark 
    '\xD7':(u'\u00D7', None  , '_', 'times' ), #multiply sign 
    '\xD8':(u'\u00D8', '\xAF', 'O', 'Oslash'), #capital O, slash 
    '\xD9':(u'\u00D9', '\xF4', 'U', 'Ugrave'), #capital U, grave accent 
    '\xDA':(u'\u00DA', '\xF2', 'U', 'Uacute'), #capital U, acute accent 
    '\xDB':(u'\u00DB', '\xF3', 'U', 'Ucirc' ), #capital U, circumflex accent 
    '\xDC':(u'\u00DC', '\x86', 'U', 'Uuml'  ), #capital U, dieresis or umlaut mark 
    '\xDD':(u'\u00DD', None  , 'Y', 'Yacute'), #capital Y, acute accent 
    '\xDE':(u'\u00DE', None  , '_', 'THORN' ), #capital THORN, Icelandic 
    '\xDF':(u'\u00DF', '\xA7', '_', 'szlig' ), #small sharp s, German (sz ligature) 
    '\xE0':(u'\u00E0', '\x88', 'a', 'agrave'), #small a, grave accent 
    '\xE1':(u'\u00E1', '\x87', 'a', 'aacute'), #small a, acute accent 
    '\xE2':(u'\u00E2', '\x89', 'a', 'acirc' ), #small a, circumflex accent 
    '\xE3':(u'\u00E3', '\x8B', 'a', 'atilde'), #small a, tilde 
    '\xE4':(u'\u00E4', '\x8A', 'a', 'auml'  ), #small a, dieresis or umlaut mark 
    '\xE5':(u'\u00E5', '\x8C', 'a', 'aring' ), #small a, ring 
    '\xE6':(u'\u00E6', '\xBE', '_', 'aelig' ), #small ae diphthong (ligature) 
    '\xE7':(u'\u00E7', '\x8D', 'c', 'ccedil'), #small c, cedilla 
    '\xE8':(u'\u00E8', '\x8F', 'e', 'egrave'), #small e, grave accent 
    '\xE9':(u'\u00E9', '\x8E', 'e', 'eacute'), #small e, acute accent 
    '\xEA':(u'\u00EA', '\x90', 'e', 'ecirc' ), #small e, circumflex accent 
    '\xEB':(u'\u00EB', '\x91', 'e', 'euml'  ), #small e, dieresis or umlaut mark 
    '\xEC':(u'\u00EC', '\x93', 'i', 'igrave'), #small i, grave accent 
    '\xED':(u'\u00ED', '\x92', 'i', 'iacute'), #small i, acute accent 
    '\xEE':(u'\u00EE', '\x94', 'i', 'icirc' ), #small i, circumflex accent 
    '\xEF':(u'\u00EF', '\x95', 'i', 'iuml'  ), #small i, dieresis or umlaut mark 
    '\xF0':(u'\u00F0', None  , '_', 'eth'   ), #small eth, Icelandic 
    '\xF1':(u'\u00F1', '\x96', 'n', 'ntilde'), #small n, tilde 
    '\xF2':(u'\u00F2', '\x98', 'o', 'ograve'), #small o, grave accent 
    '\xF3':(u'\u00F3', '\x97', 'o', 'oacute'), #small o, acute accent 
    '\xF4':(u'\u00F4', '\x99', 'o', 'ocirc' ), #small o, circumflex accent 
    '\xF5':(u'\u00F5', '\x9B', 'o', 'otilde'), #small o, tilde 
    '\xF6':(u'\u00F6', '\x9A', 'o', 'ouml'  ), #small o, dieresis or umlaut mark 
    '\xF7':(u'\u00F7', '\xD6', '_', 'divide'), #divide sign 
    '\xF8':(u'\u00F8', '\xBF', 'o', 'oslash'), #small o, slash 
    '\xF9':(u'\u00F9', '\x9D', 'u', 'ugrave'), #small u, grave accent 
    '\xFA':(u'\u00FA', '\x9C', 'u', 'uacute'), #small u, acute accent 
    '\xFB':(u'\u00FB', '\x9E', 'u', 'ucirc' ), #small u, circumflex accent 
    '\xFC':(u'\u00FC', '\x9F', 'u', 'uuml'  ), #small u, dieresis or umlaut mark 
    '\xFD':(u'\u00FD', None  , 'y', 'yacute'), #small y, acute accent 
    '\xFE':(u'\u00FE', None  , '_', 'thorn' ), #small thorn, Icelandic 
    '\xFF':(u'\u00FF', '\xD8', 'y', 'yuml'  ), #small y, dieresis or umlaut mark 
}

chars_cp1252 = dic_cp1252.keys()
chars_cp1252.sort()
chars_cp1252 = ''.join(chars_cp1252)
 

###################### Codepage 1252 to ASCII translation setup

letters_cp1252 = []
letters_ascii = []
for char in chars_cp1252:  
    ascii = dic_cp1252[char][2]
    if ascii != '_':
        letters_cp1252.append(char)
        letters_ascii.append(ascii)
letters_cp1252 = ''.join(letters_cp1252)
letters_ascii = ''.join(letters_ascii)
        
TRANS_CP1252_ASCII = maketrans(letters_cp1252, letters_ascii)


###################### Codepage 1252 to MacRoman translation setup

chars_macRoman = [] # MacRoman filled with _ in missing positions
for char in chars_cp1252:
    mac = dic_cp1252[char][1]
    if mac == None:
        # replace characters missing in MacRoman with underscore
        mac = '_'
    chars_macRoman.append(mac)
chars_macRoman = ''.join(chars_macRoman)
    
TRANS_CP1252_MACROMAN = maketrans(chars_cp1252, chars_macRoman)


###################### MacRoman to Codepage 1252 translation setup

dic_macRoman = {}
for char in chars_cp1252:
    mac = dic_cp1252[char][1]
    if mac != None:
        # only characters defined in MacRoman (no fillers)
        dic_macRoman[mac] = char

chars_macRoman_only = dic_macRoman.keys()
chars_macRoman_only.sort()
chars_macRoman_only = ''.join(chars_macRoman_only)

chars_cp1252_mac = [] # CP1252 subset with MacRoman equivalents
for mac in chars_macRoman_only:
    char = dic_macRoman[mac]
    chars_cp1252_mac.append(char)
chars_cp1252_mac = ''.join(chars_cp1252_mac)

TRANS_MACROMAN_CP1252 = maketrans(chars_macRoman_only, chars_cp1252_mac)


###################### HTML entities to Codepage 1252 conversion setup

dic_entities = {}
for char in chars_cp1252:
    entity = dic_cp1252[char][3]
    dic_entities[entity] = char
    

###################### Codepage 1252 lower/uppercase translation setup

chars_upper = []
chars_lower = []
for entity in dic_entities.keys():
    # take advantage of entity names fo find out lowercase equivalents
    if entity != entity.lower():
        chars_upper.append(dic_entities[entity])
        chars_lower.append(dic_entities[entity.lower()])

chars_upper.sort()
chars_upper = ''.join(chars_upper)
chars_lower.sort()
chars_lower = ''.join(chars_lower)

TRANS_CP1252_UPPER = maketrans(chars_lower, chars_upper)
TRANS_CP1252_LOWER = maketrans(chars_upper, chars_lower)

###################### 
###################### Translation functions (public interface)
###################### 

def cp1252_macRoman(text):
    'translate Windows Codepage 1252 to MacRoman'
    return translate(text, TRANS_CP1252_MACROMAN)
    
def macRoman_cp1252(text):
    'translate MacRoman to Windows Codepage 1252'
    return translate(text, TRANS_MACROMAN_CP1252)
    
def cp1252_ascii(text):
    'translate Windows Codepage 1252 to plain ASCII'
    return translate(text, TRANS_CP1252_ASCII)
    
def macRoman_ascii(text):
    'translate MacRoman to plain ASCII'
    text = macRoman_cp1252(text)
    return cp1252_ascii(text)
    
def cp1252_upper(text):
    'translate Windows Codepage 1252 to uppercase CP1252'
    text = text.upper()
    return translate(text, TRANS_CP1252_UPPER) 

def cp1252_lower(text):
    'translate Windows Codepage 1252 to lowercase CP1252'
    text = text.lower()
    return translate(text, TRANS_CP1252_LOWER)
    
def cp1252_html(text):
    'translate Windows Codepage 1252 to HTML 4 entities'
    for char in chars_cp1252:
        if text.find(char) >= 0:
            text = text.replace(char, '&' + dic_cp1252[char][3] + ';')
    return text
     
def html_cp1252(text):
    'translate HTML 4 entities to Windows Codepage 1252'
    if text.find('&') >= 0 and text.find(';') > 1: # possible entities 
        for entity in dic_entities.keys():
            html_entity = '&' + entity + ';'
            if text.find(html_entity) >= 0:
                text = text.replace(html_entity, dic_entities[entity])
        return text
    else: # no HTML entities in text
        return text
    
###################### tests

def smoke_tests():
    print '<HTML><BODY>'
    
    mac = 'acentos: çƒêîò‡Ž’—œ‚  permil: \xE4 euro: \xDB  AElig: \xAE  copy: \xA9' 
    print 'Mac:', mac
    print '<BR>'
    
    win = macRoman_cp1252(mac)
    print 'Win:', win
    print '<BR>'
    
    ascii = cp1252_ascii(win)
    print 'ASCII:', ascii
    print '<BR>'
    
    upper = cp1252_upper(win)
    print 'UPPER:', upper 
    print '<BR>'

    lower = cp1252_lower(win)
    print 'lower:', lower 
    print '<BR>'
    
    html = cp1252_html(win)
    print 'to HTML:', html
    print '<BR>'
    
    text = html_cp1252(html)
    print 'from HTML:', text
    print '<BR>'
    
    print '</BODY></HTML>'

###################### MAIN

def main():
    import sys
    if len(sys.argv) != 3 or not sys.argv[1] in ['wm','wa','mw','ma']:
        script = sys.argv[0]
        print 'Usage:'
        print script, 'wm <filename>: convert file from Windows codepage 1252 to MacRoman'
        print script, 'wa <filename>: convert file from Windows codepage 1252 to ASCII'
        print script, 'mw <filename>: convert file from MacRoman to Windows codepage 1252'
        print script, 'ma <filename>: convert file from MacRoman to ASCII'
        sys.exit()
    else:
        opt = sys.argv[1]
        if   opt == 'wm': trans = cp1252_macRoman
        elif opt == 'wa': trans = cp1252_ascii
        elif opt == 'mw': trans = macRoman_cp1252
        elif opt == 'ma': trans = macRoman_ascii
        try:
            filename = sys.argv[2]
            text = open(filename).read()
        except IOError:
            print 'ERROR: unable to open file "%s"' % filename
            sys.exit(1)
        print trans(text)

if __name__ == '__main__':
    # smoke_tests()
    main()
            
'''
bugs: 
- o teste de upper e lower revela confusao entre AElig e ccedil    
    
    
'''



                   
