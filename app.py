import funcs as fc
import dash
from dash import html
from dash import dcc
from dash import Input
from dash import Output
from dash import State

app = dash.Dash(__name__)

app.layout = html.Div([
    
    #bloco do título, fixado acima da página 
    html.Div([html.H1("Painel analitico: Rio Claro - SP")],
             style = {"position": "fixed",
                      "display": "flex",
                      "zIndex": "9999",
                      "backgroundColor": "#27672F",
                      "top": "0",
                      "width": "100%",
                      "justifyContent": "center",
                      "marginLeft": "13px",
                      "marginRight": "13px"}),
    
    # bloco dos filtros aplicáveis, filtram os dados do mapa de calor e da série histórica 
    html.Div([
        dcc.Store(id = "variavel_store"),
        dcc.Store(id = "min_store"),
        dcc.Store(id = "max_store"),
        html.H2("Mapa de Calor"),
        html.Div([
                  dcc.Dropdown(id = "Parametro_Operacional", 
                               options = [{"label": "Tonelagem", "value": "producao"},
                                          {"label": "Tempo_Coleta", "value": "horas_coleta"},
                                          {"label": "Tamanho: km percorrido em coleta", "value": "km_coleta"}, 
                                          {"label": "Produtividade: ton/h", "value": "ton/h"},
                                          {"label": "Densidade: ton/km", "value": "ton/km"}],
                               value = "producao",
                               multi = False),
                  dcc.DatePickerRange(id = "filtro_data",
                                      start_date = "2025-05-20",
                                      end_date = "2025-06-20"),
                  dcc.Dropdown(id = "Turno",
                               options = [{"label": "Noturno", "value": "NOTURNO"},
                                          {"label": "Diurno", "value": "DIURNO"}],
                               value = ["DIURNO", "NOTURNO"],
                               multi = True), 
                  dcc.Dropdown(id = "Frequencia",
                               options = [{"label":"Segunda", "value": "seg"},
                                          {"label":"Terca", "value": "ter"},
                                          {"label":"Quarta", "value": "qua"},
                                          {"label":"Quinta", "value": "qui"},
                                          {"label":"Sexta", "value": "sex"},
                                          {"label":"Sabado", "value": "sáb"}],
                               value = ["seg","ter","qua","qui","sex","sáb","dom"],
                               multi = True)],
                 style = {"display":"flex",
                          "flexDirection":"row",
                          "justifyContent":"center",
                          "height":"10%",
                          "gap": "2px"}),
        html.Div([
            html.Div([
                html.Div(id = "congelar"),
                html.Div([
                    html.Button("Congelar", id = "freeze",
                                style = {"width":"20%", "height":"5%"}),
                    dcc.Graph(id = "mapa",
                              style = {"height":"95%", "width":"100%"})],
                         style = {"width":"42%",
                                  "height":"100%",
                                  "display":"flex",
                                  "flexDirection": "column",
                                  "alignItems":"center"})],
                     style = {"display":"flex",
                              "flexDirection":"row",
                              "alignItems":"center",
                              "justifyContent":"center",
                              "height":"75%",
                              "width":"100%",
                              "gap":"10px",
                              "marginBottom":"10px"})],
                 style = {"display":"flex",
                          "flexDirection":"row",
                          "alignItems":"center",
                          "justifyContent":"center",
                          "height":"100%",
                          "width":"100%",
                          "backgroundColor": "#9feaa8"})], 
             
             style = {"display":"flex",
                      "flexDirection":"column",
                      "alignItems":"center",
                      "justifyContent":"center",
                      "height":"90vh",
                      "width": "90%",
                      "marginTop": "80px",
                      "backgroundColor": "#9feaa8",
                      "border":"3px solid black",
                      "borderRadius": "15px"}),
    
    # bloco que plota o mapa de calor e as séries históricas 
    html.Div([
        html.Div([html.H2("Série Histórica"),
                  html.Div([
                      dcc.Dropdown(id = "Parametro_Operacional_g",
                                   options = [{"label": "Tonelagem", "value": "producao"},
                                              {"label": "Tempo_Coleta", "value": "horas_coleta"},
                                              {"label": "Tamanho: km percorrido em coleta", "value": "km_coleta"}, 
                                              {"label": "Produtividade: ton/h", "value": "ton/h"},
                                              {"label": "Densidade: ton/km", "value": "ton/km"}],
                                   value = "producao",
                                   multi = False),
                      dcc.DatePickerRange(id = "filtro_data_g",
                                          start_date = "2025-05-20",
                                          end_date = "2025-06-20"),
                      dcc.Dropdown(id = "Turno_g",
                                   options = [{"label": "Noturno", "value": "NOTURNO"},
                                              {"label": "Diurno", "value": "DIURNO"}],
                                   value = ["DIURNO", "NOTURNO"],
                                   multi = True),
                      dcc.Dropdown(id = "Frequencia_g",
                                   options = [{"label":"Segunda", "value": "seg"},
                                              {"label":"Terca", "value": "ter"},
                                              {"label":"Quarta", "value": "qua"},
                                              {"label":"Quinta", "value": "qui"},
                                              {"label":"Sexta", "value": "sex"},
                                              {"label":"Sabado", "value": "sáb"}],
                                   value = ["seg","ter","qua","qui","sex","sáb","dom"],
                                   multi = True)],
                           style = {"display":"flex",
                                    "flexDirection":"row",
                                    "justifyContent":"center",
                                    "height":"10%",
                                    "gap":"2px",
                                    "width":"80%"}),
                  html.Div([
                      html.Div([dcc.Graph(id = "grafico1",
                                          style = {"height":"100%", "width":"100%"})],
                               style = {"height":"48%",
                                        "width":"100%"}),
                      html.Div([dcc.Graph(id = "grafico2",
                                          style = {"height":"100%", "width":"100%"})],
                               style = {"height":"48%",
                                        "width":"100%"})], 
                           style = {"display":"flex",
                                    "flexDirection":"column",
                                    "height":"65%",
                                    "width":"90%",
                                    "gap":"5px"})],
                 style = {"display":"flex",
                          "flexDirection":"column",
                          "alignItems":"center",
                          "justifyContent":"center",
                          "height":"100%",
                          "width":"100%",
                          "gap":"5px"})],
             
             style = {"display":"flex",
                      "flexDirection":"column",
                      "height":"90vh",
                      "width":"90%",
                      "justifyContent":"center",
                      "alignItems":"center",
                      "border":"3px solid black",
                      "backgroundColor": "#9feaa8",
                      "borderRadius": "15px"}),
    
    # bloco que contém o gráfico de correlação com o histograma dos resíduos 
    # possuí um filtro próprio  
    html.Div([html.H2("Correlação"),
        html.Div([dcc.Dropdown(id = "variavel 1",
                               options = [{"label":"Tamanho_setor", "value": "km_coleta"},
                                           {"label": "Deslocamento", "value": "km_trajeto"},
                                           {"label": "Tonelagem", "value": "producao_ton"},
                                           {"label": "Produtividade: ton/h", "value": "ton/h"},
                                           {"label": "Densidade: ton/km", "value": "ton/km"}],
                               value = "producao_ton"),
                  dcc.Dropdown(id = "variavel 2",
                               options = [{"label":"Tamanho_setor", "value": "km_coleta"},
                                           {"label": "Deslocamento", "value": "km_trajeto"},
                                           {"label": "Tonelagem", "value": "producao_ton"},
                                           {"label": "Produtividade: ton/h", "value": "ton/h"},
                                           {"label": "Densidade: ton/km", "value": "ton/km"}],
                               value = "ton/h"),
                  dcc.DatePickerRange(id = "filtro_data_1",
                                      start_date = "2025-05-20",
                                      end_date = "2025-06-20"),
                  dcc.Dropdown(id = "Frequencia_1", 
                               options = [{"label":"Segunda", "value": "seg"},
                                          {"label":"Terca", "value": "ter"},
                                          {"label":"Quarta", "value": "qua"},
                                          {"label":"Quinta", "value": "qui"},
                                          {"label":"Sexta", "value": "sex"},
                                          {"label":"Sabado", "value": "sáb"}],
                               value = ["seg"],
                               multi = True),
                  dcc.Dropdown(id = "Turno_1", 
                               options = [{"label":"Noturno", "value":"NOTURNO"},
                                           {"label": "Diurno", "value": "DIURNO"}],
                               value = ["DIURNO","NOTURNO"], 
                               multi = True),
                  dcc.Dropdown(id = "Setor",
                               options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],
                               value = [9,18,16,14,13,20],
                               multi = True)], 
                 style = {"display": "flex", 
                          "flexDirection": "row", 
                          "justifyContent": "center",
                          "width": "80%",
                          "height":"10%",
                          "gap":"2px"}),
        html.Div([dcc.Graph(id = "correlacao", style = {"width": "65%", "height":"100%"}), 
                  dcc.Graph(id = "histograma", style = {"width": "30%", "height":"100%"})],
                 style = {"display": "flex",
                          "flexDirection": "row",
                          "margin":"20px",
                          "justifyContent":"center",
                          "gap" : "20px" ,
                          "width": "100%",
                          "height":"55%"})],
             style = {"display": "flex", 
                      "flexDirection": "column",
                      "backgroundColor": "#9feaa8",
                      "alignItems": "center",
                      "justifyContent":"center",
                      "border":"3px solid black",
                      "borderRadius": "10px",
                      "height":"75vh",
                      "width":"90%"})
], 
                      style={"display": "flex",
                             "flexDirection": "column",
                             "alignItems": "center",
                             "justifyContent":"center",
                             "gap":"15px",
                             "backgroundColor": "#26ce34"})


