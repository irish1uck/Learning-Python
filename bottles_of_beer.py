


def bottles_of_beer(bob):
    if bob == 1:
        print("""1 bottle of beer on the wall.
1 bottle of beer.
Take one down,
pass it around,
No more bottles of beer.

No more bottles
of beer on the wall.
No more bottles of beer.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall.
{} bottles of beer.
Take one down,
pass it around,
{} bottles of beer on the wall.
""".format(tmp, tmp, bob))
    bottles_of_beer(bob)
