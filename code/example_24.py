import pickle

with open('outputs/series.pkl', 'rb') as f:
    records = pickle.load(f)

features = records["features"]

def show_severe(feature):
    alert_id = feature.get("id")
    properties = feature.get("properties")
    if properties:
        severity = properties.get("severity")
        if severity == "Severe":
            effective = properties.get("effective")
            messageType = properties.get("messageType")
            headline = properties.get("headline")
            description = properties.get("description")
            yield(
                f"     Alert ID: {alert_id}" + "\n" +
                f"    Effective: {effective}" + "\n" +
                f" Message Type: {messageType}" + "\n" +
                f"     Severity: {severity}" + "\n" +
                f"     Headline: {headline}" + "\n" +
                f"  Description: {description}" + "\n")

    
for feature in features:
    for severe in show_severe(feature):
        print(severe)
        print("-"*80)