# Python Identifier Anonymizer

A Python library to anonymize and normalize identifiers in Python source code.

## Installation

```sh
pip install git+https://github.com/ashirafj/python-identifier-anonymizer
```

## Usage

```py
import anonymizer

anonymized_code, identifiers_map = anonymizer.anonymize(code)
```

## Example

You can refer to the example program, [example.py](https://github.com/ashirafj/python-identifier-anonymizer/blob/master/example.py)

### Original code

The following source code is the original (input) source code to be anonymized.

```py
# get values
a, b = map(int, input().split())

# calculate the area and perimeter
area = a * b
perimeter = 2 * (a + b)

# output the result
print(area, perimeter)
```

### Anonymized code

The following source code is the anonymized (output) source code.

Please note that it also normalizes (removes) some tokens, such as comments, white lines, and white spaces.

```py
VAR00, VAR01 = map(int, input().split())
VAR02 = VAR00 * VAR01
VAR03 = 2 * (VAR00 + VAR01)
print(VAR02, VAR03)
```

### Identifier Map

The identifier map of the anonymization is as follows. It maps anonymized identifiers to original identifiers.

| Anonymized | Original |
| - | - |
| `VAR00` | `a` |
| `VAR01` | `b` |
| `VAR02` | `area` |
| `VAR03` | `perimeter` |

## Acknowledgments

This project is inspired by [pycodesuggest](https://github.com/uclnlp/pycodesuggest) and replicated a part of the code.
We are grateful to the authors for their work.
