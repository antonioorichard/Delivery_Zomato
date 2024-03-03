#================
#        Library
#================
import streamlit as st
from PIL import Image

#        work data
import pandas as pd

## Importar map
import folium
from streamlit_folium import folium_static
from folium.plugins import Draw # desenhar

# Gráficos
import plotly.express as px
import plotly.graph_objects as go 
#=================
#        Library
#=================





st.set_page_config( page_title = 'Visão Cidades', page_icon = '🏙️', layout = 'wide' )



#____________---Loading data---__________
df = pd.read_csv('Dataset/zomato.csv')
#____________--\Loading data---__________



#___________---Limpeza dos dados---_______
def clean_data(df):
#Correção do espaço
    lista_cols = list(df.head(0)) 
    for cols in lista_cols:
        # Verificar
        if  type(df.loc[0 , cols]) == str:
            # Cocertar o espaço 'texto ' p/ 'texto'
            df.loc[:, cols] = df.loc[:, cols].str.strip() 
            print('Funcionou str')
            # Remover o 'NaN'
            df = df.loc[df[cols] != 'NaN', :]

        else: 
            print('Funcionou float or int')
            # Armazenar o tipo 
            classe = type(df.loc[0,cols])
            # Mudo o tipo para str
            df[cols]= df[cols].astype(str)
            # Concertar os espaços
            df.loc[:, cols] = df.loc[:, cols].str.strip()
            # Remover o 'NaN'
            df = df.loc[df[cols] != 'NaN', :]
            # Converto para tipo anterior
            df[cols]= df[cols].astype(classe)
    
    return(df)

# Chamando a função de limpeza clean_data
df =clean_data(df)
#___________--\Limpeza dos dados---_______




COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}
def color_name(color_code):
    return COLORS[color_code]
#__________--- Color---___________________



#========================================
#              Barra Laterals
#========================================
    
#image_path = 'C:/Users\Antonio Richard/OneDrive - acad.ifma.edu.br/Documentos/A Sala de aprendizado/repos/JupyterLab/Dashboards/Delivery_india/'

#image = Image.open(image_path + 'Delivery.jpg')
st.sidebar.markdown(' # Zomato Company !')
image = Image.open('Logo_scooter_delivery.png')

st.sidebar.image(image, width = 150)

st.sidebar.markdown('## Fastest Delivery in Town')

#_____________---FILTER---_______

st.sidebar.markdown("""---""")

# FILTRO DE DATA

st.sidebar.markdown(' ## Filtros ')
st.sidebar.markdown(' ### Escolha os Paises que Deseja visualizar as Informações!')

# FILTRO DE CLIMA
# Options
#interessante tirar conditions dos nomes 

traffic_options1 = st.sidebar.multiselect( 
                     'Selecione o País aqui 👇!', 
                    df['Country_id'].unique(), 
                    default = ['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada', 'Singapure', 
                               'United Arab Emirates', 'India', 'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'], 
)

linhas_selecionadas2 =  df['Country_id'].isin( traffic_options1)
df = df.loc[linhas_selecionadas2,:]

#========================================
#              \Barra Laterals
#========================================



#========================================
#              ESTRUTURA
#========================================
#____________---Title---____________
st.markdown( '# 🏙️ Visão Cidades 🌆')

#____________---Bloco---____________
with st.container(height = None, border = True):
    #st.markdown('Top 10 cidades com mais Restaurantes na Base de Dados')
    cols = ['Restaurant ID', 'City', 'Country_id']
    # Selecao de linhas
    df_aux = df.loc[:,cols].groupby(['City','Country_id']).count().reset_index().sort_values('Restaurant ID', ascending= False)
    df_aux = df_aux.iloc[0:10,:].reset_index()
    df_aux.drop("index", axis = "columns", inplace = True)
    
    # desenhar o gráfio de linhas
    fig = px.bar(df_aux, x='City', y='Restaurant ID', text = 'Restaurant ID' ,color ='Country_id',  labels={'City': 'Cidades', 'Restaurant ID': 'Quantidade de Restaurantes', 'Country_id': 'Países'})
    fig.update_layout(title='Top 10 cidades com mais Restaurantes na Base de Dados', title_x=0.25, title_font=dict(size = 24)) # Ajustar a 
    # a posição do title e a fonte. 

    fig.update_xaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário
    fig.update_yaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário
    
    st.plotly_chart(fig, use_container_width = True)

    

    
    
    
with st.container(height = None, border = True):
    col0, col1 = st.columns(2)
    
    with col0: 
        #st.markdown('Cidades com Restaurantes com média de avaliação up')
        cols = ['Aggregate rating', 'City', 'Country_id']
        filtro = df['Aggregate rating'] > 4
        # Selecao de linhas
        df_aux = df.loc[filtro == True,cols].groupby(['City','Country_id']).count().reset_index().sort_values('Aggregate rating', ascending= False)
        df_aux = df_aux.iloc[0:10,:]
        # desenhar o gráfio de linhas
        fig = px.bar(df_aux, x='City', y='Aggregate rating', text = 'Aggregate rating',color ='Country_id' , labels={'City': 'Cidades', 'Aggregate rating': 'Média de avaliação', 'Country_id': 'Países'})
        fig.update_layout(title='Top 10 cidades com Restaurantes com avaliação acima de 4', title_x=0.0, title_font=dict(size = 24)) # Ajustar a 
        # a posição do title e a fonte. 

        fig.update_xaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário
        fig.update_yaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário

        st.plotly_chart(fig, use_container_width = True)


    with col1: 
        #st.markdown('Cidades com Restaurantes com média de avaliação low')
        cols = ['Aggregate rating', 'City', 'Country_id']
        filtro = df['Aggregate rating'] < 2.5
        # Selecao de linhas
        df_aux = df.loc[filtro == True, cols].groupby(['City','Country_id']).count().reset_index().sort_values('Aggregate rating', ascending= True)
        df_aux = df_aux.iloc[0:10,:]
        # desenhar o gráfio de linhas
        fig = px.bar(df_aux, x='City', y='Aggregate rating', text ='Aggregate rating', color ='Country_id' , labels={'City': 'Cidades', 'Aggregate rating': 'Média de avaliação', 'Country_id': 'Países'})
        fig.update_layout(title='Top 10 cidades com Restaurantes com avaliação abaixo de 2.5', title_x=0.01, title_font=dict(size = 24)) # Ajustar a 
        # a posição do title e a fonte. 

        fig.update_xaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário
        fig.update_yaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário

        st.plotly_chart(fig, use_container_width = True)

            
        
with st.container(height = None, border = True):
    #st.markdown('Top 10 Cidades mais restaurantes com tipos culinários distintos')
    cols = ['Cuisines', 'City', 'Country_id']
    # Selecao de linhas
    df_aux = df.loc[:,cols].groupby(['City','Country_id']).nunique().reset_index().sort_values('Cuisines', ascending= False)
    df_aux = df_aux.iloc[0:10,:]
    # desenhar o gráfio de linhas
    fig = px.bar(df_aux, x='City', y='Cuisines', text ='Cuisines', color ='Country_id' , labels={'City': 'Cidades', 'Cuisines': 'Quantidade de Tipos Culinários Únicos', 'Country_id': 'Países'})
    fig.update_layout(title='Top 10 Cidades com mais tipos culinários distintos', title_x=0.2, title_font=dict(size = 24)) # Ajustar a 
    # a posição do title e a fonte. 

    fig.update_xaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário
    fig.update_yaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário

    st.plotly_chart(fig, use_container_width = True)

#========================================
#              \ESTRUTURA
#========================================