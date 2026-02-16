from config.settings import AVG_SPEED_KMH

def estimate_travel_time(distance_km):
    return (distance_km/AVG_SPEED_KMH)*60