def gerar_mapa(variavel, data_ini, data_fin, turno, dia_semana,var_guard ,minimo, maximo):
    if var_guard == variavel:
        return fc.mapa_analitico(variavel, data_ini, data_fin, turno, dia_semana, minimo, maximo)
    else:
        return fc.mapa_analitico(variavel, data_ini, data_fin, turno, dia_semana, None, None)

def guardar_vars(n_clicks, variavel, data_ini, data_fin, turno, dia_semana):
    if not n_clicks:
        return dash.no_update
    resposta = fc.filtro_guardar(variavel, data_ini, data_fin, turno, dia_semana)
    var = resposta[0]
    min = resposta[1]
    max = resposta[2]
    return var, min, max

def congelar_mapa(n_clicks, variavel, data_ini, data_fin, turno, dia_semana):
    if not n_clicks:
        return dash.no_update
    
    lista = []
    grafico = fc.mapa_analitico(variavel, data_ini, data_fin, turno, dia_semana, None, None)
    
    var = str(variavel)
    data_in = str(data_ini)
    data_fi = str(data_fin)
    
    lista.append(
        html.Div([f"{var} / {data_in}_{data_fi}"],
                 style = {"height":"5%",
                          "fontWeight": "bold"}))
    
    lista.append(
        dcc.Graph(figure = grafico,
                  style = {"height":"95%","width":"100%"}))
    
    estilo = {"width":"42%",
              "height":"100%",
              "display":"flex",
              "flexDirection": "column",
              "alignItems":"center"}
    
    return lista, estilo
        

