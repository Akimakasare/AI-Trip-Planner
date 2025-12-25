#✈️ AI Trip Planner

AI Trip Planner is a Python-based web application built using Streamlit that helps users plan their trips efficiently. By selecting a source city, destination city, and trip duration, the application generates a complete travel plan including flight details, hotel recommendations, places to visit, a day-wise itinerary, budget estimation, Google Maps integration, and a downloadable PDF summary.

🚀 Features

Select source and destination cities

Choose trip duration

Flight and hotel recommendations

AI-generated itinerary

Budget calculation

Google Maps link for destination

Downloadable trip summary in PDF format

Clean, modular, and error-safe code structure

🧱 Project Structure
AI_Trip_Planner/
├── app.py
├── requirements.txt
└── utils/
    ├── flights.py
    ├── hotels.py
    ├── places.py
    ├── itinerary.py
    ├── budget.py
    ├── maps.py
    └── pdf_generator.py

🛠️ Technologies Used

Python

Streamlit

FPDF

Requests (API-ready)

AI-ready architecture

▶️ How to Run

Install dependencies:

pip install -r requirements.txt


Start the application:

streamlit run app.py


Open the browser at:

http://localhost:8501

🌱 Future Enhancements

Real flight and hotel API integration

GPT-powered itinerary generation

User login and saved trips

Weather and currency support

Cloud deployment
