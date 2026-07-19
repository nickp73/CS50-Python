def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": "2.4", "orbit": "Earth"})
    print(creat_report(spacecraft))


def creat_report(spacecraft):
    return f"""
    ========= REPORT =========
    
    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}
    ==========================
    """


if __name__ == "__main__":
    main()