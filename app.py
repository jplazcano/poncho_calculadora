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
        'Año': [f'Año {i}' for i in range(t + 1)],
        'Valor Futuro': growth_over_time,
        'Contribuciones Totales': total_contributions_list
    })

    return df

def plot_with_plotly(df):
    # Crear la figura
    fig = go.Figure()

    # Agregar la línea del valor futuro
    fig.add_trace(go.Scatter(x=df['Año'], y=df['Valor Futuro'], mode='lines+markers', name='Valor Futuro'
                             , line=dict(color='#23AF32')))
    # Agregar la línea de las contribuciones totales
    fig.add_trace(go.Scatter(x=df['Año'], y=df['Contribuciones Totales'], mode='lines+markers', name='Contribuciones Totales',
                             line=dict(color='#8B133B')))

    # Actualizar el layout de la gráfica
    fig.update_layout(title='Interés compuesto a lo largo del tiempo',
                      xaxis_title='Año',
                      yaxis_title='Cantidad ($)'
                      )

    return fig


svg = """<svg data-name="Grupo 18017" xmlns="http://www.w3.org/2000/svg" width="280" height="36.448">
    <defs>
        <linearGradient id="prefix__a" x1=".5" x2=".5" y2="1" gradientUnits="objectBoundingBox">
            <stop offset="0" stop-color="#ce4372" />
            <stop offset="1" stop-color="#830b34" />
        </linearGradient>
    </defs>
    <path data-name="Trazado 9406"
        d="M49.175 23.063v6.8h-4.857V6.787h4.209l.17 1.768a9.043 9.043 0 0114.877 7.07c0 5.136-3.6 9.205-8.967 9.205a8.892 8.892 0 01-5.435-1.768m4.755-2.7a4.736 4.736 0 10-4.789-4.736 4.579 4.579 0 004.789 4.736"
        fill="#2a2a2b" />
    <path data-name="Trazado 9407"
        d="M64.911 15.641c0-5.434 4.076-9.374 9.646-9.374 5.6 0 9.646 3.94 9.646 9.374s-4.042 9.375-9.646 9.375c-5.57 0-9.646-3.94-9.646-9.375m9.646 4.823a4.633 4.633 0 004.721-4.823 4.722 4.722 0 10-9.443 0 4.633 4.633 0 004.721 4.823"
        fill="#2a2a2b" />
    <path data-name="Trazado 9408"
        d="M86.786 6.643h4.585l.136 2.14a7.386 7.386 0 015.774-2.479c4.687 0 6.963 3.057 6.963 7.914v10.426h-4.857v-9.883c0-2.582-1.257-3.974-3.533-3.974a3.854 3.854 0 00-4.212 4.076v9.782h-4.857z"
        fill="#2a2a2b" />
    <path data-name="Trazado 9409"
        d="M106.569 15.641a9.052 9.052 0 019.476-9.374 8.889 8.889 0 019.171 7.472h-4.784a4.652 4.652 0 00-8.967 1.9 4.644 4.644 0 008.967 1.868h4.823a8.928 8.928 0 01-9.2 7.507 9.071 9.071 0 01-9.476-9.375"
        fill="#2a2a2b" />
    <path data-name="Trazado 9410"
        d="M127.606 1.019h4.857v7.812a7.185 7.185 0 015.57-2.378c4.755 0 7.031 3.057 7.031 7.914v10.428h-4.857v-9.884c0-2.581-1.257-3.974-3.533-3.974a3.854 3.854 0 00-4.211 4.076v9.782h-4.857z"
        fill="#2a2a2b" />
    <path data-name="Trazado 9411"
        d="M147.382 15.641c0-5.434 4.076-9.374 9.646-9.374 5.6 0 9.646 3.94 9.646 9.374s-4.042 9.375-9.646 9.375c-5.571 0-9.646-3.94-9.646-9.375m9.646 4.823a4.633 4.633 0 004.721-4.823 4.722 4.722 0 10-9.443 0 4.633 4.633 0 004.721 4.823"
        fill="#2a2a2b" />
    <path data-name="Trazado 9412"
        d="M168.454 15.675c0-5.5 3.8-9.341 9.239-9.341a8.678 8.678 0 018.865 6.725h-2.892a5.946 5.946 0 00-5.91-4.008c-3.77 0-6.352 2.683-6.352 6.623 0 3.906 2.582 6.555 6.352 6.555a5.848 5.848 0 005.91-4.042h2.955a8.73 8.73 0 01-8.933 6.759 8.891 8.891 0 01-9.239-9.273"
        fill="#2a2a2b" />
    <path data-name="Trazado 9413"
        d="M188.506 15.641c0-5.4 3.736-9.307 9.035-9.307a8.89 8.89 0 016.725 2.853V6.64h2.887v18h-2.887v-2.546a8.889 8.889 0 01-6.725 2.853c-5.3 0-9.035-3.906-9.035-9.307m9.375 6.589a6.28 6.28 0 006.454-6.589 6.438 6.438 0 10-12.873 0 6.253 6.253 0 006.419 6.589"
        fill="#2a2a2b" />
    <path data-name="Trazado 9414"
        d="M214.904 21.859v7.735h-2.887V6.788h2.887v2.6a9.146 9.146 0 0115.828 6.24 9.146 9.146 0 01-15.828 6.235m6.42.233a6.2 6.2 0 006.454-6.469 6.47 6.47 0 00-12.941 0 6.229 6.229 0 006.487 6.469"
        fill="#2a2a2b" />
    <path data-name="Trazado 9415"
        d="M235.371 0a2.178 2.178 0 012.246 2.242 2.244 2.244 0 01-4.483 0A2.178 2.178 0 01235.371 0m-1.461 6.793h2.887v18h-2.887z"
        fill="#2a2a2b" />
    <path data-name="Trazado 9416"
        d="M243.318 19.157V9.205h-3.767V6.793h3.77v-5.8h2.887v5.8h4.959v2.411h-4.959v9.612c0 2.378.951 3.4 3.464 3.4a16.2 16.2 0 001.732-.1v2.683c-.713.068-1.461.1-2.072.1-4.11 0-6.012-1.8-6.012-5.74"
        fill="#2a2a2b" />
    <path data-name="Trazado 9417"
        d="M253.304 15.641c0-5.4 3.736-9.307 9.035-9.307a8.89 8.89 0 016.725 2.853V6.64h2.887v18h-2.887v-2.546a8.889 8.889 0 01-6.725 2.853c-5.3 0-9.035-3.906-9.035-9.307m9.375 6.589a6.28 6.28 0 006.453-6.589 6.438 6.438 0 10-12.873 0 6.253 6.253 0 006.419 6.589"
        fill="#2a2a2b" />
    <path data-name="Rectángulo 5203" fill="#2a2a2b" d="M277.113 1.019H280v23.776h-2.887z" />
    <path data-name="Trazado 9418"
        d="M36.238 20.471a18.012 18.012 0 01-18.119 17.9A18.012 18.012 0 010 20.471a18.012 18.012 0 0118.119-17.9 18.012 18.012 0 0118.119 17.9"
        transform="translate(0 -1.926)" fill="url(#prefix__a)" />
    <path data-name="Trazado 9419"
        d="M26.514 11.963a8.006 8.006 0 00-4.324-2.787.355.355 0 00-.441.343 32.415 32.415 0 01-1.559 10.139 24.11 24.11 0 01-2.013 4.47.355.355 0 00.224.524 8 8 0 001.868.221 7.965 7.965 0 006.246-12.908"
        fill="#f0f6fa" />
    <path data-name="Trazado 9420"
        d="M20.062 8.986a.355.355 0 00-.251-.1l-9.523.015a.355.355 0 00-.355.355v20.368a.355.355 0 00.506.322 14.889 14.889 0 004.893-4.331 21.876 21.876 0 003.328-6.365 31.457 31.457 0 001.506-10.012.355.355 0 00-.1-.251"
        fill="#f0f6fa" />
</svg>"""

