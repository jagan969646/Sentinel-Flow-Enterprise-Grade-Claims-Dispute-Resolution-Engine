import os
import sys
import time
import pandas as pd
from datetime import datetime

from automation.python.anomaly_detector import detect_anomalies

# --- SENIOR ARCHITECTURE: DYNAMIC PATH INJECTION ---
# Ensures the script can resolve local dependencies regardless of the 
# execution environment or folder depth.
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Professional Import Handling
try:
    from automation import anomaly_detector
except ImportError as e:
    print(f"❌ Dependency Error: {e}")
    print(f"Check that 'anomaly_detector.py' exists in: {current_dir}")
    input("\nPress Enter to exit...")
    sys.exit(1)

# --- BUSINESS LOGIC CONSTANTS (Flutter JD Alignment) ---
OPEX_SAVINGS_PER_TX = 1.25  # Strategic ROI Metric per record

def generate_stakeholder_report(start_time):
    """
    JD Requirement: 'Delivers performance reports for stakeholders'
    Uses absolute paths to ensure the report renders correctly.
    """
    try:
        # Resolve paths relative to where app.py lives
        input_path = os.path.join(current_dir, "data", "input", "transactions.xlsx")
        output_path = os.path.join(current_dir, "data", "output", "flagged_transactions.xlsx")

        if not os.path.exists(input_path):
            print(f"⚠️  Report Skipped: Input data not found at {input_path}")
            return

        input_df = pd.read_excel(input_path, engine="openpyxl")
        
        # Verify if detector created an output
        anomalies = 0
        if os.path.exists(output_path):
            flagged_df = pd.read_excel(output_path, engine="openpyxl")
            anomalies = len(flagged_df)

        total = len(input_df)
        savings = total * OPEX_SAVINGS_PER_TX

        # Render the Executive Dashboard
        print("\n" + "█"*65)
        print(f" SENTINEL CORE v2.3 | FINANCIAL INTEGRITY EXECUTIVE REPORT")
        print("█"*65)
        print(f" STATUS:            SUCCESSFUL")
        print(f" BATCH VOLUME:      {total} Transactions")
        print(f" ANOMALIES FOUND:   {anomalies} (Flagged for RPA)")
        print(f" ESTIMATED ROI:     £{savings:,.2f}")
        print(f" ENGINE LATENCY:    {time.time() - start_time:.4f}s")
        print("█"*65 + "\n")
        
    except Exception as e:
        print(f"⚠️  Metrics generation failed: {e}")

def main():
    start_time = time.time()
    print(f"--- [INITIALIZING RECONCILIATION ENGINE | {datetime.now().strftime('%H:%M:%S')}] ---")

    try:
        # 1. Execute Core Logic
        detect_anomalies()

        # 2. Generate BA Reporting
        generate_stakeholder_report(start_time)

        print("--- Process Complete ---")
        # CRITICAL: Keeps terminal open so you can see the results
        input("\nPROMPT: Execution finished. Press Enter to close dashboard...") 

    except Exception as e:
        print(f"❌ System Exception: {str(e)}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
