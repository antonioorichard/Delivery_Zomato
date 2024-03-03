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


    ## Gráficos
import plotly.express as px
import plotly.graph_objects as go
#=================
#        Library
#=================

    



st.set_page_config( page_title = 'Visão da Culinária', page_icon = '👨‍🍳', layout = 'wide' )



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
st.sidebar.markdown(' ### Por padrão estão todos selecionados!')

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
st.sidebar.markdown("""---""")
# Filtro slider
num_slider = st.sidebar.slider( 
    'Quantidade de Restaurantes ?', 
                  value =10,
                  min_value = 1,
                  max_value = 20, 
                                 
                 )

#========================================
#              \Barra Laterals
#========================================
# Restruturada em Cuisines
df2 = df.loc[:, ['Cuisines', 'Aggregate rating', 'Restaurant Name']]
        # Bem para resolver o problema de várias culinárias em uma linha, vamos pegas nomes e coloca []
    
df2['Cuisines'] = df2['Cuisines'].str.split(', ')

        # Dar uma linha para cada elemento
df_exploded = df2.explode('Cuisines')
#========================================
#              ESTRUTURA
#========================================
#____________---Title---____________
st.markdown( '# 🍽️ Visão Cuisines 🍽️')
st.markdown( '### 👨‍🍳 Melhores Restaurantes dos Principais tipos Culinários 🍽️')
with st.container(height = None, border = False):
    with st.expander("more"):
        st.write(" Foram selecionados as culinárias que se encontra em mais estabeliciementos, os melhores Restaurantes  foram escolhidos por meio do critério melhor avaliação que pode ser de 0 a 5, e ainda a maior quantidade de votos. A ordem do tipo culinário mais consumido, é cresente da direita para esquerda.  Sendo está analise atualizada junto com o dataset")
        
# --------------------------------------///\\\--------------------------------------------
#                     Selecionando Top culinária rosa de informações dela
# Quais os 5 principais tipos culinários ?
                #Quais os pratos que mais saem? 
df2 = df.loc[:, ['Cuisines',  'Restaurant Name', 'Country_id','City', 'Average Cost for two', 'Aggregate rating', 'Votes']]
        # Bem para resolver o problema de várias culinárias em uma linha, vamos pegas nomes e coloca []
df2['Cuisines'] = df2['Cuisines'].str.split(', ')
        # Dar uma linha para cada elemento
df_exploded = df2.explode('Cuisines')
        # Agrupando
top=df_exploded.loc[:,['Cuisines',  'Restaurant Name']].groupby(['Cuisines'] ).count().reset_index().sort_values(['Restaurant Name'], ascending= False)
        # Resetando o index
top_cuisines = top.loc[:5,:].reset_index()
        # Deletando a coluna 'index'
top_cuisines.drop("index" ,axis='columns', inplace=True)
        # Selecionando somente os cincos primeiros
top_cuisines = top_cuisines.iloc[0:5,:]

# Criando um biblioteca para armazenar informações com Listas e dicionários
top_library = [
        {'Cuisines': 'Tipo de comida', 'Restaurant Name': 'Name', 'Country_id': 'Name', 'City': 'Name0', 'Average Cost for two': 0, 'Aggregate rating': 5, 'Votes': 10,},
        {'Cuisines': 'Tipo de comida', 'Restaurant Name': 'Name', 'Country_id': 'Name', 'City': 'Name1', 'Average Cost for two': 1, 'Aggregate rating': 6, 'Votes': 11,},
        {'Cuisines': 'Tipo de comida', 'Restaurant Name': 'Name', 'Country_id': 'Name', 'City': 'Name2', 'Average Cost for two': 2, 'Aggregate rating': 7, 'Votes': 12,},
        {'Cuisines': 'Tipo de comida', 'Restaurant Name': 'Name', 'Country_id': 'Name', 'City': 'Name3', 'Average Cost for two': 3, 'Aggregate rating': 8, 'Votes': 13,},
        {'Cuisines': 'Tipo de comida', 'Restaurant Name': 'Name', 'Country_id': 'Name', 'City': 'Name4', 'Average Cost for two': 4, 'Aggregate rating': 9, 'Votes': 14,},
              ]

