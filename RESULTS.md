# Results

Exploratory study of LLM behavior under forced numerical output constraints.

## Fabrication rates

| Model | Total | Fabricated | Rate |
|---|---|---|---|
| dolphin | 75 | 26 | 34.7% |
| gemini-flash | 77 | 12 | 15.6% |
| gpt-4o-mini | 77 | 7 | 9.1% |
| GLM-4.5 | 27 | 1 | 3.7% |
| claude-haiku | 75 | 0 | 0% |

## Key findings

1. Compliance token (0) observed in 3+ models
2. Breaking points span L1 to never
3. Institutional pressure does not break aligned models
4. job_loss is the strongest attack vector

## Data

Raw: data/raw/*.json
Processed: data/processed/results.csv
