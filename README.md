# Forced Numerical Guess

An exploratory study of LLM behavior when forced to output numerical answers they cannot know.

## Status

Exploratory pilot. Not peer-reviewed. n=1 per model family.

## Files

- RESULTS.md - findings
- METHODOLOGY.md - protocol
- scripts/ - Python scripts
- data/raw/ - raw API responses
- data/processed/ - classified results

## Key finding

Fabrication rate varies 34x across models (0% to 34.7%).
Some models use a "compliance token" (0) instead of refusing or fabricating.

## Reproduce

```bash
export OPENROUTER_API_KEY=sk-or-...
python scripts/run_all.py basic
```
