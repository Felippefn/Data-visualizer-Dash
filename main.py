import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_auth
import dash_table
import pandas as pd
import numpy as np
import operator
import glob
import os.path
import plotly.graph_objs as go
import plotly.express as px
from plotly import graph_objects as go
from dash.dependencies import Input, Output, State
from collections import Counter


max_file = 'NPS pesquisa.xlsx'
# file_type = '\*.xlsx'
# files = glob.glob(folder_path + file_type)
# max_file = max(files, key=os.path.getctime)


def nps_calculate(list_):
    detractor = []
    neutral = []
    promoter = []

    for item in list_:
        if item < 7:
            detractor.append(item)
        elif item > 8:
            promoter.append(item)
        else:
            neutral.append(item)

    total = detractor + promoter + neutral
    nps = ((len(promoter)/len(total))*100) - \
        ((len(detractor)/len(total))*100)
    if nps >= 0:
        nps = nps + 0.45
    else:
        nps = nps - 0.45
    return nps


def csat_(list_):
    note_5 = []
    note_4 = []
    note_3 = []
    note_2 = []
    note_1 = []

    for item in list_:
        if item == "Nota 5 - Muito satisfeito":
            note_5.append(item)
        elif item == "Nota 4 - Satisfeito":
            note_4.append(item)
        elif item == "Nota 3 - Neutro":
            note_3.append(item)
        elif item == "Nota 2 - Insatisfeito":
            note_2.append(item)
        elif item == "Nota 1 - Muito insatisfeito":
            note_1.append(item)
    total = note_1 + note_2 + note_3 + note_4 + note_5
    csat = ((len(note_5) + len(note_4)) / len(total))*100
    return csat


def feeling_rate(list_, typo):
    positive = []
    negative = []
    sugestion = []

    for item in list_:
        if item == "Positivo":
            positive.append(item)
        elif item == "Negativo":
            negative.append(item)
        elif item == "Sugestão":
            sugestion.append(item)

    total = positive + negative + sugestion

    p = ((len(positive) / len(total)) * 100)
    n = ((len(negative) / len(total)) * 100)
    s = ((len(sugestion) / len(total)) * 100)
    p = int(p)
    n = int(n)
    s = int(s)
    
    if typo == "positivo":

        return p

    elif typo == "negativo":

        return n

    else:

        return s


def type_user_nps(list_, typo):
    promoter = []
    neutral = []
    detractor = []

    for item in list_:
        if item == "Promoter":
            promoter.append(item)
        elif item == "Neutral":
            neutral.append(item)
        else:
            detractor.append(item)
    total = promoter + neutral + detractor
    promoter_ = ((len(promoter) / len(total)) * 100)
    neutral_ = ((len(neutral) / len(total)) * 100)
    detractor_ = ((len(detractor) / len(total)) * 100)
    format_promoter = "{:.2f}".format(promoter_)
    format_neutral = "{:.2f}".format(neutral_)
    format_detractor = "{:.2f}".format(detractor_)
    if typo == "promoter":
        return format_promoter + "%"
    elif typo == "neutral":
        return format_neutral + "%"
    else:
        return format_detractor + "%"


def analytic_classfy(list_, typo):
    dict_list = dict(
        Counter(list_))
    max_value = max(dict_list.items(), key=operator.itemgetter(1))[0]
    list_max = sorted(dict_list.items(), key=lambda x: x[1], reverse=True)

    keys = []
    values = []
    for item in list_max:
        keys.append(item[0]), values.append(item[1])

    if typo == "k":
        return keys
    elif typo == "v":
        return values
    elif typo == "max":
        return max_value
    elif typo == "%":
        return percent
    else:
        return list_max


img_justa = r'C:\Users\Felippe\Pictures\Logos-Justa (2).zip\Download Logo principal\Logo J.png'
nps_pesquisa = (max_file)
df = pd.read_excel(nps_pesquisa, sheet_name="Base Pesquisas")
df['Mês pesquisa'] = df['Mês pesquisa'].astype("Int64")
df['NPS'] = df['NPS'].astype("Int64")
df['ID heroi_Dimension'] = df['ID heroi_Dimension'].astype("Int64")

