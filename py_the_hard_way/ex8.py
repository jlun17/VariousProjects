formatter = "%r %r %r %r"

# 1 2 3 4
print formatter % (1,2,3,4)
# 'one' 'two' 'three' 'four'
print formatter % ("one", "two", "three", "four")
# True False False True
print formatter % (True, False, False, True)
# '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
print formatter % (formatter, formatter, formatter, formatter)
# 'I had this thing.' 'That you could type up right.' 'But it didn't sing.' 'So I said goodnight.'
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
