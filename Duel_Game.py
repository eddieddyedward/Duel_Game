import random
from collections import Counter
import argparse

def damage_reduction(att1, def2, hp2):
    hp2 -= (att1 - def2)/2
    return hp2

def power_strike(att1, def2, hp2):
    hp2 -= (att1 + att1/2 - def2)
    return hp2

def second_wind(att1, def2, hp2):
    hp2 -= att1 - def2
    hp2 += 5
    return hp2

def power_reduction(att1, def2, hp2): # combination of power strike and damage reduction
    hp2 -= (att1 + att1/2 - def2)/2
    return hp2

def power_wind(att1, def2, hp2): # combination of power strike and second wind
    hp2 -= (att1 + att1/2 - def2)
    hp2 += 5
    return hp2

def ultimate_attack(hp2): # 4th ability
    hp2 -= 100
    return hp2

def turns(att1, def2, hp2):
    hp2 -= att1 - def2
    return hp2

def special_ability(s):
    sa = random.choice([1, 2, 3, 4])  # 1 = damage reduction; 2 = power strike; 3 = second wind; 4 = ultimate attack
    # Ultimate Attack = when the character attacks, there is a 1% chance that the other character gets instantaneously killed
    match sa:
        case 1:
            print(f"Character {s} special ability: Damage Reduction")
        case 2:
            print(f"Character {s} special ability: Power Strike")
        case 3:
            print(f"Character {s} special ability: Second Wind")
        case 4:
            print(f"Character {s} special ability: Ultimate Attack")
    return sa

