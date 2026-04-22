class Agent:
    def __init__(self, name):
        self.name = name

    def send(self, message, receiver):
        print(f"{self.name}: {message}")
        receiver.receive(message, self)

    def receive(self, message, sender):
        print(f"{self.name} received: {message}")
        reply = self.generate_reply(message)

        # STOP if no reply
        if reply:
            print(f"{self.name}: {reply}")
        # Do NOT send back again (this stops infinite loop)

    def generate_reply(self, message):
        message = message.lower()

        if "hello" in message:
            return "Hi!"
        elif "how are you" in message:
            return "I am fine!"
        elif "bye" in message:
            return None   # STOP here
        else:
            return "Okay!"


# Create agents
agent1 = Agent("Agent A")
agent2 = Agent("Agent B")

# Controlled conversation (no infinite loop)
agent1.send("Hello", agent2)
agent1.send("How are you?", agent2)
agent1.send("Bye", agent2)