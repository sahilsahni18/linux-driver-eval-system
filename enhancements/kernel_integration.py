def check_kernel_integration(code_text):
    keywords = ["register_chrdev", "unregister_chrdev", "module_init", "module_exit"]
    score = sum(1 for kw in keywords if kw in code_text)
    return min(score / len(keywords), 1.0)  # normalized score