import pandas as pd
from sklearn.model_selection import train_test_split

#main data
app_train = pd.read_csv("application_train.csv")

#to be joined
# bur_bal = pd.read_csv("bureau_balance.csv")
# bur = pd.read_csv("bureau.csv")
# credit_bal = pd.read_csv("credit_card_balance.csv")
# home_desc = pd.read_csv("HomeCredit_columns_description.csv")
# install_pmt = pd.read_csv("installments_payments.csv")


# merged_train = app_train.merge(bur, how="left", on="SK_ID_CURR")
# merged_test = merged_train.merge(bur_bal, on="SK_ID_BUREAU", how="left")
# print(merged_train.shape)

#need to do test train split for test dataset
train ,test = train_test_split(app_train, test_size=0.3)
print(train.shape, test.shape)