def setup_fixed():
    ap1 = random.randrange(15,21) # first character's attack power
    dp1 = random.randrange(10,16) # first character's defense power
    h1 = 100 # first character's health

    ap2 = random.randrange(15,21) # second character's attack power
    dp2 = random.randrange(10,16) # second character's defense power
    h2 = 100 # second character's health

    print(f"Character 1: attack = {ap1}, defense = {dp1}")
    print(f"Character 2: attack = {ap2}, defense = {dp2}")
    print()

    if ap1 - dp2 == 0 and ap2 - dp1 == 0:
        print("Tie")
        return "Tie"

    r = random.choice([1, 2]) # decide who is attacking first
    n = 1 # the number of the round
    check = 0 # verifies if the 25% condition is met for a single special ability
    check_both = 0 # verifies if the 6.25% condition is met for a combination of 2 special abilities
    sa1 = special_ability(1)
    sa2 = special_ability(2)
    print()

    if r == 1:
        print(f"Round {n}:")
        print("Character 1 attacks")

        if sa1 == 2 and sa2 == 1 and random.random() < 0.0625:
            print("Character 1 activates Power Strike")
            print("Character 2 activates Damage Reduction")
            h2 = power_reduction(ap1, dp2, h2)
            check_both = 1

        if check_both == 0:
            if sa1 == 2 and random.random() < 0.25:
                print("Character 1 activates Power Strike")
                h2 = power_strike(ap1, dp2, h2)
                check = 1
            if sa2 == 1 and random.random() < 0.25 and check == 0:
                print("Character 2 activates Damage Reduction")
                h2 = damage_reduction(ap1, dp2, h2)
                check = 1
            # Ultimate Attack
            if sa1 == 4 and random.random() < 0.01 and check == 0:
                print("Character 1 activates Ultimate Attack")
                h2 = ultimate_attack(h2)
                check = 1

        if check == 0 and check_both == 0:
            print("No ability activated")
            h2 = turns(ap1, dp2, h2)
        else:
            check = 0
            check_both = 0

        print(f"Character 2 has {h2} health")
        print()
        n += 1

    else:
        print(f"Round {n}:")
        print("Character 2 attacks")

        if sa2 == 2 and sa1 == 1 and random.random() < 0.0625:
            print("Character 2 activates Power Strike")
            print("Character 1 activates Damage Reduction")
            h1 = power_reduction(ap2, dp1, h1)
            check_both = 1

        if check_both == 0:
            if sa2 == 2 and random.random() < 0.25:
                print("Character 2 activates Power Strike")
                h1 = power_strike(ap2, dp1, h1)
                check = 1
            if sa1 == 1 and random.random() < 0.25 and check == 0:
                print("Character 1 activates Damage Reduction")
                h1 = damage_reduction(ap2, dp1, h1)
                check = 1
            # Ultimate Attack
            if sa2 == 4 and random.random() < 0.01 and check == 0:
                print("Character 2 activates Ultimate Attack")
                h1 = ultimate_attack(h1)
                check = 1

        if check == 0 and check_both == 0:
            print("No ability activated")
            h1 = turns(ap2, dp1, h1)
        else:
            check = 0
            check_both = 0

        print(f"Character 1 has {h1} health")
        print()
        n += 1

    if r == 1:
        while h1 > 0 and h2 > 0:
            print(f"Round {n}:")
            print(f"Character 2 attacks")

            if sa2 == 2 and sa1 == 1 and random.random() < 0.0625:
                print("Character 2 activates Power Strike")
                print("Character 1 activates Damage Reduction")
                h1 = power_reduction(ap2, dp1, h1)
                check_both = 1
            if sa2 == 2 and sa1 == 3 and random.random() < 0.0625 and h1 < 30:
                print("Character 2 activates Power Strike")
                print("Character 1 activates Second Wind")
                h1 = power_wind(ap2, dp1, h1)
                check_both = 1

            if check_both == 0:
                if sa2 == 2 and random.random() < 0.25:
                    print("Character 2 activates Power Strike")
                    h1 = power_strike(ap2, dp1, h1)
                    check = 1
                if sa1 == 1 and random.random() < 0.25 and check == 0:
                    print("Character 1 activates Damage Reduction")
                    h1 = damage_reduction(ap2, dp1, h1)
                    check = 1
                if sa1 == 3 and random.random() < 0.25 and h1 < 30 and check == 0:
                    print("Character 1 activates Second Wind")
                    h1 = second_wind(ap2, dp1, h1)
                    check = 1
                # Ultimate Attack
                if sa2 == 4 and random.random() < 0.01 and check == 0:
                    print("Character 2 activates Ultimate Attack")
                    h1 = ultimate_attack(h1)
                    check = 1

            if check == 0 and check_both == 0:
                print("No ability activated")
                h1 = turns(ap2, dp1, h1)
            else:
                check = 0
                check_both = 0

            print(f"Character 1 has {h1} health")
            print()
            n += 1

            if h1 <= 0 or h2 <= 0:
                break

            print(f"Round {n}:")
            print(f"Character 1 attacks")

            if sa1 == 2 and sa2 == 1 and random.random() < 0.0625:
                print("Character 1 activates Power Strike")
                print("Character 2 activates Damage Reduction")
                h2 = power_reduction(ap1, dp2, h2)
                check_both = 1
            if sa1 == 2 and sa2 == 3 and random.random() < 0.0625 and h2 < 30:
                print("Character 1 activates Power Strike")
                print("Character 2 activates Second Wind")
                h2 = power_wind(ap1, dp2, h2)
                check_both = 1

            if check_both == 0:
                if sa1 == 2 and random.random() < 0.25:
                    print("Character 1 activates Power Strike")
                    h2 = power_strike(ap1, dp2, h2)
                    check = 1
                if sa2 == 1 and random.random() < 0.25 and check == 0:
                    print("Character 2 activates Damage Reduction")
                    h2 = damage_reduction(ap1, dp2, h2)
                    check = 1
                if sa2 == 3 and random.random() < 0.25 and h2 < 30 and check == 0:
                    print("Character 2 activates Second Wind")
                    h2 = second_wind(ap1, dp2, h2)
                    check = 1
                # Ultimate Attack
                if sa1 == 4 and random.random() < 0.01 and check == 0:
                    print("Character 1 activates Ultimate Attack")
                    h2 = ultimate_attack(h2)
                    check = 1

            if check == 0 and check_both == 0:
                print("No ability activated")
                h2 = turns(ap1, dp2, h2)
            else:
                check = 0
                check_both = 0

            print(f"Character 2 has {h2} health")
            print()
            n += 1
    else:
        while h1 > 0 and h2 > 0:
            print(f"Round {n}:")
            print(f"Character 1 attacks")

            if sa1 == 2 and sa2 == 1 and random.random() < 0.0625:
                print("Character 1 activates Power Strike")
                print("Character 2 activates Damage Reduction")
                h2 = power_reduction(ap1, dp2, h2)
                check_both = 1
            if sa1 == 2 and sa2 == 3 and random.random() < 0.0625 and h2 < 30:
                print("Character 1 activates Power Strike")
                print("Character 2 activates Second Wind")
                h2 = power_wind(ap1, dp2, h2)
                check_both = 1

            if check_both == 0:
                if sa1 == 2 and random.random() < 0.25:
                    print("Character 1 activates Power Strike")
                    h2 = power_strike(ap1, dp2, h2)
                    check = 1
                if sa2 == 1 and random.random() < 0.25 and check == 0:
                    print("Character 2 activates Damage Reduction")
                    h2 = damage_reduction(ap1, dp2, h2)
                    check = 1
                if sa2 == 3 and random.random() < 0.25 and h2 < 30 and check == 0:
                    print("Character 2 activates Second Wind")
                    h2 = second_wind(ap1, dp2, h2)
                    check = 1
                # Ultimate Attack
                if sa1 == 4 and random.random() < 0.01 and check == 0:
                    print("Character 1 activates Ultimate Attack")
                    h2 = ultimate_attack(h2)
                    check = 1

            if check == 0 and check_both == 0:
                print("No ability activated")
                h2 = turns(ap1, dp2, h2)
            else:
                check = 0
                check_both = 0

            print(f"Character 2 has {h2} health")
            print()
            n += 1

            if h1 <= 0 or h2 <= 0:
                break

            print(f"Round {n}:")
            print(f"Character 2 attacks")

            if sa2 == 2 and sa1 == 1 and random.random() < 0.0625:
                print("Character 2 activates Power Strike")
                print("Character 1 activates Damage Reduction")
                h1 = power_reduction(ap2, dp1, h1)
                check_both = 1
            if sa2 == 2 and sa1 == 3 and random.random() < 0.0625 and h1 < 30:
                print("Character 2 activates Power Strike")
                print("Character 1 activates Second Wind")
                h1 = power_wind(ap2, dp1, h1)
                check_both = 1

            if check_both == 0:
                if sa2 == 2 and random.random() < 0.25:
                    print("Character 2 activates Power Strike")
                    h1 = power_strike(ap2, dp1, h1)
                    check = 1
                if sa1 == 1 and random.random() < 0.25 and check == 0:
                    print("Character 1 activates Damage Reduction")
                    h1 = damage_reduction(ap2, dp1, h1)
                    check = 1
                if sa1 == 3 and random.random() < 0.25 and h1 < 30 and check == 0:
                    print("Character 1 activates Second Wind")
                    h1 = second_wind(ap2, dp1, h1)
                    check = 1
                # Ultimate Attack
                if sa2 == 4 and random.random() < 0.01 and check == 0:
                    print("Character 2 activates Ultimate Attack")
                    h1 = ultimate_attack(h1)
                    check = 1

            if check == 0 and check_both == 0:
                print("No ability activated")
                h1 = turns(ap2, dp1, h1)
            else:
                check = 0
                check_both = 0

            print(f"Character 1 has {h1} health")
            print()
            n += 1

    print()
    if h1 <= 0:
        print("Character 2 won")
        return 'Character 2'
    if h2 <= 0:
        print("Character 1 won")
        return 'Character 1'
    return None


