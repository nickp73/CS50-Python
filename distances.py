distances = {
    "Voyager 1": 14.4,
    "Voyager 2": 13.2,
    "Pioneer 10": 12.2,
    "Pioneer 11": 11.2,
    "New Horizons": 4.8
}

def main():
    for distance in distances.values():
        print(f"{distance} AU = {convert(distance)} m")

def convert(au):
    return au * 149597870700



if __name__ == "__main__":
    main()