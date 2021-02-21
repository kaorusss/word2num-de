# word2num-de
EN
- Transforms written numbers in German to numbers.
- Works for numbers 0-9999

DE
- Übersetzt ausgeschriebene Zahlen in (auf Deutsch) in Zahlen
- Unterstützt Zahlen zwischen 0 und 9999.

Implementation based on the following project: https://github.com/IBM/wort-to-number

## Installation

Package can be installed using pip.

```bash
pip install word2num-de
```

## Usage example

Import the main function word_to_number.

```
from word2num_de import word_to_number
```

The function returns the written-out number in digits (as a string).

```
print(word_to_number("sechshunderteinundzwanzig"))
'621'
```

```
print(word_to_number("sechshunderteinundzwanzig"))
'621'
```
