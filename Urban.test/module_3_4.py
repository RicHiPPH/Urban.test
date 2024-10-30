# Airborne, aIrplane, fareair, Backing, Backward
def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.startswith(i) or i.startswith(root_word):
            same_words.append(i)
    return same_words


print(single_root_words("air", "aIrplane", "fareair", "Backing", "Backward"))
print(single_root_words('Disablement', "Able", "Mable", "Disable", "Bagel"))

# slou = ("aIrplane", "fareair", "Backing", "Backward")
