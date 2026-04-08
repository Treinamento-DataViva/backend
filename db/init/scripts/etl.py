import extract 
import transform 
import load    

df = extract.extract_data()
df_tratado = transform.transform_data(df)
load.load_data(df_tratado)
load.load_lookup_table()
