from evaluation_engine import compile_driver, run_static_analysis
from metrics_calculator import calculate_weighted_metrics
import json

def evaluate_model_output(code_file):
    success, warnings, errors = compile_driver(code_file)
    static_output = run_static_analysis(code_file)
    metrics = calculate_weighted_metrics(success, warnings, errors, static_output)

    print("Evaluation Results:")
    print(json.dumps(metrics, indent=2))
    with open("app/results/output_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

if __name__ == "__main__":
    evaluate_model_output("app/generated_code/sample_driver.c")