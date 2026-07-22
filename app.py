import funcs as fc
import dash
from dash import html
from dash import dcc
from dash import Input
from dash import Output

app = dash.Dash(__name__)

app.layout = html.Div([
    
    #bloco do título, fixado acima da página 
    html.Div([html.H1("Painel Analítico: Rio Claro - SP")],
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
    html.Div([html.H1("Filtros"),
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
                      "justifyContent": "center",
                      "flexDirection": "column",
                      "width": "60%", 
                      "marginTop": "70px"}),
    
    # bloco que plota o mapa de calor e as séries históricas 
    html.Div([
        html.Div([html.H2("Mapa de Calor", style = {"marginLeft": "20px"}),
                  html.Div([dcc.Graph(id = "mapa")])],
                 style = {"display":"flex",
                          "flexDirection":"column",
                          "alignItems":"center",
                          "width":"35%",
                          "flex": "1 1 500px",
                          "minWidth": "300px",
                          "maxWidth":"100%",
                          "backgroundColor": "#9feaa8",
                          "border":"5px solid black",
                          "borderRadius": "10px",
                          "height": "700px"}),
        html.Div([html.H1("Série Histórica", style = {"marginLeft": "20px"}),
                  html.Div([dcc.Graph(id = "grafico1", style = {"width": "90%", "height":"300px"}),
                            dcc.Graph(id = "grafico2", style = {"width": "90%", "height":"300px"})], 
                           style = {"display":"flex",
                                    "alignItems": "center",
                                    "flexDirection": "column", 
                                    "gap": "20px",})],
                 style = {"border":"5px solid black",
                          "borderRadius": "10px",
                          "backgroundColor": "#9feaa8",
                          "width": "60%",
                          "alignItems": "center",
                          "height":"700px"})],
             style = {"display":"flex",
                      "flexDirection":"column",
                      "alignItems":"center",
                      "gap": "30px",
                      "width":"98%",
                      "marginTop":"30px",
                      "marginBottom": "30px"}),
    
    # bloco que contém o gráfico de correlação com o histograma dos resíduos 
    # possuí um filtro próprio  
    html.Div([html.H1("Correlação", style = {"marginLeft": "20px"}),
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
                          "flexDirection": "column", 
                          "justifyContent": "center", 
                          "width": "60%"}),
        html.Div([dcc.Graph(id = "correlacao", style = {"width": "65%"}), dcc.Graph(id = "histograma", style = {"width": "30%"})],
                 style = {"display": "flex",
                          "flexDirection": "row",
                          "justifyContent": "center",
                          "gap" : "20px" ,
                          "width": "100%",
                          "marginBottom": "30px",
                          "marginTop": "15px"})],
             style = {"display": "flex", 
                      "flexDirection": "column", 
                    # "justifyContent": "center",
                      "backgroundColor": "#9feaa8",
                      "width": "90%", 
                      "alignItems": "center",
                      "border":"5px solid black",
                      "borderRadius": "10px",
                      "flexWrap": "wrap"})
], 
                      style={"display": "flex",
                             "flexWrap": "wrap",
                             "flexDirection": "column",
                             "alignItems": "center",
                             "margin": "0",
                             "padding": "0",
                             "backgroundColor": "#26ce34"})


def gerar_mapa(variavel, data_ini, data_fin, turno, dia_semana):
    return fc.mapa_analitico(variavel, data_ini, data_fin, turno, dia_semana)

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
             Input("Frequencia", "value"))(gerar_mapa)

app.callback(Output("grafico1", "figure"),
             Input("Parametro_Operacional", "value"),
             Input("filtro_data", "start_date"),
             Input("filtro_data", "end_date"),
             Input("Turno", "value"),
             Input("Frequencia", "value"))(gerar_grafico1)

app.callback(Output("grafico2", "figure"),
             Input("Parametro_Operacional", "value"),
             Input("filtro_data", "start_date"),
             Input("filtro_data", "end_date"),
             Input("Turno", "value"),
             Input("Frequencia", "value"))(gerar_grafico2)

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