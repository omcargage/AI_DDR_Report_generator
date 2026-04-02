from utils.constants import ISSUE_KEYWORDS, RECOMMENDATIONS, AREA_KEYWORDS, DEFAULTS


def extract_issues(text):
    text_lower = text.lower()
    lines = text_lower.split("\n")

    issues = []
    seen = set()  # for deduplication

    for line in lines:

        # 🔹 Detect area from line
        detected_area = "General"

        for area, keywords in AREA_KEYWORDS.items():
            for word in keywords:
                if word in line:
                    detected_area = area
                    break

        # 🔹 Detect issue from line
        for issue, keywords in ISSUE_KEYWORDS.items():
            for word in keywords:
                if word in line:

                    # unique key to avoid duplicates
                    key = (detected_area, issue)

                    if key not in seen:
                        seen.add(key)

                        issues.append({
                            "issue": issue,
                            "area": detected_area,
                            "location": line.strip(),  # raw context
                            "recommendation": RECOMMENDATIONS.get(issue, DEFAULTS["missing"]),
                            "source": "inspection"  # useful later
                        })

                    break

    return issues