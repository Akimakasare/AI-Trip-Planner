def calculate_budget(flight, hotel, days):
    flight_cost = flight.get("price", 0)
    hotel_cost = hotel.get("price_per_night", 0) * days

    return {
        "flight_cost": flight_cost,
        "hotel_cost": hotel_cost,
        "total_cost": flight_cost + hotel_cost
    }
