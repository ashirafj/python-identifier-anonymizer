import anonymizer

code = """# get values
a, b = map(int, input().split())

# calculate the area and perimeter
area = a * b
perimeter = 2 * (a + b)

# output the result
print(area, perimeter)
"""

print("========== Original Code ==========")
print(code)
print("========== Anonymized Code ==========")
anonymized_code, identifiers_map = anonymizer.anonymize(code)
print(anonymized_code)
print("========== Identifier Map ==========")
print(identifiers_map)
