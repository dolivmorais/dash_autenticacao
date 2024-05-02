from dash import dcc, Dash, html, Output, Input
import dash_auth

app = Dash(__name__)

opcoes_dropdown =[
    {"label": "Dia 1", "value": "Dia 1"},
    {"label": "Dia 2", "value": "Dia 2"}
    ]

app.layout = html.Div([
    html.H1("Meu Dashbord"),
    dcc.Dropdown(id="dropdown",options=opcoes_dropdown, value="Dia 1"),
    dcc.Graph(id="grafico")
])

@app.callback(Output("grafico","figure"),Input("dropdown","value"))
def atualizar_grafico(valor_dropdown):
    if valor_dropdown == "Dia 1":
        pontos = {"x":[1,2,3,4], "y":[4,5,6,7]}
        titulo = "Grafico Dia 1"
    else:
        pontos = {"x":[1,2,3,4], "y":[2,1,3,2]}
        titulo = "Grafico Dia 2"
    return {"layout": {"title": titulo},"data":[pontos]}


app.run_server(debug=True)