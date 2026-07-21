# ============================================
# Project 1: Rule-Based AI Chatbot
# DecodeLabs - AI Industrial Training Kit (Batch 2026)
# ============================================

# Phase 1: Knowledge Base (Dictionary) - 5+ Intents
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to see you.",
    "how are you": "I'm just a bunch of code, but I'm doing great! You?",
    "what is your name": "I'm DecodeBot, your friendly rule-based assistant.",
    "what can you do": "I can chat with you using predefined rules and logic!",
    "help": "Sure! You can say hello, ask my name, or ask how I am.",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
}

# Exit commands (Kill Command)
exit_commands = ["exit", "bye", "quit", "goodbye"]


def get_response(user_input):
    """
    Returns chatbot's reply based on cleaned input.
    Uses .get() for an atomic lookup + fallback operation,
    avoiding the if-elif ladder anti-pattern.
    """
    # Nested condition example: partial keyword matching
    if "name" in user_input:
        return "I'm DecodeBot!"

    return responses.get(user_input, "I do not understand. Can you rephrase that?")


def chatbot():
    print("🤖 DecodeBot: Hello! Type 'exit' anytime to end our chat.\n")

    # Phase 2: The Heartbeat - Infinite Loop
    while True:
        raw_input_text = input("You: ")

        # Phase 1: Sanitization & Normalization
        clean_input = raw_input_text.lower().strip()

        # Exit Strategy
        if clean_input in exit_commands:
            print("🤖 DecodeBot: Goodbye! Have a great day. 👋")
            break

        # Process input through the Logic Skeleton
        reply = get_response(clean_input)
        print(f"🤖 DecodeBot: {reply}")


if __name__ == "__main__":
    chatbot()
