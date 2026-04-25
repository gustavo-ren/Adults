import pandas as pd

def drop_unnecessary(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop(columns=["native-country", "education", "marital-status", "relationship",
                            "race", "sex"])


def occupation_mapping(occupation: str) -> str:
    if occupation.strip() in ["Adm-clerical", "Exec-managerial", "Prof-specialty", "Sales", "Tech-support"]:
        return "Office-Worker"
    elif occupation.strip() in ["Armed-Forces", "Protective-serv"]:
        return "Security-Worker"
    elif occupation.strip() in ["Craft-repair", "Machine-op-inspct", "Transport-moving"]:
        return "Machinery-Worker"
    elif occupation.strip() in ["Farming-fishing", "Handlers-cleaners", "Priv-house-serv"]:
        return "Manual-Worker"
    elif occupation.strip() == "Other-service":
        return "Other-Service"
    

def summarize_workclass(workclass: str) -> str:
    if workclass.strip() in ["Federal-gov", "Local-gov", "State-gov"]:
        return "GOV"
    elif workclass.strip() in ["Private", "Self-emp-inc", "Self-emp-not-inc"]:
        return "PRIVATE"
    else:
        return "UNPAID"