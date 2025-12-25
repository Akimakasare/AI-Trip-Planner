def generate_itinerary(destination, days, places):
    itinerary = {}
    index = 0

    for day in range(1, days + 1):
        itinerary[f"Day {day}"] = places[index:index + 2]
        index += 2

    return itinerary
