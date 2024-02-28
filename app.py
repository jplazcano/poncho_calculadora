import streamlit as st
import plotly.graph_objs as go
import pandas as pd


def calculate_compound_interest(P, C, t, r, capitalization):
    frequency_mapping = {
        'Anual': 1,
        'Semestral': 2,
        'Trimestral': 4,
        'Mensual': 12,
        'Diaria': 365
    }
    n = frequency_mapping[capitalization]
    r_decimal = r / 100  # Convertir la tasa de interés a decimal

    total_amount = P
    growth_over_time = [P]

    for year in range(1, t + 1):
        if capitalization == 'Mensual':
            for month in range(1, 13):
                total_amount *= (1 + r_decimal / n)
                total_amount += C
        else:
            # Para capitalización no mensual, acumular contribuciones y aplicarlas al momento de la capitalización
            total_amount *= (1 + r_decimal / n)
            total_amount += C * 12  # Aplicar todas las contribuciones anuales de una vez

        growth_over_time.append(total_amount)

    total_contributions_list = [P + C * 12 * year for year in range(t + 1)]

    # Crear un DataFrame para visualizar los resultados
    df= pd.DataFrame({
        'Year': [f'Year {i}' for i in range(t + 1)],
        'Future Value': growth_over_time,
        'Total Contributions': total_contributions_list
    })

    return df

def plot_with_plotly(df):
    # Crear la figura
    fig = go.Figure()

    # Agregar la línea del valor futuro
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Future Value'], mode='lines+markers', name='Future Value'))
    # Agregar la línea de las contribuciones totales
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Total Contributions'], mode='lines+markers', name='Total Contributions'))

    # Actualizar el layout de la gráfica
    fig.update_layout(title='Interés compuesto a lo largo del tiempo',
                      xaxis_title='Year',
                      yaxis_title='Amount',
                      legend_title='Legend')

    return fig

st.title('Calculadora de Interés Compuesto, Poncho Capital')
st.image("/Users/juanpelazcano/Desktop/calculadora_poncho/Flor Bustamane Arias IMG 7778.png", width=200)

P = st.number_input('Cantidad Inicial', min_value=0.0, value=1000.0, step=100.0)
C = st.number_input('Contribución Mensual', min_value=0.0, value=100.0, step=10.0)
t = st.number_input('Cantidad de Tiempo en Años', min_value=1, value=10, step=1)
r = st.number_input('Tasa de Interés Estimada (%)', min_value=0.0, value=5.0, step=0.1)
capitalization = st.selectbox('Frecuencia de Capitalización', ('Anual', 'Mensual'))

if st.button('Calcular'):
    df = calculate_compound_interest(P, C, t, r, capitalization)
    df_styled = df.style.format({
    'Future Value': '${:,.2f}',
    'Total Contributions': '${:,.2f}'
})
    st.dataframe(df_styled)

    fig = plot_with_plotly(df)
    st.plotly_chart(fig)
