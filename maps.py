def get_google_maps_link(destination):
    base_url = "https://www.google.com/maps/search/"
    return f"{base_url}{destination.replace(' ', '+')}"