new_df = df[['Mês pesquisa', 'Ano',  'Name', 'NpsClassification', 'Origin', 'Comment', 'NPS', 'Classificação 1', 'Sentimento', 'Classificação 2', 'Sentimento2',
            'Você já precisou da ajuda da nossa equipe de ajuda alguma vez? Se sim, avalie com uma nota de 1 a 5', 'Ciclo de Vida_Dimension', 'Cidade_Dimension',
             'Data de Aprovação_Dimension', 'Dias sem Transacionar_Dimension', 'Estado_Dimension', 'ID heroi_Dimension', 'MCC_Dimension', 'MCC Descrição_Dimension',
             'Nome Fantasia_Dimension', 'O que você acha do atendimento e acompanhamento do nosso vendedor? Se sim, avalie com uma nota de 1 a 5_Dimension', 'Qual dos nossos benefícios melhor te atende? _Dimension',
            'TPV PROMETIDO_Dimension',
             'TPV TOTAL_Dimension']]

year_2021 = [2021]
one_tt = [1, 2, 3]

two_tt = [4, 5, 6]

three_tt = [7, 8, 9]

four_tt = [10, 11, 12]

one_df = df[df['Mês pesquisa'].isin(one_tt) & df['Ano'].isin(year_2021)]
two_df = df[df['Mês pesquisa'].isin(two_tt) & df['Ano'].isin(year_2021)]
three_df = df[df['Mês pesquisa'].isin(three_tt) & df['Ano'].isin(year_2021)]
four_df = df[df['Mês pesquisa'].isin(four_tt) & df['Ano'].isin(year_2021)]

one_df = one_df['NPS']
two_df = two_df['NPS']
three_df = three_df['NPS']
four_df = four_df['NPS']

list_nps = []
xNps = np.array(df['NPS'])
nps = np.unique(xNps)

list_months = []
xMonths = np.array(df['Mês pesquisa'])
months = np.unique(xMonths)

list_origins = []
list_originsm = []
xOrigins = np.array(df['Origin'])
origins = np.unique(xOrigins)

list_year = []
list_yearm = []
xYear = np.array(df["Ano"])
year = np.unique(xYear)

for i in months:
    list_months.append(i)

for i in nps:
    list_nps.append(i)

for i in origins:
    list_origins.append(i)
    if i == "Email" or i == "Telefone":
        list_originsm.append(i)


for i in year:
    list_year.append(i)
    if i == 2022:
        list_yearm.append(i)

# suppress_callback_exceptions=True) ignore errors
app = dash.Dash(__name__, title='CX NPS', suppress_callback_exceptions=True)
colors = {
    'background': '#001122',  # darkBlue
    'text': '#ffffff',  # white
    'wheat': '#f5deb3',
    'blue': '#1F77B4',
    'yellow': '#ffd500'
}
# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )

tabs_styles = {'vertical-align': 'top'}
tab_style = {
    'borderTop': '1px solid #000000',
    'borderBottom': '1px solid #000000',
    'borderLeft': '1px solid #000000',
    'borderRight': '1px solid #000000',
    'fontWeight': 'bold',
    'textAlign': 'left',
    'backgroundColor': '#f5deb3',
    'color': colors['background']
}
tab_selected_style = {
    'borderTop': '1px solid #f5deb3',
    'borderBottom': '1px solid #f5deb3',
    'borderLeft': '1px solid #f5deb3',
    'borderRight': '1px solid #f5deb3',
    'backgroundColor': colors['background'],
    'color': '#f5deb3',
    'textAlign': 'left',
    'boxShadow': '0 6px 6px 0 #f5deb3, 0 6px 6px 0 black',
}


