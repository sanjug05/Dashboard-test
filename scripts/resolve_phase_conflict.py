#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('index.html')
text = TARGET.read_text()

start = "<<<<<<< "
if start not in text:
    print('No conflict markers found.')
    raise SystemExit(0)

ours_snippet = """  document.querySelectorAll('.phase-date').forEach(i=>{\n    const pid=i.dataset.phase;\n    const val=i.value;\n    i.classList.remove('input-error');\n    if(!val||!startDate)return;\n    const actualDate=new Date(val);\n    if(actualDate<startDate){\n      i.classList.add('input-error');\n      showToast(`${PHASES_CONFIG.find(p=>p.id===pid)?.name||pid}: Date cannot be before start date`,'error');\n      hasValidationError=true;\n      return;\n    }\n    const phaseConfig=PHASES_CONFIG.find(p=>p.id===pid);\n    if(!phaseConfig)return;\n    const targetDate=new Date(startDate);\n    targetDate.setDate(startDate.getDate()+phaseConfig.days);\n    const diff=Math.ceil((actualDate-targetDate)/86400000);\n    if(diff>phaseConfig.days*2)i.classList.add('input-error');\n  });"""

# Resolve only the specific known conflict hunk.
marker_start = text.find("<<<<<<< ")
if marker_start == -1:
    print('No conflict markers found.')
    raise SystemExit(0)
marker_end = text.find(">>>>>>>", marker_start)
if marker_end == -1:
    print('Unclosed conflict marker; aborting.')
    raise SystemExit(1)
marker_end = text.find("\n", marker_end)
if marker_end == -1:
    marker_end = len(text)

chunk = text[marker_start:marker_end]
if ".phase-date" not in chunk:
    print('Conflict found, but not the known phase-date hunk. No changes made.')
    raise SystemExit(1)

updated = text[:marker_start] + ours_snippet + text[marker_end:]
TARGET.write_text(updated)
print('Resolved known phase-date conflict in index.html')
