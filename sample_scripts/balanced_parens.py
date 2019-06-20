from IPython import embed

def check_parens(parens):
    stack = []
    for paren in parens :
        if paren == "(":
          stack.append(paren)
        elif paren == ")" and len(stack) == 0:
            return False
        elif paren == ")" and stack[-1] == "(":
            stack.pop()

    if len(stack) > 0:
       return False

    return True
