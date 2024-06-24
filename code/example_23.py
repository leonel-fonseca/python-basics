import pickle

with open('outputs/series.pkl', 'rb') as f:
    records = pickle.load(f)

features = records["features"]

for feature in features:
    alert_id = feature.get("id")
    properties = feature.get("properties")
    if properties:
        effective = properties.get("effective")
        messageType = properties.get("messageType")
        severity = properties.get("severity")
        headline = properties.get("headline")
        description = properties.get("description")
        print(
            f"     Alert ID: {alert_id}" + "\n" +
            f"    Effective: {effective}" + "\n" +
            f" Message Type: {messageType}" + "\n" +
            f"     Severity: {severity}" + "\n" +
            f"     Headline: {headline}" + "\n" +
            f"  Description: {description}" + "\n")
        print("-"*80)