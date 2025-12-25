from fpdf import FPDF

def generate_pdf(source, destination, days, flight, hotel, itinerary, budget):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "AI Trip Planner Summary", ln=True)
    pdf.cell(200, 10, f"From: {source}", ln=True)
    pdf.cell(200, 10, f"To: {destination}", ln=True)
    pdf.cell(200, 10, f"Days: {days}", ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, "Flight Details:", ln=True)
    pdf.multi_cell(0, 8, str(flight))

    pdf.ln(5)
    pdf.cell(200, 10, "Hotel Details:", ln=True)
    pdf.multi_cell(0, 8, str(hotel))

    pdf.ln(5)
    pdf.cell(200, 10, "Itinerary:", ln=True)
    for day, plan in itinerary.items():
        pdf.multi_cell(0, 8, f"{day}: {', '.join(plan)}")

    pdf.ln(5)
    pdf.cell(200, 10, "Budget:", ln=True)
    pdf.multi_cell(0, 8, str(budget))

    file_name = "trip_plan.pdf"
    pdf.output(file_name)
    return file_name
