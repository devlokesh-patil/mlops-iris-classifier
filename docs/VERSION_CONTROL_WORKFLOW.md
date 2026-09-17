# Version Control Workflow — [Project Name]

## 1. Overview

This document describes the Git-based version control workflow used for this
Machine Learning project, developed as part of MLOps Lab Experiment 2.

- **Repository:** https://github.com/<your-username>/ml-mlops-lab2
- **Primary language:** Python
- **Maintainer(s):** [Your Name]

## 2. Branching Strategy

| Branch | Purpose |
|--------------------|------------------------------------------------------|
| `main` | Stable, always-deployable code |
| `develop` | Integration branch for day-to-day development |
| `feature/<name>` | Individual features, branched from and merged back into `develop` |
| `conflict-demo-*` | Demonstration branches created for conflict resolution practice |

**Rule:** No one commits directly to `main`. All changes flow:

`feature/*` → Pull Request → `develop` → (periodically) merged into `main`.

## 3. Commit Convention

Commits follow a short, imperative style with a type prefix:

## feat: add new functionality
fix: correct a bug
docs: documentation changes
chore: tooling/config changes
refactor: code change with no behavior change

Example: `feat: add classification report to training script`

## 4. Standard Workflow (Feature Development)

```bash
git switch develop
git pull origin develop
git switch -c feature/<short-description>
# ... make changes ...
git add <files>
git commit -m "feat: <description>"
git push -u origin feature/<short-description>
# Open a Pull Request into `develop` on GitHub
# After review/approval, merge via GitHub (squash or merge commit)
git branch -d feature/<short-description>
git push origin --delete feature/<short-description>
```

## 5. Merge Conflict Resolution Process

1. Attempt the merge/rebase; Git flags conflicting files.
2. Open each conflicted file and locate `<<<<<<<` / `=======` / `>>>>>>>` markers.
3. Decide which change(s) to keep — current, incoming, or a manual combination.
4. Remove all conflict markers.
5. `git add <file>` to mark the conflict as resolved.
6. `git commit` (or continue the rebase) to finalize.
7. Test the code (`python src/train.py`) before pushing to confirm nothing broke.

## 6. .gitignore Policy for ML Artifacts

Large/generated files excluded and tracked separately (DVC/cloud/Git-LFS):
raw/processed datasets, model checkpoints/binaries, virtual envs, notebook checkpoints.

## 7 PR checklist

code runs, no large files, commit messages conventional, branch up to date, PR description explains what/why.

## 8 Verification Log

git --version >=2.30, git log graph shows merged branches, repo 3+ branches, 1+ merged PR, python script prints Accuracy.

## 9 Lessons Learned/Notes.