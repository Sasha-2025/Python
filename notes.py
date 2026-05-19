def no_notes(amount):

    notes = [2000, 500, 200, 100, 50, 20, 10]
    x =0

    for i in range(7):
        q =notes[i]

        x = amount // q
        print("Notes of {} = {}".format(q, x))
        amount = amount % q

no_notes(2660)