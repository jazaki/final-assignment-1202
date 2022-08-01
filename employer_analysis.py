from common import bar_graph_plotter

def run_employer_analysis():

  # Determine Employers who provides mental health benefits in US
  bar_graph_plotter('state', 'benefits', 'count', 'Employers who provides mental health benefits in US')

  # Determine Employers who provides mental health benefits in World
  bar_graph_plotter('country', 'benefits', 'count', 'Employers who provides mental health benefits in World')

  # Determine Employers who discuss mental health of their employee as per wellness program in US
  bar_graph_plotter(
    'state', 'wellness_program', 'count', 'Employers who discuss mental health of their employee as per wellness program in US'
  )

  # Determine Employers who discuss mental health of their employee as per wellness program in World
  bar_graph_plotter(
    'country', 'wellness_program', 'count', 'Employers who discuss mental health of their employee as per wellness program in World'
  )

  # Determine Employers who provides resources to seek help about mental health issues in US
  bar_graph_plotter('state', 'seek_help', 'count', 'Employers who provides resources to seek help about mental health issues in US')

  # Determine Employers who provides resources to seek help about mental health issues in World
  bar_graph_plotter('country', 'seek_help', 'count', 'Employers who provides resources to seek help about mental health issues in World')

  # Determine Employers who protect anonymity of their employees having mental health issues in US
  bar_graph_plotter('state', 'anonymity', 'count', 'Employers who protect anonymity of their employees having mental health issues in US')

  # Determine Employers who protect anonymity of their employees having mental health issues in World
  bar_graph_plotter(
    'country', 'anonymity', 'count', 'Employers who protect anonymity of their employees having mental health issues in World'
  )

  # Determine Easness at which the medical leave can be takenby the employee due to mental state in uS
  bar_graph_plotter('state', 'leave', 'count', 'Easness at which the medical leave can be takenby the employee due to mental state in US')

  # Determine Easness at which the medical leave can be takenby the employee due to mental state in world
  bar_graph_plotter(
    'country', 'leave', 'count', 'Easness at which the medical leave can be takenby the employee due to mental state in world'
  )

  pass