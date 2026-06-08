"""
Spusti raz: python import_whoop_once.py
Importuje physiological_cycles export z WHOOP do databazy.
"""
import csv
import sys
from datetime import datetime

# Nastav cestu k CSV suboru
CSV_FILE = "physiological_cycles[1].csv"

from app import app, db, BiometricLog

with app.app_context():
    imported = 0
    skipped = 0

    with open(CSV_FILE, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw_date = row.get('Cycle start time', '').strip()
            raw_hrv  = row.get('Heart rate variability (ms)', '').strip()
            raw_rec  = row.get('Recovery score %', '').strip()
            raw_rhr  = row.get('Resting heart rate (bpm)', '').strip()

            if not raw_date or not raw_hrv:
                skipped += 1
                continue

            try:
                entry_date = datetime.strptime(raw_date[:10], '%Y-%m-%d').date()
                hrv_val = float(raw_hrv)
            except (ValueError, TypeError):
                skipped += 1
                continue

            try:
                rec_val = int(float(raw_rec)) if raw_rec else 0
            except ValueError:
                rec_val = 0

            try:
                rhr_val = int(float(raw_rhr)) if raw_rhr else None
            except ValueError:
                rhr_val = None

            existing = BiometricLog.query.filter_by(date=entry_date).first()
            if existing:
                skipped += 1
                continue

            db.session.add(BiometricLog(
                date=entry_date,
                hrv=hrv_val,
                recovery=rec_val,
                rhr=rhr_val
            ))
            imported += 1

    db.session.commit()
    print(f"Import dokonceny: {imported} pridanych, {skipped} preskocených.")