# Exemplo como pode acessa informações dados[número do dicionário]['Votes'] = 18


#Selecionando os melhores restaurantes pela maior nota e quantidade de votos
lista = list(range(len(top_cuisines['Cuisines'])))


for index in lista:
    filtro = df_exploded['Cuisines'].str.contains(top_cuisines.loc[index, 'Cuisines'])
    df_sel=df_exploded.loc[filtro != False,:].sort_values(['Aggregate rating','Votes'], ascending= False)
    df_sel = df_sel.reset_index()
    df_sel.drop("index", axis = 'columns', inplace=True)
    df_sel = df_sel.iloc[0:2,: ]
# Alterando o top_library
    top_library[index]['Cuisines']              = df_sel.loc[0, 'Cuisines']
    top_library[index]['Restaurant Name']       = df_sel.loc[0, 'Restaurant Name'] 
    top_library[index]['Country_id']            = df_sel.loc[0, 'Country_id']
    top_library[index]['City']                  = df_sel.loc[0, 'City']   
    top_library[index]['Average Cost for two']  = df_sel.loc[0, 'Average Cost for two']
    top_library[index]['Aggregate rating']      = df_sel.loc[0, 'Aggregate rating']   
    top_library[index]['Votes']                 = df_sel.loc[0, 'Votes']    

# --------------------------------------\\\///----------------------------------------

#____________---Bloco---____________
with st.container(height = None, border = True):
        
    col0, col1, col2, col3, col4 = st.columns(5)
    with col0:
        Name       = top_library[0]['Cuisines']
        Restaurant = top_library[0]['Restaurant Name']
        Nota       = top_library[0]['Aggregate rating']
        Pais       = top_library[0]['Country_id']
        Preco      = top_library[0]['Average Cost for two']
        cidade     = top_library[0]['City'] 
        
        value = f"{Nota}/5.0"
        col0.metric(f'{Name}: {Restaurant}', value = value, help = f"Pais: {Pais}, \n \n Cidade: {cidade}, \n \n Preço do Prato para dois: {Preco}  ")
        
    with col1:
       
        Name       = top_library[1]['Cuisines']
        Restaurant = top_library[1]['Restaurant Name']
        Nota       = top_library[1]['Aggregate rating']
        Pais       = top_library[1]['Country_id']
        Preco      = top_library[1]['Average Cost for two']
        cidade     = top_library[1]['City'] 
        
        value = f"{Nota}/5.0"
        col1.metric(f'{Name}: {Restaurant}', value = value, help = f"Pais: {Pais}, \n \n Cidade: {cidade}, \n \n Preço do Prato para dois: {Preco}  ")        
    with col2:
        Name       = top_library[2]['Cuisines']
        Restaurant = top_library[2]['Restaurant Name']
        Nota       = top_library[2]['Aggregate rating']
        Pais       = top_library[2]['Country_id']
        Preco      = top_library[2]['Average Cost for two']
        cidade     = top_library[2]['City'] 
        
        value = f"{Nota}/5.0"
        col2.metric(f'{Name}: {Restaurant}', value = value, help = f"Pais: {Pais}, \n \n Cidade: {cidade}, \n \n Preço do Prato para dois: {Preco}  ")
        
    with col3:
        Name       = top_library[3]['Cuisines']
        Restaurant = top_library[3]['Restaurant Name']
        Nota       = top_library[3]['Aggregate rating']
        Pais       = top_library[3]['Country_id']
        Preco      = top_library[3]['Average Cost for two']
        cidade     = top_library[3]['City'] 
        
        value = f"{Nota}/5.0"
        col3.metric(f'{Name}: {Restaurant}', value = value, help = f"Pais: {Pais}, \n \n Cidade: {cidade}, \n \n Preço do Prato para dois: {Preco}  ")
        
    with col4:
        Name       = top_library[4]['Cuisines']
        Restaurant = top_library[4]['Restaurant Name']
        Nota       = top_library[4]['Aggregate rating']
        Pais       = top_library[4]['Country_id']
        Preco      = top_library[4]['Average Cost for two']
        cidade     = top_library[4]['City'] 
        
        value = f"{Nota}/5.0"
        col4.metric(f'{Name}: {Restaurant}', value = value, help = f"Pais: {Pais}, \n \n Cidade: {cidade}, \n \n Preço do Prato para dois: {Preco}  ")
    
