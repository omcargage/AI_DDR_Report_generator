from utils.constants import AREA_KEYWORDS

def map_areas(issues):
    area_map = {}

    for issue in issues:
        assigned = False

        for area, keywords in AREA_KEYWORDS.items():
            for word in keywords:
                if word in issue["issue"].lower():
                    area_map.setdefault(area, []).append(issue)
                    assigned = True
                    break

        if not assigned:
            area_map.setdefault("General", []).append(issue)

    return area_map