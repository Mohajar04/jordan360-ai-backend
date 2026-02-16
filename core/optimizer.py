from context.distance import calculate_distance
from context.time import estimate_travel_time
from core.similarity import cosine_similarity
from core.utility import compute_utility

def build_route(user_vector,user_lat,user_lon,available_time,locations,crowd_input):
    route=[]
    explanations=[]
    remaining_time=available_time
    current_lat=user_lat
    current_lon=user_lon
    remaining=locations.copy()

    while remaining and remaining_time>0:
        scored=[]
        for loc in remaining:
            distance=calculate_distance(current_lat,current_lon,
                                        loc["latitude"],loc["longitude"])
            travel_time=estimate_travel_time(distance)
            total_time=travel_time+loc["avg_visit_time"]

            if total_time<=remaining_time:
                sim=cosine_similarity(user_vector,loc["feature_vector"])
                crowd=crowd_input.get(loc["name"],0)
                score,time_eff,dist_eff=compute_utility(
                    sim,total_time,available_time,distance,crowd)

                scored.append((loc,score,total_time,sim,time_eff,dist_eff,crowd))

        if not scored:
            break

        best=sorted(scored,key=lambda x:x[1],reverse=True)[0]
        loc,score,time_used,sim,time_eff,dist_eff,crowd=best

        route.append(loc["name"])
        explanations.append({
            "location":loc["name"],
            "similarity":sim,
            "time_efficiency":time_eff,
            "distance_efficiency":dist_eff,
            "crowd_penalty":crowd,
            "final_score":score
        })

        remaining_time-=time_used
        current_lat=loc["latitude"]
        current_lon=loc["longitude"]
        remaining.remove(loc)

    return route,explanations
