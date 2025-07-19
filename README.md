# Linux Device Driver Evaluation System

## 🚀 Overview

This project evaluates the performance of AI coding models in generating Linux kernel device drivers. It benchmarks code generation against key metrics such as compilation success, functionality, security, and code quality.

## 📁 Project Structure

```
linux_driver_eval_system/
├── app/
│   ├── generated_code/        # Generated drivers by AI models
│   ├── results/               # Evaluation outputs (JSON)
├── docs/                      # Architecture and evaluation rubrics
├── evaluation_engine.py       # Compilation and static checks
├── metrics_calculator.py      # Weighted metric scoring
├── run_evaluation.py          # Entry point for evaluation
├── requirements.txt
└── README.md
```

## 📦 Dependencies

- `gcc`
- `clang-tidy`
- Python 3.7+
- Linux kernel headers (if compiling modules)

Install with:

```bash
sudo apt install gcc clang-tidy linux-headers-$(uname -r)
pip install -r requirements.txt
```

## ▶️ Run Evaluation

```bash
python run_evaluation.py
```

This evaluates the driver located at `app/generated_code/sample_driver.c` and outputs a JSON file in `app/results/`.

## 🧠 What It Measures

- Compilation success rate and diagnostics
- Static analysis warnings (clang-tidy)
- Functional placeholder scores
- Security checks (based on pattern matching)
- Code quality style and maintainability

## 📄 Documentation

See `docs/architecture.md` and `docs/rubric.md` for internals and grading system.
