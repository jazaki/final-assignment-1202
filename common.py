# Function to remove all null values and plot bar graph

def bar_graph_plotter(x_coord, y_coord, y_label, graph_title):
  df_non_NaN = df[df[x_coord].notnull()][[x_coord, y_coord]]
  new_df = (df_non_NaN.groupby(x_coord)[y_coord].value_counts(normalize=True).mul(100).round(2).sort_index()
    .to_frame(name=y_label)).reset_index()

  fig = px.bar(new_df, x=x_coord, y=y_label, title=graph_title, color=y_coord)
  fig.show()
  pass