import re
from enhancements.kernel_integration import check_kernel_integration
from enhancements.resource_management import check_resource_management
from enhancements.error_handling import check_error_handling
from enhancements.documentation import score_documentation
from enhancements.advanced_features import detect_advanced_features

def calculate_weighted_metrics(success, warnings, errors, static_analysis_output, code_text):
    # ---- COMPILATION METRICS ----
    compilation_score = 0
    if success:
        compilation_score += 40
    compilation_score -= warnings * 0.3
    compilation_score -= errors * 1.5
    compilation_score = max(compilation_score, 0)

    # ---- FUNCTIONALITY (still placeholder) ----
    error_handling_score = check_error_handling(code_text)
    functionality = {
        "basic_operations": 0.9,
        "error_handling": error_handling_score,
        "edge_cases": 0.6
    }
    functionality_score = (
        functionality["basic_operations"] * 0.5 +
        functionality["error_handling"] * 0.3 +
        functionality["edge_cases"] * 0.2
    ) * 20

    # ---- SECURITY ----
    buffer_safety = 0.95 if "buffer overflow" not in static_analysis_output else 0.5
    race_conditions = 0.8 if "data race" not in static_analysis_output else 0.5
    input_validation = 0.7 if "tainted input" not in static_analysis_output else 0.5
    resource_management = check_resource_management(code_text)
    security_score = (
        buffer_safety * 0.3 +
        race_conditions * 0.2 +
        input_validation * 0.2 +
        resource_management * 0.3
    ) * 25

    # ---- CODE QUALITY ----
    style_compliance = 0.88
    documentation = score_documentation(code_text)
    maintainability = 0.75
    code_quality_score = (
        style_compliance * 0.4 +
        documentation * 0.3 +
        maintainability * 0.3
    ) * 15

    # ---- ADVANCED FEATURES ----
    advanced_features = detect_advanced_features(code_text)
    advanced_score = advanced_features * 5

    # ---- KERNEL INTEGRATION ----
    kernel_integration_score = check_kernel_integration(code_text) * 5

    # ---- OVERALL SCORE ----
    overall = (
        compilation_score +
        functionality_score +
        security_score +
        code_quality_score +
        advanced_score +
        kernel_integration_score
    )

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
            "input_validation": input_validation,
            "resource_management": resource_management
        },
        "code_quality": {
            "style_compliance": style_compliance,
            "documentation": documentation,
            "maintainability": maintainability
        },
        "integration": {
            "kernel_api_usage": kernel_integration_score
        },
        "advanced_features": {
            "score": advanced_features
        },
        "overall_score": round(overall, 2)
    }
