def find_matching_hash():
    hash_values = dict()

    for i in range(1, 10000000000000000):
        x = i/10000000000000000
        hashed_value = hash(x) % (2**32)

        if hashed_value in hash_values: #found duplicate entry
            print_x = repr(x) #reader says wrapping a float in repr() gets rid of the scientific notation but this does not actually work ?
            print_y = repr(hash_values[hashed_value])
            print("float values " + print_x + " and " + print_y + " share the same hash: " + str(hashed_value))
            return
        else:
            hash_values[hashed_value] = x

find_matching_hash()