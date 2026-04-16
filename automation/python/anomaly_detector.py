import pandas as pd
import os
from datetime import datetime

# --- SENIOR ARCHITECTURE: DYNAMIC ABSOLUTE PATHING ---
# Using __file__ ensures the script finds its data regardless of 
# which directory the terminal is currently in.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Logic to map the folder structure based on Flutter UKI project standards
INPUT_PATH = os.path.join(BASE_DIR, "data", "input", "transactions.xlsx")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "output", "flagged_transactions.xlsx")
LOG_PATH = os.path.join(BASE_DIR, "data", "logs", "execution_log.txt")

def log_message(message):
    """Encapsulated logging for audit trails (JD: Risk & Issue Management)"""
    # Ensure logs directory exists before writing
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def detect_anomalies():
    """
    Core Decision Layer for Settlement Reconciliation.
    Processes high-volume financial data to isolate settlement mismatches.
    """
    try:
        log_message("SYSTEM_INIT: Anomaly Detection Engine engaged.")

        # 1. PRE-FLIGHT VALIDATION
        if not os.path.exists(INPUT_PATH):
            error = f"DATA_NOT_FOUND: Ingestion failed at {INPUT_PATH}"
            log_message(error)
            print(f"❌ {error}")
            return

        # 2. DATA INGESTION
        # Explicitly using openpyxl engine to handle complex .xlsx files
        df = pd.read_excel(INPUT_PATH, engine="openpyxl")

        # 3. SCHEMA VALIDATION
        required_columns = ["Transaction_ID", "Expected_Amount", "Actual_Amount"]
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"CRITICAL_SCHEMA_MISMATCH: Missing required field '{col}'")

        # 4. TRANSFORMATION & LOGIC (The 'Decision' Engine)
        # Identifies any discrepancy between expected and actual settlement
        df["Mismatch"] = df["Expected_Amount"] != df["Actual_Amount"]
        flagged_df = df[df["Mismatch"] == True].copy()

        # 5. SECURE OUTPUT GENERATION
        # JD Alignment: Ensures a clean hand-off for RPA (UiPath) ingestion
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        flagged_df.to_excel(OUTPUT_PATH, index=False)

        # 6. ANALYTICS & AUDIT SUMMARY
        total_records = len(df)
        mismatch_count = len(flagged_df)
        
        log_message(f"AUDIT_COMPLETE: Processed {total_records} records. Flags: {mismatch_count}")
        
        # Professional standard terminal feedback
        print("✅ Core Decision Layer: Process Completed Successfully")
        print(f"   > Integrity Check: {total_records} Rows Scanned")
        print(f"   > Anomalies Identified: {mismatch_count}")

    except Exception as e:
        error_msg = f"EXCEPTION_CAUGHT: {str(e)}"
        print(f"❌ {error_msg}")
        log_message(error_msg)

if __name__ == "__main__":
    detect_anomalies()
