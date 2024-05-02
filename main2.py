import dash
import dash_core_components as dcc
import dash_html_components as html

# Inicialize o aplicativo Dash
app = dash.Dash(__name__)

# Layout do aplicativo
app.layout = html.Div([
    html.H1('Meu Primeiro Aplicativo Dash'),
    html.P("Este é um exemplo simples de um aplicativo Dash.")
])

# Iniciar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
