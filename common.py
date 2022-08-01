# Function to remove all null values and plot bar graph
def df_modifier(x_coord, y_coord):
  df_non_NaN = df[df[x_coord].notnull()][[x_coord, y_coord]]
  return df_non_NaN.groupby(x_coord).filter(lambda x: len(x) > 26)
  pass

def bar_graph_plotter(x_coord, y_coord, y_label, graph_title):
  filtered_df = df_modifier(x_coord, y_coord)
  plot_df = (filtered_df.groupby(x_coord)[y_coord].value_counts(normalize=True).mul(100).round(2).sort_index()
    .to_frame(name=y_label)).reset_index()

  fig = px.bar(plot_df, x=x_coord, y=y_label, title=graph_title, color=y_coord)
  fig.show()
  pass