import re
import shelve


def cleanup(words):  # Clean up the input
    if "s" in words:
        words.remove("s")
    if "is" in words:
        words.remove("is")


def relationship(relation):  # analyse the relationship and assign an id
    global gen
    global sibling
    global cousin
    global removal
    global data
    great = "great"
    grand = "grand"

    print(child, relation, parent)

    if child not in data:
        child_id = [gen, sibling, cousin, removal]
        data[child] = child_id
        print(child_id)
    else:
        child_id = data[child]
    if parent not in data:
        gen += len(re.findall(great, relation)) + len(re.findall(grand, relation))
        if re.search("father", relation) or re.search("mother", relation) or re.search("uncle", relation) or re.search("aunt", relation):
            gen += 1
        if re.search("aunt", relation) or re.search("uncle", relation) or re.search("sister", relation) or re.search("brother", relation):
            sibling += 1
        if re.search("cousin", relation):
            cousin += 1
        # if re.search(, relation):
        #     cousin += list(nth.keys())[list(nth.values()).index("second")]-1

        parent_id = [gen + child_id[0], sibling, cousin, removal]
        data[parent] = parent_id
        print(parent_id)


gen = 0
sibling = 0
cousin = 0
removal = 0
sibling = 0
d = shelve.open('database')
nth = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth"
    # etc
}



statement = input("Relationship?")

words = re.split("\W+", statement)
cleanup(words)

child = words[0:2]
parent = words[-2:]
relation = words[2:-2]

child = ' '.join(child)
parent = ' '.join(parent)
relation = ' '.join(relation)

child = child.title()
parent = parent.title()

data = d

relationship(relation)

d.update(data)
d.close()

"""Things to add:
    If spouse or new surname +1 family marker
    Who is X's father/cousin/etc.?
    What is X to Y?
    Family tree generator using plotly maybe"""