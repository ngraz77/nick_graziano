def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

text_messages = ["Hey, how are you?", "Want to hang out today?", "Good morning.", "How's your day so far?"]

sent_messages = []

send_messages(text_messages, sent_messages)

print("\nMessages left to send:")
print(text_messages)

print("\nMessages that were sent:")
print(sent_messages)
