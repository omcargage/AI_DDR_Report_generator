import re

def analyze_thermal(text):
    hotspots = re.findall(r"Hotspot\s*:\s*(\d+\.?\d*)", text)
    coldspots = re.findall(r"Coldspot\s*:\s*(\d+\.?\d*)", text)

    insights = []

    for h, c in zip(hotspots, coldspots):
        delta = float(h) - float(c)

        if delta > 5:
            insights.append(
                f"High thermal variation ({delta:.1f}°C) → possible moisture presence"
            )
        else:
            insights.append(
                f"Normal thermal variation ({delta:.1f}°C)"
            )

    return insights