def main():
    time_of_day = input("What is the current time? (HH:MM): ").strip()

    breakfast_start = 7.0
    breakfast_end = 8.0

    lunch_start = 12.0
    lunch_end = 13.0

    dinner_start = 18.0
    dinner_end = 19.0

    try:
        current_time = convert(time_of_day)

        if breakfast_start <= current_time <= breakfast_end:
            print("Breakfast Time")

        elif lunch_start <= current_time <= lunch_end:
            print("Lunch Time")

        elif dinner_start <= current_time <= dinner_end:
            print("Dinner Time")


    except ValueError:
        print("Please enter the time in the format HH:MM (e.g., 07:30 or 18:15).")


def convert(time):
    # Split "7:30" into hours ("7") and minutes ("30")
    hours, minutes = time.split(":")

    # Convert minutes to a fraction of an hour (e.g., 30 / 60 = 0.5)
    decimal_minutes = float(minutes) / 60.0

    # Return the sum as a float (e.g., 7 + 0.5 = 7.5)
    return float(hours) + decimal_minutes


if __name__ == "__main__":
    main()
