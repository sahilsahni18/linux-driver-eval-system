def score_documentation(code_text):
    lines = code_text.splitlines()
    comment_lines = [line for line in lines if line.strip().startswith("//") or line.strip().startswith("/*")]
    return min(len(comment_lines) / len(lines), 1.0)