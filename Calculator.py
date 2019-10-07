prompt = ""
answer = 0
while prompt.lower() != "q":
    prompt = input("Enter Value: ")
    if prompt.lower() == 'q':
        break
    prompt = prompt.strip()
    operator = prompt[0]
    value = int(prompt[1:])

    if "+" in prompt:
        answer = answer + value
    elif "-" in prompt:
        answer = answer - value
    elif "*" in prompt:
        answer = answer * value
    print(answer)