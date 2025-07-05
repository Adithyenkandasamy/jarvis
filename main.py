from llm.llm_manager import get_llm_reply

if __name__ == "__main__":
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            break
        reply = get_llm_reply(prompt)
        print("Jarvis:", reply)