app.layout = html.Div(style={'backgroundColor': colors['background'], 'height': '100%', 'width': '100%'}, children=[
    html.H1(
        children='Customer Experience',
        className='H1-Text H1-Text-Display'
    ),
    # html.Img(id="logo-justa", src=app.get_asset_url(r'C:\Users\Felippe\Documents\Programming\Justa\Dash_NPS\Logo J.png'), height='40', width='160'),
    html.Div(children=[
        html.Div([
            dcc.Tabs(id="tabs-styled-with-inline", value='tab-0', children=[
                dcc.Tab(id="nps_nbutton", label='NPS', value='tab-1', style=tab_style,
                        selected_style=tab_selected_style),
                dcc.Tab(id="clas_nbutton", label='Classificação', value='tab-2',
                        style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(id="det_nbutton", label='Detalhes', value='tab-3',
                        style=tab_style, selected_style=tab_selected_style),
                # dcc.Tab(id="voc_nbutton", label='VOC', value='tab-4',
                #         style=tab_style, selected_style=tab_selected_style)
            ]),
            html.Div(id='tabs-content-inline')
        ])
    ]),
    html.Div(id='big-div', children=[
        html.Div(id="medium_block", children=[
            html.H1(children="Mês:", style={
                'color': colors['text']
            }, className="mes_text"),
            dcc.Dropdown(id='dropdown-id',
                         options=[
                            {'label': i, 'value': i} for i in list_months],
                         multi=True,
                         value=[min(list_months)],
                         style={'backgroundColor': colors['background'],
                                'color': '#0065CD',
                                'width': '250px'}),
            dcc.Checklist(id="origin-marker",
                          options=[
                              {'label': i, 'value': i} for i in list_origins],
                          value=[i for i in list_originsm]
                          ),
            dcc.Checklist(id="year-marker",
                          options=[
                              {'label': i, 'value': i} for i in list_year],
                          value=[i for i in list_yearm]
                          ),
            html.Div(id="small_block", children=[html.H1(
                children='Respostas:',
                className='answer_text'),
                html.Div(id="number_answer")
            ])])
    ])
]
)


@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div(id="nps_graph_trim", style={'backgroundColor': colors['background']}, children=[
            dcc.Graph(
                id='nps_graph_TRI', style={'width': '52vh', 'height': '58vh'},
                figure={
                        'data': [
                            {'x': ["1ºTrimestre", "2ºTrimestre", "3ºTrimestre", "4ºTrimestre"], 'y': [int(nps_calculate(one_df)), int(nps_calculate(two_df)), int(nps_calculate(three_df)), int(nps_calculate(four_df))],
                                'type': 'bar', 'name': 'Trimestre'}
                        ],
                        'layout': {
                            'title': 'NPS Score Trimestre',
                            'plot_bgcolor': '#06182b',
                            'paper_bgcolor': '#06182b',
                    
                            'font': {
                                'color': colors['text'],
                            },
                            'text':[int(nps_calculate(one_df)), int(nps_calculate(two_df)), int(nps_calculate(three_df)), int(nps_calculate(four_df))],
                            'hovermode':"x",

                            'marker': {'color': '#b1b1ff'}
                        }
                        }  
            ),
            html.Div([
                dcc.Graph(id='nps-indicator'),
                html.Div(id='promoter-indicator'),
                html.Div(id='neutral-indicator'),
                html.Div(id='detractor-indicator')
            ]),
            dcc.Graph(id="csat_ajuda"),
            dcc.Graph(id="csat_comercial"),
            dcc.Graph(id="pie-chart"),
        ])

    elif tab == 'tab-2':
        return html.Div([
            html.Div(id="box-feeling", children=[
                dcc.Graph(id='feeling')
            ]),
            html.Div(id="positive-classification"),
            html.Div(id="negative-classification"),
            html.Div(id="sugestion-classification"),
            dcc.Graph(id="funnel_chart"),
            html.Div(id='positive-class'),
            html.Div(id='sugestion-class'),
            html.Div(id='negative-class')

        ])

    elif tab == 'tab-3':
        return html.Div(id="details-excel", children=[
            dash_table.DataTable(
                id='memory-table',
                style_cell={'textAlign': 'center'},
                style_header={
                    'backgroundColor': 'grey',
                    'color': 'rgb(30, 30, 30)',
                    'fontWeight': 'bold'},
                style_data={
                    'backgroundColor': '#06182b',
                    'color': 'white',
                },
                page_action='none',
                style_table={'height': '630px', 'width': '99vw',
                             'overflowY': 'auto', 'overflowX': 'auto'},
                sort_action="native",
                filter_action="native",
                columns=[{'name': i, 'id': i} for i in new_df.columns]

            )
        ])


@app.callback(
    Output('positive-class', 'children'),
    Output('sugestion-class', 'children'),
    Output('negative-class', 'children'),
    [
        Input('dropdown-id', 'value'),
        Input("origin-marker", "value"),
        Input("year-marker", "value")
    ]
)
def generate_indicator(dropdown_value, check_select, check_year):
    df_filtered = df[df['Mês pesquisa'].isin(dropdown_value) & df['Origin'].isin(
        check_select) & df["Ano"].isin(check_year)]
    akk = ["Positivo", "Negativo", "Sugestão"]
    main_a = df_filtered[df_filtered["Sentimento"].isin(akk)]
    main_b = df_filtered[df_filtered["Sentimento2"].isin(akk)]
    main1 = main_a["Classificação 1"]
    main2 = main_b["Classificação 2"]
    main_t = pd.concat([main1, main2], axis=0)

    positive_a = df_filtered[df_filtered["Sentimento"] == "Positivo"]
    positive_b = df_filtered[df_filtered["Sentimento2"] == "Positivo"]
    positive1 = positive_a["Classificação 1"]
    positive2 = positive_b["Classificação 2"]
    positive = pd.concat([positive1, positive2])

    sugestion_a = df_filtered[df_filtered["Sentimento"] == "Sugestão"]
    sugestion_b = df_filtered[df_filtered["Sentimento2"] == "Sugestão"]
    sugestion1 = sugestion_a["Classificação 1"]
    sugestion2 = sugestion_b["Classificação 2"]
    sugestion = pd.concat([sugestion1, sugestion2])

    negative_a = df_filtered[df_filtered["Sentimento"] == "Negativo"]
    negative_b = df_filtered[df_filtered["Sentimento2"] == "Negativo"]
    negative1 = negative_a["Classificação 1"]
    negative2 = negative_b["Classificação 2"]
    negative = pd.concat([negative1, negative2])

    pos = analytic_classfy(positive, "k")[0]
    sug = analytic_classfy(sugestion, "k")[0]
    neg = analytic_classfy(negative, "k")[0]

    pos_v = analytic_classfy(positive, "v")[0]
    pos_t = analytic_classfy(positive, "v")
    pos_t = sum(pos_t)
    pois = (pos_v / pos_t) * 100
    format_pos = "{:.2f}".format(pois) + "%"

    neg_v = analytic_classfy(negative, "v")[0]
    neg_t = analytic_classfy(negative, "v")
    neg_t = sum(neg_t)
    negs = (neg_v / neg_t) * 100
    format_neg = "{:.2f}".format(negs) + "%"

    sug_v = analytic_classfy(sugestion, "v")[0]
    sug_t = analytic_classfy(sugestion, "v")
    sug_t = sum(sug_t)
    sugs = (sug_v / sug_t) * 100
    format_sug = "{:.2f}".format(sugs) + "%"

    return [
        html.Span('Pontos forte: {}|\n{}'.format(pos, format_pos),
                  className="pos_cl"),
                  
        html.Span('Mais sugerido: {}|\n{}'.format(
            sug, format_sug), className="sug_cl"),
        html.Span('Maior dor: {}|\n{}'.format(neg, format_neg),
                  className="neg_cl"),
    ]


@app.callback(
    Output("funnel_chart", "figure"),
    [
        Input('dropdown-id', 'value'),
        Input("origin-marker", "value"),
        Input("year-marker", "value")
    ]
)
def generate_indicator(dropdown_value, check_select, check_year):
    df_filtered = df[df["Mês pesquisa"].isin(dropdown_value) & df["Origin"].isin(
        check_select) & df["Ano"].isin(check_year)]
    akk = ["Positivo", "Negativo", "Sugestão"]
    main_a = df_filtered[df_filtered["Sentimento"].isin(akk)]
    main_b = df_filtered[df_filtered["Sentimento2"].isin(akk)]
    main1 = main_a["Classificação 1"]
    main2 = main_b["Classificação 2"]
    main_t = pd.concat([main1, main2], axis=0)

    positive_a = df_filtered[df_filtered["Sentimento"] == "Positivo"]
    positive_b = df_filtered[df_filtered["Sentimento2"] == "Positivo"]
    positive1 = positive_a["Classificação 1"]
    positive2 = positive_b["Classificação 2"]
    positive = pd.concat([positive1, positive2])

    sugestion_a = df_filtered[df_filtered["Sentimento"] == "Sugestão"]
    sugestion_b = df_filtered[df_filtered["Sentimento2"] == "Sugestão"]
    sugestion1 = sugestion_a["Classificação 1"]
    sugestion2 = sugestion_b["Classificação 2"]
    sugestion = pd.concat([sugestion1, sugestion2])

    negative_a = df_filtered[df_filtered["Sentimento"] == "Negativo"]
    negative_b = df_filtered[df_filtered["Sentimento2"] == "Negativo"]
    negative1 = negative_a["Classificação 1"]
    negative2 = negative_b["Classificação 2"]
    negative = pd.concat([negative1, negative2])

    fig = go.Figure()

    fig.add_trace(go.Bar(
        name='Positivo',
        y=analytic_classfy(positive, "k"),
        x=analytic_classfy(positive, "v"),
        marker_color="#5a65e5",
        orientation="h",
        # transition={
        #         'duration': 500,
        #         'easing': 'cubic-in-out'
        #     }
    ))
    fig.add_trace(go.Bar(
        name='Sugestão',
        y=analytic_classfy(sugestion, "k"),
        x=analytic_classfy(sugestion, "v"),
        marker_color="#F78702",
        orientation="h"
    ))

    fig.add_trace(go.Bar(
        name='Negativo',
        y=analytic_classfy(negative, "k"),
        x=analytic_classfy(negative, "v"),
        marker_color="#ff4d4d",
        orientation="h"
    ))
    fig.update_layout(barmode='stack',
                      title={
                          'text': "Classificações",
                          'y': 0.9,
                          'x': 0.5,
                          'xanchor': 'center',
                          'yanchor': 'top'
                      },
                      plot_bgcolor='#06182b', paper_bgcolor='#06182b',
                      font_color="white")
    fig.update_traces(width=0.35, hovertemplate='Benefício: %{label}<br>Quantidade Respostas: %{value}')
    return fig


@app.callback(
    Output("feeling", "figure"),
    [
        Input('dropdown-id', 'value'),
        Input("origin-marker", "value"),
        Input("year-marker", "value")
    ]
)
def generate_indicator(dropdown_value, check_select, check_year):
    df_filtered = df[df["Mês pesquisa"].isin(
        dropdown_value) & df["Origin"].isin(check_select) & df["Ano"].isin(check_year)]
    a = df_filtered["Sentimento"]
    b = df_filtered["Sentimento2"]
    ab = pd.concat([a, b])

    bas0 = df[df["Origin"].isin(check_select) & df["Ano"].isin(check_year)]
    bas1 = bas0[bas0["Mês pesquisa"] == max(bas0["Mês pesquisa"].unique())]
    bas = bas1["Sentimento"]
    asa = bas1["Sentimento2"]
    basa = pd.concat([asa, bas])
    y = feeling_rate(basa, "positivo")
    ya = feeling_rate(basa, "sugestão")
    yb = feeling_rate(basa, "negativo")

    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode="number+gauge", value=feeling_rate(ab, "positivo"),
        domain={'x': [0.25, 1], 'y': [0.8, 0.9]},
        title={'text': "Positivo"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0.25, 100]},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': y},
            'bgcolor': "#5a65e5",
            'steps': [
                {'range': [30, 70], 'color': "#515ace"},
                {'range': [70, 100], 'color': "#4850b7"}],
            'bar': {'color': "#41b5df"}}))

    fig.add_trace(go.Indicator(
        mode="number+gauge", value=feeling_rate(ab, "negativo"),
        domain={'x': [0.25, 1], 'y': [0.2, 0.3]},
        title={'text': "Negativo"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0.25, 100]},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': yb},
            'bgcolor': "#ff4d4d",
            'steps': [
                {'range': [30, 70], 'color': "#e54545"},
                {'range': [70, 100], 'color': "#cc3d3d"}],
            'bar': {'color': "#41b5df"}}))

    fig.add_trace(go.Indicator(
        mode="number+gauge", value=feeling_rate(ab, "sugestão"),
        domain={'x': [0.25, 1], 'y': [0.5, 0.6]},
        title={'text': "Sugestão"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0.25, 100]},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': ya},
            'bgcolor': "#F78702",
            'steps': [
                {'range': [30, 70], 'color': "#de7901"},
                {'range': [70, 100], 'color': "#c56c01"}],
            'bar': {'color': "#41b5df"}}))

    fig.update_layout(height=200, margin={'t': 0, 'b': 0, 'l': 0})
    fig.update_layout(plot_bgcolor='#001122',
                      paper_bgcolor='#001122', font_color="white")
    fig.update_traces(number_font_size=30, title_font_size=20, gauge_bar_line_width=2, gauge_bordercolor="black",
                      number_font_family='bomdia', delta_font_family='bomdia', legendgrouptitle_font_family='bomdia')
    return fig


