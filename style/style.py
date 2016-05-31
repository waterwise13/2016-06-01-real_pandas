from IPython.core.display import HTML
css = open('/Users/Neuromancer/style/style-table.css').read() + open('/Users/Neuromancer/style/style-notebook.css').read()
HTML('<style>{}</style>'.format(css))