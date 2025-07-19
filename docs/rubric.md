# 📊 Evaluation Rubric

## 🎯 Goal
To evaluate how well an AI-generated Linux device driver performs in terms of correctness, safety, quality, and completeness.

---

## ⚙️ Metrics Breakdown

| Category       | Sub-metrics                     | Weight |
|----------------|----------------------------------|--------|
| Compilation    | success, warnings, errors        | 40%    |
| Functionality  | basic ops, error handling, edge  | 20%    |
| Security       | buffer safety, race checks, input| 25%    |
| Code Quality   | style, docs, maintainability     | 15%    |

---

## ✅ Scoring Criteria

### 1. Compilation (40%)
- ✅ Compiles successfully → +40 points
- ⚠️ Each warning → -0.3 pts
- ❌ Each error → -1.5 pts

### 2. Functionality (20%)
- Scored from placeholders or runtime test hooks (if used)
- Based on expected use-case completeness

### 3. Security (25%)
- Regex-based flags for:
  - `buffer overflow`
  - `data race`
  - `tainted input`
- Static value or zero if flagged

### 4. Code Quality (15%)
- Style checked by clang-tidy
- Documentation comment ratio
- Maintainability scored from readability

---

## 🏁 Output Format

```json
{
  "compilation": {...},
  "functionality": {...},
  "security": {...},
  "code_quality": {...},
  "overall_score": 78.5
}
```

All metrics are normalized to a 100-point scale.
