def detect_advanced_features(code_text):
    features = {
        "power_management": "suspend" in code_text or "resume" in code_text,
        "device_tree": "of_device_id" in code_text,
        "debug_support": "pr_debug" in code_text or "dev_dbg" in code_text
    }
    score = sum(1 for used in features.values() if used) / len(features)
    return round(score, 2)
