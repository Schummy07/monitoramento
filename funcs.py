import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 
import geopandas as gps
import numpy as np 

def mapa_analitico(variavel, data_ini, data_fin, turno, dia_semana):
    # coreção da variável para se ajustar ao projeto 
    #variavel = variavel[0]
    
    #importação dos dados
    url = "https://raw.githubusercontent.com/Schummy07/monitoramento/main/dados.csv"
    dados = pd.read_csv(url)
    dados["data"] = pd.to_datetime(dados["data"])
    url_mapa = "https://raw.githubusercontent.com/Schummy07/monitoramento/refs/heads/main/mapa_atual.geojson"
    mapa = gps.read_file(url_mapa)
    
    data_ini = pd.to_datetime(data_ini)
    data_fin = pd.to_datetime(data_fin)
    
    #aplicação dos filtros 
    dados_analise = dados[(dados["data"]>= data_ini) &
                          (dados["data"]<= data_fin) &
                          (dados["turno"].isin(turno)) &
                          (dados["dia_semana"].isin(dia_semana))]
    
    #calculo das médias da variável selecionada para cada setor 
    medias = dados_analise.groupby(by = ["data" ,"setor"], as_index = False)[variavel].sum()
    medias = medias.groupby("setor", as_index = False)[variavel].mean()
    medias["setor"] = [f"0{i}" if i <10 else f"{i}" for i in medias["setor"]]
    
    #aplicação do filtro no arquivo shp 
    mapa_filtro = mapa[mapa["SETOR"].isin(medias["setor"])]
    mapa_plot = mapa_filtro.__geo_interface__
    
    # return mapa_filtro, medias - linha de teste 
    # plot do gráfico georeferenciado 
    fig = px.choropleth_map(
        medias,
        geojson=mapa_plot,
        locations="setor",
        featureidkey="properties.SETOR",
        color= variavel,
        color_continuous_scale="Oranges",
        center = {"lat": -22.39, "lon": -47.577}, 
        zoom = 11, 
        opacity = 0.5)
    
    fig.update_layout(
        margin=dict(l=8, r=0, t=0, b=0), 
        width = 900, 
        height = 900)
    
    return fig
    
    
def serie_historica(variavel, data_ini, data_fin, turno, dia_semana):
    data = pd.read_csv("https://raw.githubusercontent.com/Schummy07/monitoramento/main/dados.csv")
    data["data"] = pd.to_datetime(data["data"])
    
    data_ini = pd.to_datetime(data_ini)
    data_fin = pd.to_datetime(data_fin)
    
    data_filtro = data[(data["data"] >= data_ini) & (data["data"]<= data_fin)]
    data_grafico = data_filtro[(data_filtro["turno"].isin(turno)) & (data_filtro["dia_semana"].isin(dia_semana))]
    data_grafico = data_grafico.groupby(by = ["data", "setor"], as_index = False)[variavel].sum()
    
    figura = px.line(data_grafico, x = "data", y = variavel, color = "setor")
    
    return figura


def medias(variavel, data_ini, data_fin, turno, dia_semana):
    data = pd.read_csv("https://raw.githubusercontent.com/Schummy07/monitoramento/main/dados.csv")
    data["data"] = pd.to_datetime(data["data"])
    
    data_ini = pd.to_datetime(data_ini)
    data_fin = pd.to_datetime(data_fin)
    
    data_filtro = data[(data["data"] >= data_ini) & (data["data"]<= data_fin)]
    data_grafico = data_filtro[(data_filtro["turno"].isin(turno)) & (data_filtro["dia_semana"].isin(dia_semana))]
    
    data_grafico = data_grafico.groupby(by = ["data", "setor", "dia_semana"], as_index = False)[variavel].sum()
    data_grafico = data_grafico.groupby( by = ["setor", "dia_semana"], as_index = False)[variavel].mean()
    
    figura = px.bar(data_grafico, x = variavel, y = "setor", color = "dia_semana", orientation = "h")
    figura.update_layout(barmode = "group")
    
    return figura


def correl(variavel1, variavel2, data_ini, data_fin, dia_semana, turno, setor):
    dados = pd.read_csv("https://raw.githubusercontent.com/Schummy07/monitoramento/main/dados.csv")
    dados["data"] = pd.to_datetime(dados["data"])
    
    data_ini = pd.to_datetime(data_ini)
    data_fin = pd.to_datetime(data_fin)
    
    dados_filtro = dados[(dados["data"] >= data_ini) 
                   & (dados["data"]<= data_fin) 
                   & (dados["dia_semana"].isin(dia_semana))
                   & (dados["turno"].isin(turno))
                   & (dados["setor"].isin(setor))]
    
    dados_grafico = dados_filtro.groupby(by = ["data", "setor"], as_index = False).aggregate(x = (variavel1,"sum"),
                                                                                             y = (variavel2, "sum"))
    
    x = dados_grafico["x"]
    y = dados_grafico["y"]
    coefs = np.polyfit(x, y, 1)
    pred = coefs[0]*x + coefs[1]
    
    figura = go.Figure()
    figura.add_trace(go.Scatter(x = x, y = y, mode = "markers", name = "Observações"))
    figura.add_trace(go.Scatter(x = x, y = pred, mode = "lines", name = "Regressão"))
    
    R = round(np.corrcoef(x, y)[0][1],2)
    figura.add_annotation(xref = "paper",
                          yref = "paper",
                          x = 0.9,
                          y = 0.9,
                          text = f" y = {round(coefs[0],2)}x + {round(coefs[1],2)}<br> R = {R}")
    
    return figura
    
    
def histograma(variavel1, variavel2, data_ini, data_fin, dia_semana, turno, setor):
    dados = pd.read_csv("https://raw.githubusercontent.com/Schummy07/monitoramento/main/dados.csv")
    dados["data"] = pd.to_datetime(dados["data"])
    
    data_ini = pd.to_datetime(data_ini)
    data_fin = pd.to_datetime(data_fin)
    
    dados_filtro = dados[(dados["data"] >= data_ini) 
                   & (dados["data"]<= data_fin) 
                   & (dados["dia_semana"].isin(dia_semana))
                   & (dados["turno"].isin(turno))
                   & (dados["setor"].isin(setor))]
    
    dados_grafico = dados_filtro.groupby(by = ["data", "setor"], as_index = False).aggregate(x = (variavel1,"sum"),
                                                                                             y = (variavel2, "sum"))
    
    x = dados_grafico["x"]
    y = dados_grafico["y"]
    coefs = np.polyfit(x, y, 1)
    pred = coefs[0]*x + coefs[1]
    residuo = np.abs(dados_grafico["y"] - pred)
    
    figura = go.Figure()
    figura.add_trace(go.Histogram(x = residuo, name = "Residuo"))
    
    
    return figura