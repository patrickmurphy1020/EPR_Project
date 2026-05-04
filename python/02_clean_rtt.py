import pandas as pd

# Input and output paths
input_path = "../data/real/nhs/rtt_waiting_list.csv"
output_path = "../data/processed/rtt_waiting_list_clean.csv"

# Load raw RTT file
df = pd.read_csv(input_path)

# ============================================================
# 1. FILTER TO INCOMPLETE PATHWAYS ONLY (Part_2)
# ============================================================
df = df[df["RTT Part Type"] == "Part_2"]

# ============================================================
# 2. FILTER TO ACUTE NHS TRUSTS ONLY
#    Trust ODS codes are always 3 characters and start with 'R'
# ============================================================
df = df[df["Provider Org Code"].str.match(r"^R[A-Z0-9]{2}$")]

# ============================================================
# 3. IDENTIFY WEEK BUCKET COLUMNS
# ============================================================
week_cols = [col for col in df.columns if "Weeks" in col]

# ============================================================
# 4. CONVERT WEEK BUCKETS TO NUMERIC
# ============================================================
for col in week_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# ============================================================
# 5. GROUP BY TRUST AND SUM ALL WEEK BUCKETS
# ============================================================
df_grouped = df.groupby(
    ["Provider Org Code", "Provider Org Name"]
)[week_cols].sum().reset_index()

# Rename columns
df_grouped = df_grouped.rename(columns={
    "Provider Org Code": "TrustCode",
    "Provider Org Name": "TrustName"
})

# ============================================================
# 6. CREATE KEY METRICS
# ============================================================

# Total waiting list = sum of all week buckets
df_grouped["Total_Waiting_List"] = df_grouped[week_cols].sum(axis=1)

# 52-week waits (>= 52 weeks)
week_52_cols = [col for col in week_cols if "52" in col or "53" in col or "54" in col or "55" in col or "56" in col or "57" in col or "58" in col or "59" in col or "60" in col or "61" in col or "62" in col or "63" in col or "64" in col or "65" in col or "66" in col or "67" in col or "68" in col or "69" in col or "70" in col or "71" in col or "72" in col or "73" in col or "74" in col or "75" in col or "76" in col or "77" in col or "78" in col or "79" in col or "80" in col or "81" in col or "82" in col or "83" in col or "84" in col or "85" in col or "86" in col or "87" in col or "88" in col or "89" in col or "90" in col or "91" in col or "92" in col or "93" in col or "94" in col or "95" in col or "96" in col or "97" in col or "98" in col or "99" in col or "100" in col or "101" in col or "102" in col or "103" in col or "104" in col]
df_grouped["WL_52w"] = df_grouped[week_52_cols].sum(axis=1)

# 65-week waits (>= 65 weeks)
week_65_cols = [col for col in week_cols if "65" in col or "66" in col or "67" in col or "68" in col or "69" in col or "70" in col or "71" in col or "72" in col or "73" in col or "74" in col or "75" in col or "76" in col or "77" in col or "78" in col or "79" in col or "80" in col or "81" in col or "82" in col or "83" in col or "84" in col or "85" in col or "86" in col or "87" in col or "88" in col or "89" in col or "90" in col or "91" in col or "92" in col or "93" in col or "94" in col or "95" in col or "96" in col or "97" in col or "98" in col or "99" in col or "100" in col or "101" in col or "102" in col or "103" in col or "104" in col]
df_grouped["WL_65w"] = df_grouped[week_65_cols].sum(axis=1)

# 78-week waits (>= 78 weeks)
week_78_cols = [col for col in week_cols if "78" in col or "79" in col or "80" in col or "81" in col or "82" in col or "83" in col or "84" in col or "85" in col or "86" in col or "87" in col or "88" in col or "89" in col or "90" in col or "91" in col or "92" in col or "93" in col or "94" in col or "95" in col or "96" in col or "97" in col or "98" in col or "99" in col or "100" in col or "101" in col or "102" in col or "103" in col or "104" in col]
df_grouped["WL_78w"] = df_grouped[week_78_cols].sum(axis=1)

# 104-week waits (>= 104 weeks)
week_104_cols = [col for col in week_cols if "104" in col]
df_grouped["WL_104w"] = df_grouped[week_104_cols].sum(axis=1)

# ============================================================
# 7. KEEP ONLY FINAL METRICS
# ============================================================
df_final = df_grouped[[
    "TrustCode",
    "TrustName",
    "Total_Waiting_List",
    "WL_52w",
    "WL_65w",
    "WL_78w",
    "WL_104w"
]]

# ============================================================
# 8. SAVE CLEANED OUTPUT
# ============================================================
df_final.to_csv(output_path, index=False)

print("RTT dataset cleaned and saved to:", output_path)
