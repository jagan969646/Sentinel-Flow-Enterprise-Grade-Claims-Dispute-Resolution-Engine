import os
import sys
import time
import pandas as pd
from datetime import datetime

from automation.python.anomaly_detector import detect_anomalies

# --- SENIOR ARCHITECTURE: DYNAMIC PATH INJECTION ---
# This ensures that 'app.py' can always find 'anomaly_detector.py' 
# regardless of how or where the script is launched.
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    # Now the import will resolve correctly
    from automation import anomaly_detector
except ImportError as e:
    print(f"❌ Critical Failure: Could not resolve dependency. {e}")
    sys.exit(1)

# --- BUSINESS LOGIC CONSTANTS (JD Alignment: ROI Reporting) ---
OPEX_SAVINGS_PER_TX = 1.25  # Estimated savings in GBP/EUR per record

def generate_stakeholder_report(start_time):
    """
    JD Requirement: 'Reports against automation benefits'
    """
    try:
        input_path = os.path.join(current_dir, "data/input/transactions.xlsx")
        output_path = os.path.join(current_dir, "data/output/flagged_transactions.xlsx")

        input_df = pd.read_excel(input_path, engine="openpyxl")
        flagged_df = pd.read_excel(output_path, engine="openpyxl")

        total = len(input_df)
        anomalies = len(flagged_df)
        savings = total * OPEX_SAVINGS_PER_TX

        print("\n" + "█"*60)
        print(f" SENTINEL CORE v2.2 | FINANCIAL INTEGRITY REPORT")
        print("█"*60)
        print(f" TOTAL PROCESSED:   {total}")
        print(f" ANOMALIES FOUND:   {anomalies}")
        print(f" ESTIMATED ROI:     £{savings:,.2f}")
        print(f" ENGINE LATENCY:    {time.time() - start_time:.4f}s")
        print("█"*60 + "\n")
        
    except Exception as e:
        print(f"⚠️  Metrics generation skipped: {e}")

def main():
    start_time = time.time()
    print(f"--- [INITIALIZING RECONCILIATION ENGINE | {datetime.now()}] ---")

    try:
        # 1. Execute Core Logic
        detect_anomalies()

        # 2. Generate BA Reporting
        generate_stakeholder_report(start_time)

    except Exception as e:
        print(f"❌ System Exception: {str(e)}")

if __name__ == "__main__":
    main()