centrado_svg = f"""
<div style="display: flex; justify-content: center; align-items: center;">
    {svg}
</div>
"""

st.markdown(centrado_svg,unsafe_allow_html=True)
st.title('Calculadora de Interés Compuesto')
st.markdown("""
<style>
.justifyText {
  text-align: justify;
  text-justify: inter-word;
}
</style>
<div class="justifyText">
<b>Bienvenido a nuestra calculadora de interés compuesto,</b> 
herramienta diseñada para <b>mostrarte cómo el crecimiento de tus
inversiones puede acelerarse</b> con el tiempo. El interés compuesto, a 
menudo llamado <b>"la octava maravilla del mundo"</b> por Albert Einstein,
es el principio por el cual tus ganancias generan aún más ganancias a lo largo del
tiempo: inviertís una cantidad inicial, y esta no solo crece por el interés
del primer período, sino que en cada período subsiguiente, el interés se calcula
sobre un monto cada vez mayor, incluyendo tanto tu inversión inicial como los intereses
previamente ganados.
<br><br>
Esta calculadora te permite explorar el impacto del interés compuesto en tus ahorros
e inversiones. Al ajustar el <b>monto inicial</b>, las <b>contribuciones mensuales</b> 
la <b>tasa de interés</b>, el <b>tiempo de inversión</b> y la <b>frecuencia de capitalización</b>, 
podrás ver cómo incluso pequeñas cantidades invertidas regularmente pueden crecer de manera
significativa a lo largo del tiempo.
<br><br>
Ya sea que estés ahorrando para la jubilación, la educación de tus hijos, o simplemente
construyendo tu patrimonio, el interés compuesto puede ser tu mejor aliado.
Acordate: <b>el tiempo y la paciencia son claves</b>.
</div>
""", unsafe_allow_html=True)
st.divider()


