# CLAUDE.md — Working principles for the CaliHeatWaves repository

**Read this before every task in this repository.** These rules exist because this is a scientific research project. The correctness of conclusions matters more than the code appearing to run. Silent failure is the worst outcome.

## 1. Never substitute data silently
If an expected input file is missing, incomplete, or wrong, raise a clear error naming what is missing. Never fall back to a "demonstration" file, a subset, or a test file. The user must be told what is missing so they can fix the real problem.

## 2. Never add try/except, "if exists", or fallback branches that hide errors
Errors are information. Suppressing them destroys it. The only acceptable use of try/except is when the exception path does something the user has explicitly asked for.

## 3. Never claim "success" or "fixed" without verifying correct scientific output
"The code runs without error" is not the same as "the code is correct." Before claiming a fix works, verify against a concrete expected value or behavior. Example: "The mean temperature is 23.4 °C, consistent with Cali's climatology" — not "the notebook executed 15 cells successfully."

## 4. Do not add code the user did not ask for
No auto-detection, no smart path guessing, no helpful progress bars, no debug wrappers. Solve exactly the stated problem. If ambiguous, ask.

## 5. If a file, path, or filename is not exactly what the code expects, stop and report
Do not glob for a pattern to catch "probably the right file." Use the exact expected filename. If it is not present, the user needs to know.

## 6. Prefer removing complexity over adding it
When code is failing, ask first whether it should be simpler, not whether more guards should be added. Extra branches, checks, and fallbacks are usually the wrong direction.

## 7. Report changes precisely and briefly
State which lines in which files changed and why. Do not use checkmarks, "✅ perfect", or celebratory language. If a fix required multiple attempts, say so honestly.

## 8. Assumptions are lies waiting to happen
If you assume a file is netCDF, verify it. If you assume a folder has 12 files, count them. State assumptions explicitly at the top of a change and check them before applying it.

## 9. When in doubt, ask a specific question — do not proceed
"Should the notebook fall back to test data if 2024 is incomplete, or fail?" is a good question. Do not decide silently.

## 10. Do not "improve" code that was not the target of the request
One task at a time, scoped exactly. If asked to fix a notebook, do not simultaneously refactor the download script or environment.

## Repository-specific notes

- Language of code and comments: English. Language of the user: Spanish/English mixed. Respond in the language the user writes in.
- Environment: micromamba env `caliheatwaves`, Python 3.11. Never install packages or modify the environment without asking.
- Data sources are external (Copernicus, DANE, IDEAM). Never mock or simulate their responses.
- Analysis notebooks live under `layer1_climatology/notebooks/`, `layer2_mortality/notebooks/`, `layer3_attribution/notebooks/`. Do not mix layers.
- Do not modify files under `shared/data/raw/` — that is source data.
