import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file, save
from bokeh.layouts import column, row
from bokeh.models.widgets import TableColumn, DataTable
from bokeh.models import Div, ColumnDataSource

log00 = pd.read_csv("models/log00.csv")
log03 = pd.read_csv("models/log03.csv")
log05 = pd.read_csv("models/log05.csv")
log06 = pd.read_csv("models/log06.csv")
log09 = pd.read_csv("models/log09.csv")
log10 = pd.read_csv("models/log10.csv")

dfs = [log00, log03, log05, log06, log09, log10]

for i in range(1, len(dfs)):
    dfs[i] = dfs[i].drop(columns=['Type', 'Epoch'])

logs = pd.concat(dfs, axis=1)
logs = logs.round(2)

columns = []
for c in logs.columns:
    columns.append(TableColumn(field=c, title=c))
columns.pop(0)

testpplsrc = ColumnDataSource(logs[logs.Type == "Test PPL"])
trapplsrc = ColumnDataSource(logs[logs.Type == "Training PPL"])
valpplsrc = ColumnDataSource(logs[logs.Type == "Validation PPL"])

test_table = DataTable(source=testpplsrc, columns=columns, width=590, height=50)
train_table = DataTable(source=trapplsrc, columns=columns, width=590, height=500)
val_table = DataTable(source=valpplsrc, columns=columns, width=590, height=500)

test_title = Div(text="""<b>Test Perplexity</b>""", height=20)
train_title = Div(text="""<b>Training Perplexity</b>""", height=20)
val_title = Div(text="""<b>Validation Perplexity</b>""", height=20)


train_graph = figure(title="Training Perplexity", x_axis_label="Epoch", y_axis_label="Perplexity")
train_graph.line("Epoch", "Dropout 0.0", legend_label="DO 0.0", color="blue", line_width=2, source=trapplsrc)
train_graph.line("Epoch", "Dropout 0.3", legend_label="DO 0.3", color="purple", line_width=2, source=trapplsrc)
train_graph.line("Epoch", "Dropout 0.5", legend_label="DO 0.5", color="green", line_width=2, source=trapplsrc)
train_graph.line("Epoch", "Dropout 0.6", legend_label="DO 0.6", color="pink", line_width=2, source=trapplsrc)
train_graph.line("Epoch", "Dropout 0.9", legend_label="DO 0.9", color="turquoise", line_width=2, source=trapplsrc)
train_graph.line("Epoch", "Dropout 1.0", legend_label="DO 1.0", color="black", line_width=2, source=trapplsrc)
train_graph.circle("Epoch", "Dropout 0.0", legend_label="DO 0.0", color="blue", source=trapplsrc)
train_graph.circle("Epoch", "Dropout 0.3", legend_label="DO 0.3", color="purple", source=trapplsrc)
train_graph.circle("Epoch", "Dropout 0.5", legend_label="DO 0.5", color="green", source=trapplsrc)
train_graph.circle("Epoch", "Dropout 0.6", legend_label="DO 0.6", color="pink", source=trapplsrc)
train_graph.circle("Epoch", "Dropout 0.9", legend_label="DO 0.9", color="turquoise", source=trapplsrc)
train_graph.circle("Epoch", "Dropout 1.0", legend_label="DO 1.0", color="black", source=trapplsrc)

train_graph.legend.click_policy = "hide"


val_graph = figure(title="Validation Perplexity", x_axis_label="Epoch", y_axis_label="Perplexity")
val_graph.line("Epoch", "Dropout 0.0", legend_label="DO 0.0", color="blue", line_width=2, source=valpplsrc)
val_graph.line("Epoch", "Dropout 0.3", legend_label="DO 0.3", color="purple", line_width=2, source=valpplsrc)
val_graph.line("Epoch", "Dropout 0.5", legend_label="DO 0.5", color="green", line_width=2, source=valpplsrc)
val_graph.line("Epoch", "Dropout 0.6", legend_label="DO 0.6", color="pink", line_width=2, source=valpplsrc)
val_graph.line("Epoch", "Dropout 0.9", legend_label="DO 0.9", color="turquoise", line_width=2, source=valpplsrc)
val_graph.line("Epoch", "Dropout 1.0", legend_label="DO 1.0", color="black", line_width=2, source=valpplsrc)
val_graph.circle("Epoch", "Dropout 0.0", legend_label="DO 0.0", color="blue", source=valpplsrc)
val_graph.circle("Epoch", "Dropout 0.3", legend_label="DO 0.3", color="purple", source=valpplsrc)
val_graph.circle("Epoch", "Dropout 0.5", legend_label="DO 0.5", color="green", source=valpplsrc)
val_graph.circle("Epoch", "Dropout 0.6", legend_label="DO 0.6", color="pink", source=valpplsrc)
val_graph.circle("Epoch", "Dropout 0.9", legend_label="DO 0.9", color="turquoise", source=valpplsrc)
val_graph.circle("Epoch", "Dropout 1.0", legend_label="DO 1.0", color="black", source=valpplsrc)

val_graph.legend.click_policy = "hide"


p = (column(test_title,
            test_table,
            row(column(train_title, train_table), column(val_title, val_table)),
            row(train_graph, val_graph)))

output_file('Tables_and_Graphs.html')
show(p)
