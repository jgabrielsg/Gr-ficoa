from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.layouts import row
from bokeh.models import Range1d
import pandas as pd

# x = [1, 7, 13, 42]
# y = [2, 14, 26, 84]
df = pd.read_csv("drug-use-by-age.csv")

x = df["age"]
y = df["marijuana-use"]

output_file("marijuana.html")

figure = figure(x_range=x, title="Gráfico de Barras",
           toolbar_location=None, tools="", width = 1500, height = 700)
figure.vbar(x=x, top=y, width = 1 - 0.1, color = "#A69F5E")
figure.background_fill_color = '#F1F2E6'


figure.xaxis.axis_label = "Faixa Etárias"
figure.xaxis.axis_label_text_color = "#736641"
figure.xaxis.axis_label_text_font = "Arial"
figure.xaxis.axis_label_text_font_size = "20px"
figure.xaxis.major_label_text_color = "#736641"
figure.xaxis.major_label_text_font = "Arial"
figure.xaxis.major_label_text_font_size = "20px"
figure.xaxis.major_label_text_font_style = "bold"


figure.yaxis.axis_label = "Uso de Maconha por Porcentagem da População"
figure.yaxis.axis_label_text_color = "#736641"
figure.yaxis.axis_label_text_font = "Arial"
figure.yaxis.axis_label_text_font_size = "20px"
figure.yaxis.major_label_text_color = "#736641"
figure.yaxis.major_label_text_font = "Arial"
figure.yaxis.major_label_text_font_size = "15px"
figure.yaxis.major_label_text_font_style = "bold"

figure.xaxis.axis_label_standoff = 15
figure.yaxis.axis_label_standoff = 15
figure.xaxis.major_label_standoff = 10
figure.yaxis.major_label_standoff = 10

figure.title.text = "Uso de Maconha por Idade (EUA)"
figure.title.text_color = "#736641"
figure.title.text_font = "Futura"
figure.title.text_font_size = "42px"
figure.title.align = "center"


figure.xaxis.minor_tick_in = -5
figure.yaxis.minor_tick_in = -5
figure.yaxis.major_label_orientation = "vertical"

figure.xgrid.grid_line_color = None
figure.ygrid.grid_line_color = None

save(figure)
show(figure)



# # Criar o segundo gráfico
# x2 = [5, 10, 15, 20]
# y2 = [3, 6, 9, 12]
# figure = figure(sizing_mode='stretch_width', width=700, height=400)
# figure.line(x2, y2, line_color='green')

# # Combinar os dois gráficos em uma única grade
# combined_figure = row(figure, figure)

# # Remover as grades dos gráficos
# figure.xgrid.grid_line_color = None
# figure.ygrid.grid_line_color = None
# figure.xgrid.grid_line_color = None
# figure.ygrid.grid_line_color = None

# # Salvar e exibir o gráfico combinado
