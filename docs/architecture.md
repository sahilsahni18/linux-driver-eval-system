# 📐 System Architecture

## Components

### 1. `evaluation_engine.py`
Handles:
- Compilation of C source files using `gcc`
- Static analysis using `clang-tidy`
- Captures warnings/errors from output

### 2. `metrics_calculator.py`
Implements:
- Weighted scoring system (100-point scale)
- Scores compilation, functionality, security, code quality
- Uses regex pattern matching on static analysis reports

### 3. `run_evaluation.py`
Acts as the main pipeline:
- Accepts path to driver file
- Runs compilation and analysis
- Collects metrics
- Outputs JSON result

## Flow Diagram

```
[Driver C Code]
      ↓
[Evaluation Engine] → Compilation + Static Checks
      ↓
[Metrics Calculator] → Scoring Engine
      ↓
[JSON Output Report]
```
