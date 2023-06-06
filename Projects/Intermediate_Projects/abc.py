def find_indices(l, value):

    return [
        index for index, item in enumerate(l)
        if item == value
    ]


# 👇️ [0, 2, 3]
print(find_indices(['one', 'two', 'one', 'one', 'one']))

# 👇️ []
print(find_indices(['one', 'two', 'one', 'one'], 'abc'))