@app.callback(
    Output("pie-chart", "figure"),
    [
        Input('dropdown-id', 'value'),
        Input("origin-marker", "value"),
        Input("year-marker", "value")
    ]
)
def generate_pie(dropdown_value, check_select, check_year):
    df_filtered = df[df['Mês pesquisa'].isin(
        dropdown_value) & df['Origin'].isin(check_select) & df["Ano"].isin(check_year)]
    x = dict(
        Counter(df_filtered['Qual dos nossos benefícios melhor te atende? _Dimension']))
    keys = []
    values = []
    items = x.items()
    for item in items:
        keys.append(item[0]), values.append(item[1])
    fig = px.pie(df_filtered, values=values, names=keys,
                 title='Melhores benefícios')
    fig.update_traces(textposition='inside', textinfo='percent+label', hovertemplate='Benefício: %{label} <br>Quantidade Respostas: %{value}')
    fig.update_layout(plot_bgcolor="#06182b",
                      paper_bgcolor='#06182b', font_color="white")
    fig.update_traces(legendgrouptitle_font_family='bomdia')
    return fig


@app.callback(
    Output("nps-indicator", "figure"),
    [
        Input('dropdown-id', 'value'),
        Input("origin-marker", "value"),
        Input("year-marker", "value")
    ]
)
def generate_indicator(dropdown_value, check_select, check_year):
    df_filtered = df[df['Mês pesquisa'].isin(
        dropdown_value) & df['Origin'].isin(check_select) & df["Ano"].isin(check_year)]
    a = df_filtered['NPS']

    b = df[df['Origin'].isin(check_select) & df["Ano"].isin(check_year)]
    b = b[b["Ano"] == max(b["Ano"].unique())]
    b = b["NPS"]
    x = int(nps_calculate(a))
    y = int(nps_calculate(b))
    figScorees = go.Figure()
    figScorees.add_trace(go.Indicator(
        mode="number",
        title={'text': "NPS Score<br><span style='font-size:0.8em;color:gray'>Mês selecionado</span><br>"},
        value=x,
        delta={'position': "right", 'reference': y},
        domain={'x': [0, 1], 'y': [0, 1]})
    )
    figScorees.update_layout(plot_bgcolor='#06182b',
                             paper_bgcolor='#06182b', font_color="white")
    figScorees.update_traces(number_font_size=56, delta_font_size=20, title_font_size=20, number_font_family='bomdia',
                             delta_font_family='bomdia', legendgrouptitle_font_family='bomdia')
    return figScorees


