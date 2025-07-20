def check_error_handling(code_text):
    return 1.0 if "return" in code_text and ("if" in code_text or "goto" in code_text) else 0.4
