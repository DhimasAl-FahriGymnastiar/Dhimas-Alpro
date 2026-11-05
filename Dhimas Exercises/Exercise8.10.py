def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ["Hello!", "How are you?", "Good luck!"]
sent_messages = []

send_messages(messages, sent_messages)

print("\nOriginal messages:", messages)
print("Sent messages:", sent_messages)