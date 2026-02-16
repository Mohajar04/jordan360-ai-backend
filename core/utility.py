from config.settings import W_INTEREST,W_TIME,W_DISTANCE,W_CROWD

def compute_utility(sim,total_time,available_time,distance,crowd):
    time_eff=1-(total_time/available_time)
    dist_eff=1/(1+distance)
    score=(W_INTEREST*sim+
           W_TIME*time_eff+
           W_DISTANCE*dist_eff-
           W_CROWD*crowd)
    return score,time_eff,dist_eff
