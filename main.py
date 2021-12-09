from macquisition import acquisition as ac
from mwrangling import wrangling as wr
from manalysis import analysis as an

variable_agg = input('Introduce la variable que quieres agregar:   ')

# DATA PIPELINE
if __name__ == "__main__":
    imported_df = ac.acquisition('../datasets/vehicles.csv')
#imported_df = pd.read_csv('../datasets/vehicles.csv')
    wrangled_df = wr.wrangling(imported_df, [1999,1985], 'year')
#wrangled_df = pd.??????
    analysed_df = an.analysis(wrangled_df, 'year', variable_agg)
    print(analysed_df)
    print('OK')

