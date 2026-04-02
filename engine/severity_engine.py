from utils.constants import SEVERITY_RULES

def assign_severity(area_data):

    for area in area_data:
        for issue in area_data[area]:

            rule = SEVERITY_RULES.get(issue["issue"], None)

            if rule:
                issue["severity"] = rule["level"]
                issue["severity_reason"] = rule["reason"]
            else:
                issue["severity"] = "Not Available"
                issue["severity_reason"] = "Not Available"

    return area_data