import pandas as pd
import os
from datetime import datetime

# ==============================
# CONFIGURATION
# ==============================

INPUT_PATH = "../data/input/transactions.xlsx"
OUTPUT_PATH = "../data/output/flagged_transactions.xlsx"
LOG_PATH = "../data/logs/execution_log.txt"

# ==============================
# LOG FUNCTION
# ==============================

def log_message(message):
    with open(LOG_PATH, "a") as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")

# ==============================
# MAIN FUNCTION
# ==============================

def detect_anomalies():
    try:
        log_message("Process started")

        # Check if file exists
        if not os.path.exists(INPUT_PATH):
            raise FileNotFoundError(f"Input file not found: {INPUT_PATH}")

        # Load Excel
        df = pd.read_excel(INPUT_PATH, engine="openpyxl")

        # Validate required columns
        required_columns = ["Transaction_ID", "Expected_Amount", "Actual_Amount"]
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Missing column: {col}")

        # Detect mismatches
        df["Mismatch"] = df["Expected_Amount"] != df["Actual_Amount"]

        # Filter mismatches
        flagged_df = df[df["Mismatch"] == True]

        # Save output
        flagged_df.to_excel(OUTPUT_PATH, index=False)

        # Logging results
        total_records = len(df)
        mismatch_count = len(flagged_df)

        log_message(f"Total records processed: {total_records}")
        log_message(f"Mismatches found: {mismatch_count}")

        print("✅ Anomaly detection complete.")
        print(f"📊 Total Records: {total_records}")
        print(f"⚠️ Mismatches Found: {mismatch_count}")

        log_message("Process completed successfully")

    except Exception as e:
        error_message = f"Error: {str(e)}"
        print(error_message)
        log_message(error_message)


# ==============================
# ENTRY POINT
# ==============================

if __name__ == "__main__":
    detect_anomalies()