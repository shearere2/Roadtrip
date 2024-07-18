import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

def read_shapefile(sf):
    """
    Read a shapefile into a Pandas dataframe with a 'coords' 
    column holding the geometry information. This uses the pyshp
    package
    """
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df

if __name__ == '__main__':
    sns.set(style='whitegrid', palette='pastel', color_codes=True)
    sns.mpl.rc('figure', figsize=(10,6))
    sf = shp.Reader('data/tl_2019_us_county.shp')
    print()