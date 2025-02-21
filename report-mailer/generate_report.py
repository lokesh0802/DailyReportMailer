from jinja2 import Environment, FileSystemLoader

def generate_html_report(data):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")
    return template.render(data=data)  # Render template with data