@app.callback(
    Output("csat_ajuda", "figure"),
    [
        Input('dropdown-id', 'value'),
        Input("origin-marker", "value"),
        Input("year-marker", "value")
    ]
)
def generate_chart(dropdown_value, check_select, check_year):
    df_filtered = df[df['Mês pesquisa'].isin(
        dropdown_value) & df['Origin'].isin(check_select) & df["Ano"].isin(check_year)]
    df_filteredAJUDA = df_filtered['Você já precisou da ajuda da nossa equipe de ajuda alguma vez? Se sim, avalie com uma nota de 1 a 5']
    b = df[df['Origin'].isin(check_select) & df["Ano"].isin(check_year)]
    b = b[b["Mês pesquisa"] == max(b["Mês pesquisa"].unique())]
    b = b['Você já precisou da ajuda da nossa equipe de ajuda alguma vez? Se sim, avalie com uma nota de 1 a 5']
    y = csat_(b)
    figScorew = go.Figure(go.Indicator(
        mode="gauge+number",
        title={'text': "CSAT Ajuda"},
        value=csat_(df_filteredAJUDA),
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [None, 100]},
               'borderwidth': 2,
               'bordercolor': "gray",
               'steps':
               [
            {'range': [0, 50], 'color': "#990000"},
            {'range': [50, 70], 'color': "#b8b800"},
            {'range': [70, 100], 'color': "#004000"}
        ],

            'bar': {'color': "#41b5df"},
            'threshold': {'line': {'color': "white", 'width': 4}, 'thickness': 0.75, 'value': y}},
            ))
    figScorew.update_layout(plot_bgcolor='#06182b',
                            paper_bgcolor='#06182b', font_color="white")
    # number_font_size=30, delta_font_size=20, title_font_size=25,
    figScorew.update_traces(number_font_family='bomdia',
                            delta_font_family='bomdia', legendgrouptitle_font_family='bomdia')
    return figScorew


