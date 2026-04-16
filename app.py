import os
import sys
import time
import pandas as pd
from datetime import datetime

# --- SENIOR ARCHITECTURE: DYNAMIC PATH INJECTION ---
# We define the root directory first to ensure absolute stability.
# This prevents 'blank' screens caused by path resolution failures.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Professional Import Handling
try:
    # Based on your file list, anomaly_detector.py is in the same folder as app.py
    from anomaly_detector import detect_anomalies
except ImportError:
    try:
        # Fallback if you move it to a subfolder later
        from automation.python.anomaly_detector import detect_anomalies
    except ImportError as e:
        print(f"❌ CRITICAL CONFIGURATION ERROR: {e}")
        print(f"System expected dependency at: {BASE_DIR}")
        input("\nPress Enter to exit...")
        sys.exit(1)

# --- STRATEGIC ROI METRICS (JD Alignment: 'Automation Benefits') ---
# These values position you as a BA who understands the 'Flutter Edge'
GBP_SAVINGS_PER_TX = 1.25 
ERROR_THRESHOLD_PERCENT = 0.05 

def generate_stakeholder_report(start_time):
    """
    JD Requirement: 'Delivers performance reports for stakeholders'
    Calculates operational efficiency and risk.
    """
    try:
        # Explicit Absolute Paths to ensure the report ALWAYS renders
        input_path = os.path.join(BASE_DIR, "data", "input", "transactions.xlsx")
        output_path = os.path.join(BASE_DIR, "data", "output", "flagged_transactions.xlsx")

        if not os.path.exists(input_path):
            print(f"⚠️  METRICS DELAYED: Source file not found at {input_path}")
            return

        # Use engine='openpyxl' to avoid common format errors
        input_df = pd.read_excel(input_path, engine="openpyxl")
        total_vol = len(input_df)
        
        flagged_vol = 0
        if os.path.exists(output_path):
            flagged_df = pd.read_excel(output_path, engine="openpyxl")
            flagged_vol = len(flagged_df)

        roi_savings = total_vol * GBP_SAVINGS_PER_TX
        integrity_rate = ((total_vol - flagged_vol) / total_vol * 100) if total_vol > 0 else 0

        # RENDER EXECUTIVE DASHBOARD
        print("\n" + "█"*65)
        print(f" SENTINEL CORE v2.4 | SETTLEMENT INTEGRITY EXECUTIVE REPORT")
        print("█"*65)
        print(f" BATCH STATUS:      COMPLETED")
        print(f" THROUGHPUT:        {total_vol} Transactions")
        print(f" INTEGRITY RATE:    {integrity_rate:.2f}%")
        print(f" ANOMALIES FOUND:   {flagged_vol} (Auto-Flagged for RPA)")
        print(f" OPERATIONAL ROI:   £{roi_savings:,.2f}")
        print(f" ENGINE LATENCY:    {time.time() - start_time:.4f}s")
        print("█"*65)

        # JD Requirement: 'Perform risk and issue management'
        if integrity_rate < 95:
            print(f"⚠️  RISK ALERT: Batch integrity ({integrity_rate:.2f}%) is below SLA.")
            print("   Escalating to Finance Lead for manual verification.")
        
    except Exception as e:
        print(f"⚠️  BA Metric Generation Interrupted: {e}")

def main():
    start_time = time.time()
    print(f"--- [INITIALIZING SENTINEL ENGINE | {datetime.now().strftime('%H:%M:%S')}] ---")
    print("Connecting to Data layer...")

    try:
        # 1. TRIGGER CORE ENGINE
        detect_anomalies()

        # 2. GENERATE STRATEGIC REPORT
        generate_stakeholder_report(start_time)

        print("\n--- Process Cycle Complete ---")
        input("PROMPT: Execution finished. Press Enter to close dashboard...") 

    except Exception as e:
        print(f"❌ SYSTEM EXCEPTION: {str(e)}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
