import streamlit as st
from utils.flights import get_cheapest_flight
from utils.hotels import get_best_hotel
from utils.places import get_top_places
from utils.itinerary import generate_itinerary
from utils.budget import calculate_budget
from utils.maps import get_google_maps_link
from utils.pdf_generator import generate_pdf

st.set_page_config(page_title="AI Trip Planner", layout="wide")
st.title("✈️ AI Trip Planner")

cities = [
    "Delhi", "Mumbai", "Goa", "Bangalore",
    "Chennai", "Hyderabad", "Kolkata", "Jaipur"
]
source = st.selectbox("From", cities)
destination = st.selectbox("To", cities)
days = st.slider("Trip Duration (Days)", 1, 7, 3)

if st.button("Plan My Trip"):
    flight = get_cheapest_flight(source, destination)
    hotel = get_best_hotel(destination)
    places = get_top_places(destination)
    if not flight or not hotel:
        st.error("❌ Unable to fetch flight or hotel data")
        st.stop()
    itinerary = generate_itinerary(destination, days, places)
    budget = calculate_budget(flight, hotel, days)
    map_link = get_google_maps_link(destination)
    st.subheader("✈️ Flight")
    st.json(flight)
    st.subheader("🏨 Hotel")
    st.json(hotel)
    st.subheader("📍 Places to Visit")
    st.write(places)    
    st.subheader("🗓️ AI Itinerary")
    st.write(itinerary)
    st.subheader("💰 Budget")
    st.json(budget)
    st.subheader("🗺️ Google Maps")
    st.markdown(f"[Open Map]({map_link})")
    pdf_file = generate_pdf(
        source, destination, days,
        flight, hotel, itinerary, budget
    )
    with open(pdf_file, "rb") as f:
        st.download_button(
            "📄 Download Trip PDF",
            f,
            file_name="Trip_Plan.pdf"
        )
