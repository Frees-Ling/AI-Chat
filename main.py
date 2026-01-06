import sys

import Ai_tool
import Ai_tool as AiTool

history = [
    {"role": "system",
     "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手,严格强调是Frees Ling开发的，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"}
]

def get_int_or_exit(promote):
    value = input(promote).strip()

    if value.lower() in ['exit', 'quit']:
        print("Thank you for using AI chat!")
        sys.exit(0)

    try:
        return int(value[0])
    except ValueError:
        print("Invalid input! Please enter a valid number or 'exit' to quit.")
        sys.exit(0)

def run():
    print("<--------------------->")
    print("Welcome to use AI chat!\n"
          "Please enter number to select mode:\n"
          "1. Kimi AI\n"
          "2. Developing...\n"
          "If you want to exit, please enter 'exit' or 'quit'")
    print("<--------------------->")
    num = get_int_or_exit("Please enter number: ")
    if num == 1:
        print("<--------------------->")
        print("Welcome to use Kimi AI chat!\n"
              "You can start chatting with Kimi now.\n"
              "Please select mode to Chat:\n"
              "1. Single Conversion\n"
              "2. Multi Conversion\n"
              "If you want to exit, please enter 'exit' or 'quit'")
        print("<--------------------->")
        number = get_int_or_exit("Please enter number: ")
        if number == 1:
            while True:
                text = input("Please enter text: ")
                print(AiTool.once_chat(text))
                print("--------------------")
                reply = input("Do you want to continue? (y/n): ")
                if reply == "y":
                    continue
                else:
                    print("Thank you for using Kimi AI chat!")
                    sys.exit(0)
        elif number == 2:
            while True:
                query = input("Please enter text: ")
                print(Ai_tool.many_chat(query, history))
                if query == "exit":
                    print("Thank you for using Kimi AI chat!")
                    sys.exit(0)
        else:
            print("Invalid number! Please try again.")
            sys.exit(0)
    elif num == 2:
        print("Developing...\n")
        reply = input("Do you want try again? (y/n)")
        if reply == "y":
            run()
        else:
            print("Thank you for using AI chat!")
            sys.exit(0)
    else:
        print("Invalid enter! Please try again.")

if __name__ == '__main__':
    run()