with st.container(height = None, border = True):
   # PROBLEMA AQUI NÃO ESTÁ ESPLODINDO
    st.write(f'Top {num_slider} Restaurantes') 
    df2 = df.loc[:,['Restaurant ID', 'Restaurant Name', 'Country_id', 'City', 'Cuisines', 'Average Cost for two', 'Aggregate rating', 'Votes' ]]

    df2['Cuisines'] = df2['Cuisines'].str.split(', ')
    
        # Dar uma linha para cada elemento
    df_exploded = df2.explode('Cuisines')
    df_aux = df_exploded.loc[:, ['Restaurant ID', 'Restaurant Name', 'Country_id', 'City', 'Cuisines', 'Average Cost for two', 'Aggregate rating', 'Votes' ]].sort_values('Aggregate rating', ascending =  False)
    # Regula quantidade exibida com -'num_slider'
    df_aux = df_aux.iloc[0:num_slider,:]
    st.dataframe(df_aux)

        
        
with st.container(height = None, border = True):
    col0, col1 = st.columns(2)
    
    with col0: 
        #st.markdown('Top 10 Melhores Tipos de Culinárias')
       # df2 = df.loc[:, ['Cuisines', 'Aggregate rating', 'Country_id']]
        # Bem para resolver o problema de várias culinárias em uma linha, vamos pegas nomes e coloca []

        #df['Cuisines'] = df['Cuisines'].str.split(', ')

        # Dar uma linha para cada elemento
        #df_exploded = df2.explode('Cuisines')

        df_aux = df_exploded.loc[:, ['Cuisines', 'Aggregate rating', 'Country_id']].groupby(['Cuisines', 'Country_id']).mean().reset_index().sort_values('Aggregate rating', ascending = False)

        df_aux = df_aux.iloc[0:num_slider,:]
        fig = px.bar(df_aux, x = 'Cuisines', y = 'Aggregate rating', color ='Country_id' ,text = 'Aggregate rating', labels={'Cuisines': 'Tipos de Culinária', 'Aggregate rating': 'Média de Avaliação ', 'Country_id': 'Países'})
        fig.update_layout(title =f"Top {num_slider} melhores tipos de Culinárias", title_x=0.01, title_font=dict(size = 24)) # Ajustar a 
    # a posição do title e a fonte. 

        fig.update_xaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário
        fig.update_yaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário

        st.plotly_chart(fig, use_container_width = True)
    
     
        
    with col1: 
        #st.markdown('Top 10 Piores Tipos de Culinárias')
        
        #df = df.loc[:, ['Cuisines', 'Aggregate rating', 'Country_id']]
        # Bem para resolver o problema de várias culinárias em uma linha, vamos pegas nomes e coloca []
        #df['Cuisines'] = df['Cuisines'].str.split(', ')
        # Dar uma linha para cada elemento
        #sdf_exploded = df.explode('Cuisines')

        df_aux = df_exploded.loc[:, ['Cuisines', 'Aggregate rating', 'Country_id']].groupby(['Cuisines', 'Country_id']).mean().reset_index().sort_values('Aggregate rating', ascending = True)

        df_aux = df_aux.iloc[0:num_slider,:]
        fig = px.bar(df_aux, x = 'Cuisines', y = 'Aggregate rating', color ='Country_id' , text = 'Aggregate rating' ,labels={'Cuisines': 'Tipos de Culinária', 'Aggregate rating': 'Média de Avaliação ', 'Country_id': 'Países'})
        fig.update_layout(title =f"Top {num_slider} Piores tipos de Culinárias", title_x=0.1, title_font=dict(size = 24)) # Ajustar a 
    # a posição do title e a fonte. 

        fig.update_xaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário
        fig.update_yaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário

        st.plotly_chart(fig, use_container_width = True)
            
        

#========================================
#              \ESTRUTURA
#========================================