def is_palindrome(value):
    if not isinstance(value, str):
        raise ValueError("Input must be a string")

    cleaned = "".join(char.lower() for char in value if char.isalnum())

    if cleaned == "":
        return False

    return cleaned == cleaned[::-1]