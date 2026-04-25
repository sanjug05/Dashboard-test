# Merge Notes for `index.html`

If you keep hitting the same merge conflict around `saveShowroomPhases` (`.phase-date` validation), use this workflow:

1. Enable Git rerere once (recommended):

```bash
git config rerere.enabled true
git config rerere.autoupdate true
```

2. If conflict appears in `index.html`, run:

```bash
python scripts/resolve_phase_conflict.py
```

3. Then verify and continue merge:

```bash
git diff -- index.html
git add index.html
git commit
```

This avoids repeatedly hand-resolving the exact same hunk.
