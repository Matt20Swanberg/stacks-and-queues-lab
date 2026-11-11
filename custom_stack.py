def is_valid_parentheses(s: str) -> bool:
    """
    Validate whether a string contains properly balanced brackets

    Supported brackets:
        - Parentheses: ()
        - Curly braces: {}
        - Square brackets: []

    Uses a stack (Last In, First Out) to track opening brackets
    Each closing bracket must match the most recently encountered
    opening bracket.

    Args:
        s (str): The string containing brackets to validate

    Returns:
        bool: True if all brackets are correctly matched and nested
              False if the string is empty, contains invalid characters,
              or has unmatched or incorrectly ordered brackets
    """

    # Define supported opening brackets
    open_characters = ["(", "{", "["]

    # Map each closing bracket to its matching opening bracket
    bracket_pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    # Reject empty strings before processing any characters
    # ** This was optional and not required by test,
    # but personally wanted to account for
    if not s:
        print("Invalid input: The string is empty")
        return False

    # Initialize an empty stack to track opening brackets
    stack = []
    
    # Examine each character in the input string
    for char in s:

        # Push opening brackets onto the stack
        if char in open_characters:
            stack.append(char) 

        elif char in bracket_pairs:

            # A closing bracket cannot match an empty stack
            if not stack:
                return False

            # Remove the most recent opening bracket and verify
            # that it matches the current closing bracket
            if stack.pop() != bracket_pairs[char]:
                return False

        # Reject characters that are not supported brackets
        else:
            return False

    # A valid string must have no unmatched opening brackets
    return not stack