def gerar_grafico1(variavel, data_ini, data_fin, turno, dia_semana):
    return fc.serie_historica(variavel, data_ini, data_fin, turno, dia_semana)

def gerar_grafico2(variavel, data_ini, data_fin, turno, dia_semana):
    return fc.medias(variavel, data_ini, data_fin, turno, dia_semana)

def gerar_correlacao(variavel1, variavel2, data_ini, data_fin, dia_semana, turno, setor):
    return fc.correl(variavel1, variavel2, data_ini, data_fin, dia_semana, turno, setor)

def gerar_histograma(variavel1, variavel2, data_ini, data_fin, dia_semana, turno, setor):
    return fc.histograma(variavel1, variavel2, data_ini, data_fin, dia_semana, turno, setor)

app.callback(Output("mapa", "figure"),
             Input("Parametro_Operacional", "value"),
             Input("filtro_data", "start_date"),
             Input("filtro_data", "end_date"),
             Input("Turno", "value"),
             Input("Frequencia", "value"),
             Input("variavel_store","data"),
             Input("min_store", "data"),
             Input("max_store", "data"))(gerar_mapa)

app.callback(Output("variavel_store","data"),
             Output("min_store", "data"),
             Output("max_store", "data"),
             Input("freeze", "n_clicks"),
             State("Parametro_Operacional", "value"),
             State("filtro_data", "start_date"),
             State("filtro_data", "end_date"),
             State("Turno", "value"),
             State("Frequencia", "value"))(guardar_vars)

app.callback(Output("congelar", "children"),
             Output("congelar", "style"),
             Input("freeze", "n_clicks"),
             State("Parametro_Operacional", "value"),
             State("filtro_data", "start_date"),
             State("filtro_data", "end_date"),
             State("Turno", "value"),
             State("Frequencia", "value"))(congelar_mapa)

app.callback(Output("grafico1", "figure"),
             Input("Parametro_Operacional_g", "value"),
             Input("filtro_data_g", "start_date"),
             Input("filtro_data_g", "end_date"),
             Input("Turno_g", "value"),
             Input("Frequencia_g", "value"))(gerar_grafico1)

app.callback(Output("grafico2", "figure"),
             Input("Parametro_Operacional_g", "value"),
             Input("filtro_data_g", "start_date"),
             Input("filtro_data_g", "end_date"),
             Input("Turno_g", "value"),
             Input("Frequencia_g", "value"))(gerar_grafico2)

app.callback(Output("correlacao", "figure"),
             Input("variavel 1", "value"),
             Input("variavel 2", "value"),
             Input("filtro_data_1", "start_date"),
             Input("filtro_data_1", "end_date"),
             Input("Frequencia_1", "value"),
             Input("Turno_1", "value"),
             Input("Setor", "value"),)(gerar_correlacao)

app.callback(Output("histograma", "figure"),
             Input("variavel 1", "value"),
             Input("variavel 2", "value"),
             Input("filtro_data_1", "start_date"),
             Input("filtro_data_1", "end_date"),
             Input("Frequencia_1", "value"),
             Input("Turno_1", "value"),
             Input("Setor", "value"),)(gerar_histograma)

server = app.server 

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8050, debug = True)