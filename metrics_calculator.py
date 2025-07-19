def calculate_metrics(success, warnings, errors):
    score = 0
    if success:
        score += 50
    score -= warnings * 0.5
    score -= errors * 2

    return {
        "compilation": {
            "success_rate": 1.0 if success else 0.0,
            "warnings_count": warnings,
            "errors_count": errors
        },
        "overall_score": max(score, 0)
    }
