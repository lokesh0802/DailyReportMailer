from jinja2 import Environment, FileSystemLoader

def generate_html_report(client_records):
    
    if not client_records:
        return None
    
    env = Environment(loader=FileSystemLoader("templates"))
    
    env.globals.update(zip=zip, enumerate=enumerate, len=len)
    
    template = env.get_template("report_template.html")
    
    return template.render(data=client_records[0])
