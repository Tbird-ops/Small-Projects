#Shows the usefulness of asserts to catch errors that may break the
#program somewhere later down the line.

def no_negatives(number):
    assert isinstance(number, int), 'non-integer value passed to noNegatives() function!'
    assert number >= 0, 'negative value passed to the noNegatives() function!'
    print(number)

no_negatives(5)
no_negatives("hello")
no_negatives("-2")