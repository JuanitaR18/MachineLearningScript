import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from Capture import CapturaDatos


class PrepareData:

    def __init__(self):
        self.listReturned = CapturaDatos()
        self.listData = []

    def prepareJson(self):
        self.listReturned.Captura()
        self.listData = self.listReturned.limpieza()

    def pandasDataPrepared(self):
        #Depende de la estructura de datos
        df = pd.DataFrame(self.listData,columns=['Year','Quarter','Provider','Income','amountSMS'])
        df['Year'] = pd.to_datetime(df['Year'])
        df['Quarter'] = df['Quarter'].astype('category').cat.codes
        df['Provider'] = df['Provider'].astype('category').cat.codes

        x = df[['Year','Quarter','Provider','amountSMS']]
        y = df['Income']

        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
        model = LinearRegression()
        model.fit(x_train,y_train)

        y_pred = model.predict(x_test)

        mse = mean_squared_error(y_test,y_pred)
        r2 = r2_score(y_test,y_pred)

        print(f"Mean error: {mse}")
        print(f"R-squared error: {r2}")

        plt.scatter(y_test,y_pred)
        plt.xlabel("% real income")
        plt.ylabel("income prediction")
        plt.title("Regresion: Incomes")
        plt.show()


prueba = PrepareData()
prueba.prepareJson()
prueba.pandasDataPrepared()