@app.callback(
    Output("csat_comercial", "figure"),
    [
        Input('dropdown-id', 'value'),
        Input("origin-marker", "value"),
        Input("year-marker", "value")
    ]
)
def generate_chart(dropdown_value, check_select, check_year):
    df_filtered = df[df['Mês pesquisa'].isin(
        dropdown_value) & df['Origin'].isin(check_select) & df["Ano"].isin(check_year)]
    df_filteredCOMERCIAL = df_filtered['O que você acha do atendimento e acompanhamento do nosso vendedor? Se sim, avalie com uma nota de 1 a 5_Dimension']
    b = df[df['Origin'].isin(check_select) & df["Ano"].isin(check_year)]
    b = b[b["Mês pesquisa"] == max(b["Mês pesquisa"].unique())]
    b = b['O que você acha do atendimento e acompanhamento do nosso vendedor? Se sim, avalie com uma nota de 1 a 5_Dimension']
    y = csat_(b)
    figScorew = go.Figure(go.Indicator(
        mode="gauge+number",
        title={'text': "CSAT Comercial"},
        value=csat_(df_filteredCOMERCIAL),
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 100]},
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps':
                [
                {'range': [0, 50], 'color': "#990000"},
                {'range': [50, 70], 'color': "#b8b800"},
                {'range': [70, 100], 'color': "#004000"}
            ],
            'bar': {'color': "#41b5df"},
            'threshold': {'line': {'color': "white", 'width': 4}, 'thickness': 0.75, 'value': y}}))
    figScorew.update_layout(plot_bgcolor='#06182b',
                            paper_bgcolor='#06182b', font_color="white")
    figScorew.update_traces(number_font_family='bomdia',
                            delta_font_family='bomdia', legendgrouptitle_font_family='bomdia')
    return figScorew


