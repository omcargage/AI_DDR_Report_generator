from parser.pdf_parser import extract_text_from_pdf
from parser.image_extractor import extract_images

from engine.rule_engine import extract_issues
from engine.area_mapper import map_areas
from engine.deduplicator import remove_duplicates
from engine.reasoning_engine import generate_root_causes
from engine.severity_engine import assign_severity
from engine.conflict_checker import detect_conflicts
from engine.report_builder import generate_report


def run_pipeline(inspection_pdf, thermal_pdf):

    # 🔹 Extract text
    inspection_text = extract_text_from_pdf(inspection_pdf)
    thermal_text = extract_text_from_pdf(thermal_pdf)

    # 🔹 Extract images
    images = extract_images(inspection_pdf)


    issues = extract_issues(inspection_text)

    for issue in issues:
        issue["image"] = None

    # 🔹 Pipeline
    area_data = map_areas(issues)
    area_data = remove_duplicates(area_data)
    area_data = generate_root_causes(area_data)
    area_data = assign_severity(area_data)

    conflicts = detect_conflicts(area_data)

    report = generate_report(area_data, thermal_text, images)
    return report, area_data, images
