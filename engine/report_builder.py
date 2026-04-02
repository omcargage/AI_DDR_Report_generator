def generate_report(area_data, thermal, images):

    report = "# DETAILED DIAGNOSTIC REPORT\n\n"

    # 1. Property Summary
    report += "## 1. Property Issue Summary\n"
    report += "Multiple moisture and structural issues identified.\n\n"

    # 2. Area-wise Observations
    report += "## 2. Area-wise Observations\n"

    for area, issues in area_data.items():
        report += f"\n### {area}\n"

        for i, issue in enumerate(issues):
            report += f"- {issue['issue']}\n"

            # Image
            if i >= len(images):
                report += "Image Not Available\n"

    # 3 Root Cause
    report += "\n## 3. Probable Root Cause\n"
    for area in area_data:
        for issue in area_data[area]:
            report += f"- {issue['issue']}: {issue.get('root_cause','Not Available')}\n"

    # 4 Severity
    report += "\n## 4. Severity Assessment\n"
    for area in area_data:
        for issue in area_data[area]:
            report += f"- {issue['issue']}: {issue['severity']} ({issue['severity_reason']})\n"

    # 5 Recommendations
    report += "\n## 5. Recommended Actions\n"
    for area in area_data:
        for issue in area_data[area]:
            report += f"- {issue['recommendation']}\n"

    # 6 Additional Notes
    report += "\n## 6. Additional Notes\n"
    report += "Report generated using automated analysis.\n"

    # 7 Missing Info
    report += "\n## 7. Missing or Unclear Information\n"
    report += "Some inspection details may be unavailable.\n"

    return report
    return report, area_data