def setup_per_round():
    ap1 = random.randrange(15,21) # first character's attack power
    dp1 = random.randrange(10,16) # first character's defense power
    h1 = 100 # first character's health

    ap2 = random.randrange(15,21) # second character's attack power
    dp2 = random.randrange(10,16) # second character's defense power
    h2 = 100 # second character's health

    if ap1 - dp2 == 0 and ap2 - dp1 == 0:
        print("Tie")
        return "Tie"

    print(f"Character 1: attack = {ap1}, defense = {dp1}")
    print(f"Character 2: attack = {ap2}, defense = {dp2}")
    print()

    r = random.choice([1, 2]) # decide who is attacking first
    n = 1 # the number of the round
    check = 0 # verifies if the 25% condition is met for a single special ability
    check_both = 0 # verifies if the 6.25% condition is met for a combination of 2 special abilities

    if r == 1:
        print(f"Round {n}:")
        print()
        sa1 = special_ability(1)
        sa2 = special_ability(2)
        print()
        print("Character 1 attacks")

        if sa1 == 2 and sa2 == 1 and random.random() < 0.0625:
            print("Character 1 activates Power Strike")
            print("Character 2 activates Damage Reduction")
            h2 = power_reduction(ap1, dp2, h2)
            check_both = 1

        if check_both == 0:
            if sa1 == 2 and random.random() < 0.25:
                print("Character 1 activates Power Strike")
                h2 = power_strike(ap1, dp2, h2)
                check = 1
            if sa2 == 1 and random.random() < 0.25 and check == 0:
                print("Character 2 activates Damage Reduction")
                h2 = damage_reduction(ap1, dp2, h2)
                check = 1
            # Ultimate Attack
            if sa1 == 4 and random.random() < 0.01 and check == 0:
                print("Character 1 activates Ultimate Attack")
                h2 = ultimate_attack(h2)
                check = 1

        if check == 0 and check_both == 0:
            print("No ability activated")
            h2 = turns(ap1, dp2, h2)
        else:
            check = 0
            check_both = 0

        print(f"Character 2 has {h2} health")
        print()
        n += 1

    else:
        print(f"Round {n}:")
        print()
        sa1 = special_ability(1)
        sa2 = special_ability(2)
        print()
        print("Character 2 attacks")

        if sa2 == 2 and sa1 == 1 and random.random() < 0.0625:
            print("Character 2 activates Power Strike")
            print("Character 1 activates Damage Reduction")
            h1 = power_reduction(ap2, dp1, h1)
            check_both = 1

        if check_both == 0:
            if sa2 == 2 and random.random() < 0.25:
                print("Character 2 activates Power Strike")
                h1 = power_strike(ap2, dp1, h1)
                check = 1
            if sa1 == 1 and random.random() < 0.25 and check == 0:
                print("Character 1 activates Damage Reduction")
                h1 = damage_reduction(ap2, dp1, h1)
                check = 1
            # Ultimate Attack
            if sa2 == 4 and random.random() < 0.01 and check == 0:
                print("Character 2 activates Ultimate Attack")
                h1 = ultimate_attack(h1)
                check = 1

        if check == 0 and check_both == 0:
            print("No ability activated")
            h1 = turns(ap2, dp1, h1)
        else:
            check = 0
            check_both = 0

        print(f"Character 1 has {h1} health")
        print()
        n += 1

    if r == 1:
        while h1 > 0 and h2 > 0:
            print(f"Round {n}:")
            print()
            sa1 = special_ability(1)
            sa2 = special_ability(2)
            print()
            print(f"Character 2 attacks")

            if sa2 == 2 and sa1 == 1 and random.random() < 0.0625:
                print("Character 2 activates Power Strike")
                print("Character 1 activates Damage Reduction")
                h1 = power_reduction(ap2, dp1, h1)
                check_both = 1
            if sa2 == 2 and sa1 == 3 and random.random() < 0.0625 and h1 < 30:
                print("Character 2 activates Power Strike")
                print("Character 1 activates Second Wind")
                h1 = power_wind(ap2, dp1, h1)
                check_both = 1

            if check_both == 0:
                if sa2 == 2 and random.random() < 0.25:
                    print("Character 2 activates Power Strike")
                    h1 = power_strike(ap2, dp1, h1)
                    check = 1
                if sa1 == 1 and random.random() < 0.25 and check == 0:
                    print("Character 1 activates Damage Reduction")
                    h1 = damage_reduction(ap2, dp1, h1)
                    check = 1
                if sa1 == 3 and random.random() < 0.25 and h1 < 30 and check == 0:
                    print("Character 1 activates Second Wind")
                    h1 = second_wind(ap2, dp1, h1)
                    check = 1
                # Ultimate Attack
                if sa2 == 4 and random.random() < 0.01 and check == 0:
                    print("Character 2 activates Ultimate Attack")
                    h1 = ultimate_attack(h1)
                    check = 1

            if check == 0 and check_both == 0:
                print("No ability activated")
                h1 = turns(ap2, dp1, h1)
            else:
                check = 0
                check_both = 0

            print(f"Character 1 has {h1} health")
            print()
            n += 1

            if h1 <= 0 or h2 <= 0:
                break

            print(f"Round {n}:")
            print()
            sa1 = special_ability(1)
            sa2 = special_ability(2)
            print()
            print(f"Character 1 attacks")

            if sa1 == 2 and sa2 == 1 and random.random() < 0.0625:
                print("Character 1 activates Power Strike")
                print("Character 2 activates Damage Reduction")
                h2 = power_reduction(ap1, dp2, h2)
                check_both = 1
            if sa1 == 2 and sa2 == 3 and random.random() < 0.0625 and h2 < 30:
                print("Character 1 activates Power Strike")
                print("Character 2 activates Second Wind")
                h2 = power_wind(ap1, dp2, h2)
                check_both = 1

            if check_both == 0:
                if sa1 == 2 and random.random() < 0.25:
                    print("Character 1 activates Power Strike")
                    h2 = power_strike(ap1, dp2, h2)
                    check = 1
                if sa2 == 1 and random.random() < 0.25 and check == 0:
                    print("Character 2 activates Damage Reduction")
                    h2 = damage_reduction(ap1, dp2, h2)
                    check = 1
                if sa2 == 3 and random.random() < 0.25 and h2 < 30 and check == 0:
                    print("Character 2 activates Second Wind")
                    h2 = second_wind(ap1, dp2, h2)
                    check = 1
                # Ultimate Attack
                if sa1 == 4 and random.random() < 0.01 and check == 0:
                    print("Character 1 activates Ultimate Attack")
                    h2 = ultimate_attack(h2)
                    check = 1

            if check == 0 and check_both == 0:
                print("No ability activated")
                h2 = turns(ap1, dp2, h2)
            else:
                check = 0
                check_both = 0

            print(f"Character 2 has {h2} health")
            print()
            n += 1
    else:
        while h1 > 0 and h2 > 0:
            print(f"Round {n}:")
            print()
            sa1 = special_ability(1)
            sa2 = special_ability(2)
            print()
            print(f"Character 1 attacks")

            if sa1 == 2 and sa2 == 1 and random.random() < 0.0625:
                print("Character 1 activates Power Strike")
                print("Character 2 activates Damage Reduction")
                h2 = power_reduction(ap1, dp2, h2)
                check_both = 1
            if sa1 == 2 and sa2 == 3 and random.random() < 0.0625 and h2 < 30:
                print("Character 1 activates Power Strike")
                print("Character 2 activates Second Wind")
                h2 = power_wind(ap1, dp2, h2)
                check_both = 1

            if check_both == 0:
                if sa1 == 2 and random.random() < 0.25:
                    print("Character 1 activates Power Strike")
                    h2 = power_strike(ap1, dp2, h2)
                    check = 1
                if sa2 == 1 and random.random() < 0.25 and check == 0:
                    print("Character 2 activates Damage Reduction")
                    h2 = damage_reduction(ap1, dp2, h2)
                    check = 1
                if sa2 == 3 and random.random() < 0.25 and h2 < 30 and check == 0:
                    print("Character 2 activates Second Wind")
                    h2 = second_wind(ap1, dp2, h2)
                    check = 1
                # Ultimate Attack
                if sa1 == 4 and random.random() < 0.01 and check == 0:
                    print("Character 1 activates Ultimate Attack")
                    h2 = ultimate_attack(h2)
                    check = 1

            if check == 0 and check_both == 0:
                print("No ability activated")
                h2 = turns(ap1, dp2, h2)
            else:
                check = 0
                check_both = 0

            print(f"Character 2 has {h2} health")
            print()
            n += 1

            if h1 <= 0 or h2 <= 0:
                break

            print(f"Round {n}:")
            print()
            sa1 = special_ability(1)
            sa2 = special_ability(2)
            print()
            print(f"Character 2 attacks")

            if sa2 == 2 and sa1 == 1 and random.random() < 0.0625:
                print("Character 2 activates Power Strike")
                print("Character 1 activates Damage Reduction")
                h1 = power_reduction(ap2, dp1, h1)
                check_both = 1
            if sa2 == 2 and sa1 == 3 and random.random() < 0.0625 and h1 < 30:
                print("Character 2 activates Power Strike")
                print("Character 1 activates Second Wind")
                h1 = power_wind(ap2, dp1, h1)
                check_both = 1

            if check_both == 0:
                if sa2 == 2 and random.random() < 0.25:
                    print("Character 2 activates Power Strike")
                    h1 = power_strike(ap2, dp1, h1)
                    check = 1
                if sa1 == 1 and random.random() < 0.25 and check == 0:
                    print("Character 1 activates Damage Reduction")
                    h1 = damage_reduction(ap2, dp1, h1)
                    check = 1
                if sa1 == 3 and random.random() < 0.25 and h1 < 30 and check == 0:
                    print("Character 1 activates Second Wind")
                    h1 = second_wind(ap2, dp1, h1)
                    check = 1
                # Ultimate Attack
                if sa2 == 4 and random.random() < 0.01 and check == 0:
                    print("Character 2 activates Ultimate Attack")
                    h1 = ultimate_attack(h1)
                    check = 1

            if check == 0 and check_both == 0:
                print("No ability activated")
                h1 = turns(ap2, dp1, h1)
            else:
                check = 0
                check_both = 0

            print(f"Character 1 has {h1} health")
            print()
            n += 1

    print()
    if h1 <= 0:
        print("Character 2 won")
        return 'Character 2'
    if h2 <= 0:
        print("Character 1 won")
        return 'Character 1'
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--per-round', action='store_true', help='Per-round game')
    args = parser.parse_args()

    if args.per_round:
        if int(input("Do you want to see just one game (1) or see the winning rate of the two characters in 1000 games (2) ? ")) == 1:
            setup_per_round()
        else:
            win_rate = Counter(setup_per_round() for _ in range(1000))
            print()
            print(f"First character's win rate: {win_rate['Character 1'] / 1000}")
            print(f"Second character's win rate: {win_rate['Character 2'] / 1000}")
            print(f"Tie rate: {win_rate['Tie'] / 1000}")
    else:
        if int(input("Do you want to see just one game (1) or see the winning rate of the two characters in 1000 games (2) ? ")) == 1:
            setup_fixed()
        else:
            win_rate = Counter(setup_fixed() for _ in range(1000))
            print()
            print(f"First character's win rate: {win_rate['Character 1'] / 1000}")
            print(f"Second character's win rate: {win_rate['Character 2'] / 1000}")
            print(f"Tie rate: {win_rate['Tie'] / 1000}")

if __name__ == '__main__':
    main()
