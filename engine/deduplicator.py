def remove_duplicates(area_data):
    for area in area_data:
        seen = set()
        unique = []

        for issue in area_data[area]:
            key = issue["issue"]

            if key not in seen:
                seen.add(key)
                unique.append(issue)

        area_data[area] = unique

    return area_data