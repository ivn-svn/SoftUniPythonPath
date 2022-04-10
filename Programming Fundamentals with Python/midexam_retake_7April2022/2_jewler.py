pairs_of_earrings = 0
white_gold = input().split(' ')
yellow_gold = input().split(' ')
white_gold_ints = [int(x) for x in white_gold]
yellow_gold_ints = [int(y) for y in yellow_gold]
leftover = 0
decreased = 5
while True:
    for num in range(0, len(white_gold)):
        white = white_gold_ints[num]
        yellow = yellow_gold_ints[num]
        mint = white + yellow
        if mint == 10:
            pairs_of_earrings += 1
        elif mint > 10:
            while mint >= 10 and decreased > 0:
                decreased -= 1
                if yellow >= 2:
                    yellow -= 2
                    mint = yellow + white
                    # leftover += 2
                # else:
                #     break

                if mint == 10:
                    pairs_of_earrings += 1
                    mint = yellow + white
                elif mint < 10:
                    leftover += mint
        elif mint < 10:
            leftover += mint

    if leftover > 10:
        leftovermints = leftover // 10
        leftover = leftover - (10 * leftovermints)
        if mint < 10:
            leftover += mint
        pairs_of_earrings += leftovermints

    if pairs_of_earrings >= 7:
        print(f"Great success, you created {pairs_of_earrings} earrings.")
        break
    else:
        earrings_needed = 7 - pairs_of_earrings
        print(f"Keep trying, you need {earrings_needed} more earrings.")
        break
        # Not sure if I should end cycle if earrings are not enough!