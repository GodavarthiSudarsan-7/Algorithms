

def reflex_agent(location, status):
    
    if status == "Dirty":
        return "CLEAN"
    
    if location == "A":
        return "MOVE RIGHT"
    
    if location == "B":
        return "MOVE LEFT"



environment = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"


for step in range(5):
    print("\nStep:", step+1)
    print("Location:", location)
    print("Status:", environment[location])

    action = reflex_agent(location, environment[location])
    print("Action:", action)

    if action == "CLEAN":
        environment[location] = "Clean"
    elif action == "MOVE RIGHT":
        location = "B"
    elif action == "MOVE LEFT":
        location = "A"