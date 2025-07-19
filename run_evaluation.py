from evaluation_engine import compile_driver, run_static_analysis
from metrics_calculator import calculate_metrics
import json

def evaluate_model_output(code_file):
    success, warnings, errors = compile_driver(code_file)
    static_issues = run_static_analysis(code_file)
    metrics = calculate_metrics(success, warnings, errors)

    print("Evaluation Results:")
    print(json.dumps(metrics, indent=2))
    print("\\nStatic Analysis Output:\\n", static_issues)

    with open("app/results/output_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

if __name__ == "__main__":
    evaluate_model_output("app/generated_code/sample_driver.c")