P = st.number_input('Cantidad Inicial', min_value=0.0, value=1000.0, step=100.0)
C = st.number_input('Contribución Mensual', min_value=0.0, value=100.0, step=10.0)
t = st.number_input('Cantidad de Tiempo en Años', min_value=1, value=10, step=1)
r = st.number_input('Tasa de Interés Estimada (%)', min_value=0.0, value=5.0, step=0.1)
capitalization = st.selectbox('Frecuencia de Capitalización', ('Anual', 'Mensual'))

if st.button('Calcular'):
    df = calculate_compound_interest(P, C, t, r, capitalization)


# Formateamos el DataFrame para usar el símbolo de dólar y sin decimales
    df_styled = df.style.format({
        'Valor Futuro': '${:,.0f}',
        'Contribuciones Totales': '${:,.0f}'
    }) 

    st.table(df_styled)

    fig = plot_with_plotly(df)
    st.plotly_chart(fig)

    # Resumen de los valores ingresados y los resultados obtenidos
    # Resumen con estilos adaptativos para temas claro y oscuro
    resumen_html = f"""
<style>
    .resumen {{
        padding: 20px;
        border-radius: 5px;
        margin-top: 20px;
        border-left: 4px solid #4e73df;
        background-color: var(--primary-bg);
        color: var(--font-color);
    }}
</style>
<div class="resumen">
    <h4>Resultados</h4>
    <p><b>Cantidad Inicial:</b> ${P:,.2f}</p>
    <p><b>Contribución Mensual:</b> ${C:,.2f}</p>
    <p><b>Cantidad de Tiempo en Años:</b> {t} años</p>
    <p><b>Tasa de Interés Estimada (%):</b> {r}%</p>
    <p><b>Frecuencia de Capitalización:</b> {capitalization}</p>
    <p>Al final del período de inversión, tu <b>Valor Futuro</b> estimado será <b>${df['Valor Futuro'].iloc[-1]:,.2f}</b>, habiendo contribuido un total de <b>${df['Contribuciones Totales'].iloc[-1]:,.2f}</b>.</p>
    <p>Este resumen final te muestra el poder del interés compuesto y cómo tus inversiones pueden crecer a lo largo del tiempo. Al ajustar diferentes parámetros, podé ver cómo cambiarán tus resultados finales, lo que te permite planificar mejor tu futuro financiero.</p>
</div>
"""

    st.markdown(resumen_html, unsafe_allow_html=True)

    # Mensaje promocional para PonchoCapital.com
    mensaje_promocional_html = f"""
<div style="padding: 20px; border-radius: 5px; margin-top: 20px; border-left: 4px solid #23AF32; color: #333; background-color: #f9f9f9; border-color: #ddd;">
    <h2 style="color: #23AF32;">¿Listo para comenzar a invertir?</h2>
    <p>En <a href="https://www.ponchocapital.com" target="_blank" style="font-weight: bold; color: #23AF32;">PonchoCapital.com</a>, hacer crecer tu patrimonio es más fácil de lo que piensas.</p>
    <ul>
        <li>Comprá dólar MEP de manera sencilla.</li>
        <li>Invertí en Acciones Argentinas.</li>
        <li>Inviertí en gigantes tecnológicos como Amazon, Google y Apple a través de los CEDEARs.</li>
        <li>Accedé a índices globales como el S&P 500, que históricamente rindió aproximadamente un promedio del 8% anual en dólares.</li>
        <li>Explorá una amplia gama de Obligaciones Negociables para diversificar tu cartera.</li>
    </ul>
    <p>Comenzar a invertir con nosotros es posible en <strong>pocos clicks</strong>. <a href="https://www.ponchocapital.com" target="_blank" style="font-weight: bold; color: #23AF32;">Únete ahora</a> y da el primer paso hacia tu libertad financiera.</p>
</div>
"""

    st.markdown(mensaje_promocional_html, unsafe_allow_html=True)
    st.image("Screenshot 2024-03-01 at 15.52.19.png")





