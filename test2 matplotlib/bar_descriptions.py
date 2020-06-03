import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Pythoon Projects'
chart.x_labels = ['system-design-primer', 'public-apis', 'models']

plot_dicts = [
    {'value': 81393, 'label': 'Description of system-design-primer.'},
    {'value': 69289, 'label': 'Description of public-apis.'},
    {'value': 61214, 'label': 'Description of models.'},
]
chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')