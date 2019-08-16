import datawig
import sklearn
import pandas as pd
from sklearn.metrics import r2_score as score
from sklearn.metrics import classification_report as cr

df = pd.read_csv('normalised_data.csv')
df = df.fillna(0)

df_train, df_test = datawig.utils.random_split(df, split_ratios=[0.8, 0.2])

imputer = datawig.SimpleImputer(
    input_columns = ['CH4', 'CO2','NH4','NO3','Prec_mm','tmax','tmin','Fert_Rate','Air_Temp','DAF'],
    output_column = 'N2O',
    output_path = 'imputer_model'
)

imputer.fit(train_df=df_train, num_epochs = 100)

imputed = imputer.predict(df_test)

new_dataframe = pd.DataFrame(data = imputed)

new_dataframe.to_csv('N2O_data.csv')

f1 = score(imputed['N2O'], imputed['N2O_imputed'])
print('N2O f2_score: ', f1)

# N2O f2_score:  0.2208990261287076 'Fert_Rate', 'Air_Temp', 'CH4', 'CO2', 'DAF','NH4','NO3','Prec_mm','Soil_Temp','tmax','tmin'
# N2O f2_score:  0.09467224566969124 'CH4', 'CO2','NH4','NO3','Prec_mm','tmax','tmin'
# N2O f2_score:  0.19837632947774686 'CH4', 'CO2','NH4','NO3','Prec_mm','tmax','tmin','Fert_Rate','Air_Temp','DAF'
