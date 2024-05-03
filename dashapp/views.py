from dash import dcc, Dash, html, Output, Input
from dashapp import app, server

opcoes_dropdown =[
    {"label": "Dia 1", "value": "Dia 1"},
    {"label": "Dia 2", "value": "Dia 2"}
    ]

layot_homepage = html.Div([
    html.H2("HomePage")
])

layot_login = html.Div([
    html.H2("Faça seu login")
])


layout_dashboard =  html.Div([
    html.H2("Meu Dashbord"),
    dcc.Dropdown(id="dropdown",options=opcoes_dropdown, value="Dia 1"),
    dcc.Graph(id="grafico")
    ])

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.H1("Dashapp"),
    html.Div(id="conteudo_pagina")
])

@app.callback(Output("conteudo da pagina", "children"), Input("url", "pathname"))
def carregar_pagina(pathname):
    if pathname == "/":
        return layot_homepage
    elif pathname == "/dashboard":
        return layout_dashboard
    elif pathname == "/logiin":
        return layot_login


@app.callback(Output("grafico","figure"),Input("dropdown","value"))
def atualizar_grafico(valor_dropdown):
    if valor_dropdown == "Dia 1":
        pontos = {"x":[1,2,3,4], "y":[4,5,6,7]}
        titulo = "Grafico Dia 1"
    else:
        pontos = {"x":[1,2,3,4], "y":[2,1,3,2]}
        titulo = "Grafico Dia 2"
    return {"layout": {"title": titulo},"data":[pontos]}

@server.route("/nova_tela")
def nova_tela():
    return "tela do flask"
