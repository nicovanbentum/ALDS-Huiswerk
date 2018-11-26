def uint_to_binary(integer):

    assert integer >= 0, "Parameter 'integer' can't take signed values"

    if integer == 0:
        return '0b'

    return uint_to_binary(integer // 2) + str((integer % 2))

print(uint_to_binary(5))
print(uint_to_binary(20))
print(uint_to_binary(64))
