answer = input("What is the answer to the great question in life? ")

normalised_answer = answer.lower().strip()

match normalised_answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
