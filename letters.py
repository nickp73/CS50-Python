def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi", "Toad"]
    for name in names:
        print(write_letter(name,"Princess Peach"))


def write_letter(recipient, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {recipient},
        
        You are cordially invited to a ball at
        Peach's Castle this Saturday at 7pm.

        Yours Sincerely,
        {sender}

    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """


if __name__ == "__main__":
    main()