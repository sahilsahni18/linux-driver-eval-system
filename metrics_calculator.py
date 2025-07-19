import re

def calculate_weighted_metrics(success, warnings, errors, static_analysis_output):
    # ---- COMPILATION METRICS ----
    compilation_score = 0
    if success:
        compilation_score += 40  # 40% weight
    compilation_score -= warnings * 0.3
    compilation_score -= errors * 1.5
    compilation_score = max(compilation_score, 0)

    # ---- FUNCTIONALITY METRICS (dummy logic for now) ----
    functionality = {
        "basic_operations": 0.9,
        "error_handling": 0.75,
        "edge_cases": 0.6
    }
    functionality_score = (
        functionality["basic_operations"] * 0.5 +
        functionality["error_handling"] * 0.3 +
        functionality["edge_cases"] * 0.2
    ) * 20  # 20% weight

    # ---- SECURITY METRICS (example logic using static output regex) ----
    buffer_safety = 0.95 if "buffer overflow" not in static_analysis_output else 0.5
    race_conditions = 0.8 if "data race" not in static_analysis_output else 0.5
    input_validation = 0.7 if "tainted input" not in static_analysis_output else 0.5
    security_score = (
        buffer_safety * 0.4 +
        race_conditions * 0.3 +
        input_validation * 0.3
    ) * 25  # 25% weight

    # ---- CODE QUALITY METRICS ----
    style_compliance = 0.88
    documentation = 0.65
    maintainability = 0.75
    code_quality_score = (
        style_compliance * 0.4 +
        documentation * 0.3 +
        maintainability * 0.3
    ) * 15  # 15% weight

    # ---- OVERALL SCORE ----
    overall = compilation_score + functionality_score + security_score + code_quality_score

    return {
        "compilation": {
            "success_rate": 1.0 if success else 0.0,
            "warnings_count": warnings,
            "errors_count": errors
        },
        "functionality": functionality,
        "security": {
            "buffer_safety": buffer_safety,
            "race_conditions": race_conditions,
            "input_validation": input_validation
        },
        "code_quality": {
            "style_compliance": style_compliance,
            "documentation": documentation,
            "maintainability": maintainability
        },
        "overall_score": round(overall, 2)
    }

