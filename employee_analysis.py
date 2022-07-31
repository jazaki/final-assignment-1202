from common import bar_graph_plotter

def run_employee_analysis():
  # Determining Employees seeking treatment of their mental illness in US
  bar_graph_plotter('state', 'treatment', 'count', 'Employees seeking treatment of their mental illness in US')

  # Determining Employees seeking treatment of their mental illness in World
  bar_graph_plotter('country', 'treatment', 'count', 'Employees seeking treatment of their mental illness in World')

  # Determining Employees knowing options for mental care their employer provides in US
  bar_graph_plotter('state', 'care_options', 'count', 'Employees knowing options for mental care their employer provides in US')

  # Determining Employees knowing options for mental care their employer provides in World
  bar_graph_plotter('country', 'care_options', 'count', 'Employees knowing options for mental care their employer provides in World')

  # Determining Employees comfortable discussing their mental health with their coworkers in US
  bar_graph_plotter('state', 'coworkers', 'count', 'Employees comfortable discussing their mental health with their coworkers in US')

  # Determining Employees comfortable discussing their mental health with their coworkers in World
  bar_graph_plotter('country', 'coworkers', 'count', 'Employees comfortable discussing their mental health with their coworkers in World')

  # Determining Employees comfortable discussing their mental health with their direct supervisor in US
  bar_graph_plotter(
    'state', 'supervisor', 'count', 'Employees comfortable discussing their mental health with their direct supervisor in US'
  )

  # Determining Employees comfortable discussing their mental health with their direct supervisor in World
  bar_graph_plotter(
    'country', 'coworkers', 'count', 'Employees comfortable discussing their mental health with their direct supervisor in World'
  )

  # Determining Employers who put mental health as important as physical health as per employee
  bar_graph_plotter(
    'state', 'mental_vs_physical', 'count', 'Employers who put mental health as important as physical health as per employee'
  )

  # Determining Employers who put mental health as important as physical health as per employee
  bar_graph_plotter(
    'country', 'mental_vs_physical', 'count', 'Employers who put mental health as important as physical health as per employee'
  )
  pass