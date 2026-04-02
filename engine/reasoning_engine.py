from utils.constants import ROOT_CAUSE_RULES, DEFAULTS

def generate_root_causes(area_data):

    for area in area_data:
        for issue in area_data[area]:

            issue["root_cause"] = ROOT_CAUSE_RULES.get(
                issue["issue"],
                DEFAULTS["missing"]
            )

    return area_data