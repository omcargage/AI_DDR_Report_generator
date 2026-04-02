ISSUE_KEYWORDS = {
    "Dampness": ["dampness", "seepage", "moisture"],
    "Cracks": ["crack", "cracks", "hairline crack"],
    "Leakage": ["leakage", "water ingress"],
    "Tile Hollowness": ["tile hollowness", "hollow tile"],
}
AREA_KEYWORDS = {
    "Bathroom": ["bathroom", "toilet"],
    "Balcony": ["balcony"],
    "Terrace": ["terrace", "roof"],
    "External Wall": ["external wall", "wall"],
    "Bedroom": ["bedroom"],
    "Hall": ["hall"],
}
SEVERITY_RULES = {
    "Cracks": {
        "level": "High",
        "reason": "Structural damage risk"
    },
    "Leakage": {
        "level": "High",
        "reason": "Active water intrusion"
    },
    "Dampness": {
        "level": "Moderate",
        "reason": "Moisture accumulation over time"
    },
    "Tile Hollowness": {
        "level": "Low",
        "reason": "Surface-level issue"
    }
}

ROOT_CAUSE_RULES = {
    "Dampness": "Moisture ingress due to poor waterproofing or tile gaps",
    "Cracks": "Structural stress or environmental exposure",
    "Leakage": "Water seepage from plumbing or surface failure",
    "Tile Hollowness": "Improper tile fixing or bonding failure"
}

DEFAULTS = {
    "missing": "Not Available",
    "no_image": "Image Not Available",
    "no_conflict": "No conflicts found"
}
RECOMMENDATIONS = {
    "Dampness": "Apply waterproofing treatment",
    "Cracks": "Perform structural repair and sealing",
    "Leakage": "Fix plumbing and seal leakage points",
    "Tile Hollowness": "Regrouting or tile replacement"
}
