import random as rand
head = 0
tail = 1

def choose():
    return rand.choice([head,tail])


def run_strategy(s):
    match s:
        case "random":
            return choose()
        case "tail":
            return tail
        case "head":
            return head
        case _:
            return -1


def run_experiment(s,q):
    coin = choose()
    if coin == head:
        if coin == run_strategy(s):
            return (1, 1)
        return (0, 1)

    questioned = 0
    answered = 0
    for _ in range(q):
        if coin == run_strategy(s):
            answered += 1
        questioned += 1
    return (answered, q)


def find_prob(r, q):
    print("Analysing " + str(r) + " Experiments...")
    print("On Head woken up once, on tail woken up " + str(q) + " times.")
    print()

    for strat in ["tail", "head", "random"]:
        p = 0.0
        s = 0
        t = 0
        print("Strategy: " + strat)
        
        for _ in range(r):
            (ans,que) = run_experiment(strat, q)
            s += ans
            t += que
            if ans == que:
                p += 1/r
        print("Rate of 'All Answered Correctly': " + str(round(p, 3)))
        print("Rate of correct answers: " + str(round(s/t, 3)) + " (" + str(s) + " out of " + str(t) + ")")
        print()

def main():
    find_prob(100_000, 100)

main()
