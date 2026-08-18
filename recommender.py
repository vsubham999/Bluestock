import pandas as pd


def recommend_funds(
    risk_appetite,
    scorecard_path="data/processed/fund_scorecard.csv",
    master_path="data/raw/01_fund_master.csv"
):

    
    scorecard = pd.read_csv(scorecard_path)
    master = pd.read_csv(master_path)

    
    scorecard.columns = (
        scorecard.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    master.columns = (
        master.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("Scorecard columns:")
    print(scorecard.columns.tolist())

    print("\nFund master columns:")
    print(master.columns.tolist())


    if "sharpe_ratio" not in scorecard.columns:
        raise KeyError(
            "sharpe_ratio column not found."
        )

    if "amfi_code" not in scorecard.columns:
        raise KeyError(
            "amfi_code missing from fund_scorecard."
        )

    if "amfi_code" not in master.columns:
        raise KeyError(
            "amfi_code missing from fund master."
        )


    risk_candidates = [
        "risk_grade",
        "risk",
        "risk_category",
        "risk_level",
        "riskometer"
    ]

    risk_col = None

    for col in risk_candidates:
        if col in master.columns:
            risk_col = col
            break

    if risk_col is None:
        raise KeyError(
            "No risk-grade column found in fund master."
        )

    print("\nUsing risk column:", risk_col)


    master_risk = master[
        ["amfi_code", risk_col]
    ].copy()


    master_risk = master_risk.drop_duplicates(
        subset=["amfi_code"]
    )

    
    funds = scorecard.merge(
        master_risk,
        on="amfi_code",
        how="left"
    )


    funds = funds.rename(
        columns={
            risk_col: "risk_grade"
        }
    )

    
    funds["risk_grade"] = (
        funds["risk_grade"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    
    funds["sharpe_ratio"] = pd.to_numeric(
        funds["sharpe_ratio"],
        errors="coerce"
    )

    funds = funds.dropna(
        subset=[
            "risk_grade",
            "sharpe_ratio"
        ]
    )

    
    risk_appetite = (
        risk_appetite
        .strip()
        .lower()
    )

    valid_risks = [
        "low",
        "moderate",
        "high"
    ]

    if risk_appetite not in valid_risks:
        print(
            "\nInvalid risk appetite."
        )
        print(
            "Choose: Low, Moderate, or High."
        )
        return pd.DataFrame()

    
    matching = funds[
        funds["risk_grade"] == risk_appetite
    ].copy()

    
    recommendations = (
        matching
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    
    print("\n======================================")
    print("FUND RECOMMENDATION")
    print("======================================")

    print(
        "Risk Appetite:",
        risk_appetite.title()
    )

    if recommendations.empty:
        print(
            "\nNo matching funds found."
        )
        return recommendations

    
    name_columns = [
        "fund_name",
        "scheme_name",
        "scheme",
        "fund"
    ]

    name_col = None

    for col in name_columns:
        if col in recommendations.columns:
            name_col = col
            break


    display_columns = [
        "amfi_code",
        "risk_grade",
        "sharpe_ratio"
    ]

    if name_col:
        display_columns.insert(
            0,
            name_col
        )

    print("\nTop 3 Recommended Funds:\n")

    print(
        recommendations[
            display_columns
        ].to_string(index=False)
    )

    return recommendations



if __name__ == "__main__":

    risk = input(
        "Enter investor risk appetite "
        "(Low/Moderate/High): "
    )

    recommend_funds(risk)