@app.callback(
    Output('memory-table', 'data'),
    [
        Input('dropdown-id', 'value'),
        Input("origin-marker", "value"),
        Input("year-marker", "value")
    ]
)
def callback_func(dropdown_value, check_select, check_year):
    df_filtered = df[df['Mês pesquisa'].isin(
        dropdown_value) & df['Origin'].isin(check_select) & df["Ano"].isin(check_year)]
    return df_filtered.to_dict(orient='records')


@app.callback(
    Output("number_answer", "children"),
    [
        Input('dropdown-id', 'value'),
        Input("origin-marker", "value"),
        Input("year-marker", "value")
    ]
)
def callback_answer(dropdown_value, check_select, check_year):
    df_filtered = df[df['Mês pesquisa'].isin(
        dropdown_value) & df['Origin'].isin(check_select) & df["Ano"].isin(check_year)]
    df_filteredNPS = df_filtered['NPS']
    value_answer = len(df_filteredNPS)
    return html.Span("{}".format(value_answer), className="num_ans_class")


@app.callback(
    Output('promoter-indicator', 'children'),
    Output('neutral-indicator', 'children'),
    Output('detractor-indicator', 'children'),
    [
        Input('dropdown-id', 'value'),
        Input("origin-marker", "value"),
        Input("year-marker", "value")
    ]
)
def nps_indicator(dropdown_value2, check_select2, check_year):
    df_filtered = df[df['Mês pesquisa'].isin(
        dropdown_value2) & df['Origin'].isin(check_select2) & df["Ano"].isin(check_year)]
    df_filteredNPS = df_filtered['NpsClassification']
    prom = type_user_nps(df_filteredNPS, "promoter")
    neut = type_user_nps(df_filteredNPS, "neutral")
    detr = type_user_nps(df_filteredNPS, "detractor")
    return[
        html.Span('Promotor: {}'.format(prom),
                  className="promoter-indicators"),
        html.Span('Neutro: {}'.format(neut), className="neutral-indicators"),
        html.Span('Detrator: {}'.format(detr),
                  className="detractor-indicators"),
    ]


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")