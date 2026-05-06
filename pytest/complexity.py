def check_number(n):
    if n > 0:
        if n % 2 == 0:
            return "Positive Even"
        else:
            return "Positive Odd"
    elif n == 0:
        return "Zero"
    else:
        return "Negative"
