import pandas as pd

# =========================
# 1. Clean RPPI Data
# =========================
def clean_rppi(path="data/raw/rppi_full.xlsx"):
    print("[Transform] Cleaning RPPI data...")
    df = pd.read_excel(path, sheet_name="Data1")

    print("[DEBUG] RPPI Columns:", df.columns)

    df = df.rename(columns={df.columns[0]: "quarter"})
    df_melted = df.melt(id_vars=["quarter"], var_name="state", value_name="price_index")
    df_melted = df_melted.dropna(subset=["quarter", "state", "price_index"])
    return df_melted


# =========================
# 2. Clean Median Transfers Data
# =========================
def clean_median_transfers(path="data/raw/median_transfers.xlsx"):
    print("[Transform] Cleaning Median Transfers data...")
    df = pd.read_excel(path, sheet_name="Data1")

    print("[DEBUG] Median Transfers Columns:", df.columns)

    df = df.rename(columns={df.columns[0]: "quarter"})
    df_melted = df.melt(id_vars=["quarter"], var_name="state", value_name="median_price_or_transfers")
    df_melted = df_melted.dropna(subset=["quarter", "state", "median_price_or_transfers"])
    return df_melted


# =========================
# 3. Clean Population Data
# =========================
def clean_population(path="data/raw/erp_population.xlsx"):
    print("[Transform] Cleaning Population data...")
    df = pd.read_excel(path, sheet_name="Data1")

    print("[DEBUG] Population Columns:", df.columns)

    df = df.rename(columns={df.columns[0]: "quarter"})
    df_melted = df.melt(id_vars=["quarter"], var_name="state", value_name="population")
    df_melted = df_melted.dropna(subset=["quarter", "state", "population"])
    return df_melted


# =========================
# 4. Clean Migration Data
# =========================
def clean_migration(path="data/raw/net_migration.xlsx"):
    print("[Transform] Cleaning Net Migration data...")
    df = pd.read_excel(path, sheet_name="Data1")

    print("[DEBUG] Migration Columns:", df.columns)

    df = df.rename(columns={df.columns[0]: "quarter"})
    df_melted = df.melt(id_vars=["quarter"], var_name="state", value_name="net_migration")
    df_melted = df_melted.dropna(subset=["quarter", "state", "net_migration"])
    return df_melted


# =========================
# 5. Transform All
# =========================
def transform_all():
    df_rppi = clean_rppi()
    df_rppi.to_csv("data/processed/rppi.csv", index=False)

    df_median = clean_median_transfers()
    df_median.to_csv("data/processed/median_transfers.csv", index=False)

    df_population = clean_population()
    df_population.to_csv("data/processed/population.csv", index=False)

    df_migration = clean_migration()
    df_migration.to_csv("data/processed/net_migration.csv", index=False)


if __name__ == "__main__":
    transform_all()
