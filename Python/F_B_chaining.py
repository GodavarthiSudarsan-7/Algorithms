
rules = [
    (["fever", "cough"], "flu"),
    (["flu", "fatigue"], "viral infection"),
    (["headache", "nausea"], "migraine")
]

facts = {"fever", "cough", "fatigue"}


# ---------------- FORWARD CHAINING ----------------
def forward_chaining(facts, rules):
    inferred = set(facts)

    while True:
        new_inferred = inferred.copy()

        for conditions, result in rules:
            if all(cond in inferred for cond in conditions):
                if result not in inferred:
                    print(f"Inferred: {result}")
                    new_inferred.add(result)

        if new_inferred == inferred:
            break

        inferred = new_inferred

    return inferred


# ---------------- BACKWARD CHAINING ----------------
def backward_chaining(goal, facts, rules):
    print(f"Checking goal: {goal}")

    if goal in facts:
        return True

    for conditions, result in rules:
        if result == goal:
            return all(backward_chaining(cond, facts, rules) for cond in conditions)

    return False



print("Forward Chaining:")
final_facts = forward_chaining(facts, rules)
print("Final Facts:", final_facts)


print("\nBackward Chaining:")
goal = "viral infection"
if backward_chaining(goal, facts, rules):
    print(f"{goal} is TRUE")
else:
    print(f"{goal} is FALSE")