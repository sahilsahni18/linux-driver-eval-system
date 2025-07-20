def check_resource_management(code_text):
    alloc_patterns = ["kmalloc", "vmalloc"]
    free_patterns = ["kfree", "vfree"]
    alloc_present = any(kw in code_text for kw in alloc_patterns)
    free_present = any(kw in code_text for kw in free_patterns)
    if alloc_present and free_present:
        return 1.0
    elif alloc_present and not free_present:
        return 0.4
    else:
        return 0.7  # neutral if no dynamic allocation