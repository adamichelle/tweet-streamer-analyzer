from textblob import TextBlob
import re

def clean_tweet(tweet):
    return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', tweet).split())

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity ==0:
        return 'Neutral'
    else:
        return 'Negative'

def extract_locations(location):
    # To modify locations
    possible_locations = [
        'Nigeria', 'Lagos', 'Osun', 'Ogun', 'Oyo', 'Kano', 'Abia', 'Uyo', 'Abuja', 'Port Harcourt', 'Portharcourt', 'PH', 'Enugu', 
        'Owerri', 'Cross River', 'Anambra', 'Warri', 'Ikeja', 'Unilag', 'University of Lagos', 'V.G.C', 'Naija', 'Ikorodu', 'Makurdi', 
        'Benin City', 'Benin', 'Osogbo', 'Ondo', 'Kalabari Ethnic Nationality', 'NG', 'Delta', 'Onitsha', 'Zaria', 'Kaduna', 'lasgidi',
        'South Africa', 'Pretoria', 'Cape Town', 'Jhb', 'Johannesburg', 'SA', 'S.A', 'Ghana', 'Accra', 'GH', 'United Kingdom', 'England', 
        'USA', 'U.S.A', 'United States', 'NYC', 'NY','Northern Virginia', 'CO', 'Las Vegas', 'Colorado','NM', 'CA', 'Canada', 'Toronto', 
        'Ontario', 'Italy', 'Finland', 'India', 'Swaziland', 'Cameroon', 'Namibia', 'Liberia', 'Mauritius', 'Malawi', 'Tanzania', 'Zambia', 
        'Uganda', 'Kenya', 'Sierra Leone', 'Zimbabwe', 'Africa'
    ]
    
    nigeria = possible_locations[:35]
    south_africa = possible_locations[35:42]
    ghana = possible_locations[42:45]
    uk = possible_locations[45:47]
    usa = possible_locations[47:58]
    canada = possible_locations[58:61]
    europe = possible_locations[61:63]
    other_parts_of_africa = possible_locations[-13:]
    india = possible_locations[63]

    if any(location_substring in location for location_substring in possible_locations) == False or location == '':
        return 'N/A'

    if any(ng_location_substring in location for ng_location_substring in nigeria):
        return 'Nigeria'

    if any(sa_location_substring in location for sa_location_substring in south_africa):
        return 'South Africa'

    if any(gh_location_substring in location for gh_location_substring in ghana):
        return 'Ghana'

    if any(uk_location_substring in location for uk_location_substring in uk):
        return 'UK'

    if any(usa_location_substring in location for usa_location_substring in usa):
        return 'USA'

    if any(ca_location_substring in location for ca_location_substring in canada):
        return 'Canada'
    
    if any(eu_location_substring in location for eu_location_substring in europe):
        return 'Europe'

    if any(opa_location_substring in location for opa_location_substring in other_parts_of_africa):
        return 'Other Parts of Africa'

    if location in india:
        return 'India'