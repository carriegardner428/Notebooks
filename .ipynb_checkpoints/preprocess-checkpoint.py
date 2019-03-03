def handle_missing_data(df, drop=True, impute=False):
    if drop:
        return df.dropna()
    # add impute instructions
    
def relabel_data(df):
    df['x41'] = pd.to_numeric(df.x41.str.replace('$', ''))
    df['x45'] = pd.to_numeric(df.x45.str.replace('%', ''))
    df['x34'] = df.x34.str.lower()
    df['x35'] = df.x35.str.replace('wed', 'wednesday')
    df['x35'] = df.x35.str.replace('thur', 'thursday')
    df['x35'] = df.x35.str.replace('fri', 'friday')
    df['x68'] = df.x68.str.lower()
    df['x68'] = df.x68.str.replace('jun', 'june')
    df['x68'] = df.x68.str.replace('aug', 'august')
    df['x68'] = df.x68.str.replace('sept.', 'september')
    df['x68'] = df.x68.str.replace('apr', 'april')
    df['x68'] = df.x68.str.replace('oct', 'october')
    df['x68'] = df.x68.str.replace('mar', 'march')
    df['x68'] = df.x68.str.replace('nov', 'november')
    df['x68'] = df.x68.str.replace('feb', 'february')
    df['x68'] = df.x68.str.replace('dev', 'december') # guessing dev = december
    df['x93'] = df.x93.str.replace('euorpe', 'europe')
    return df

def encode_categoricals(objects, prefix=['cars', 'day', 'month', 'market']):
    objects = pd.get_dummies(objects, prefix, dummy_na=True)
    return objects