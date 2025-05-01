
def aqi_categories(aqi):
    if aqi < 51:
        return 'Good'
    elif aqi >= 51 and aqi < 101:
        return "Moderate"
    elif aqi >= 101 and aqi < 151:
        return "Unhealthy for Sensitive Groups"
    elif aqi >= 151 and aqi < 201:
        return "Unhealthy"
    elif aqi >= 201 and aqi < 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"


    # 0 - 50 	    Good
    # 51 -100 	Moderate
    # 101-150     Unhealthy for Sensitive Groups
    # 151-200 	Unhealthy
    # 201-300 	Very Unhealthy
    # 300+ 	    Hazardous