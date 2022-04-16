
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape

def main():
    src_dir = "src"
    templates_dir = "templates"
    env = Environment(
        loader=FileSystemLoader([src_dir, templates_dir]),
        autoescape=select_autoescape()
    )
    target_dir = "docs"
    templates = env.list_templates()
    render_list = []
    for template_name in templates:
        template = env.get_template(template_name)
        if template.filename.startswith(f"{src_dir}/"):
            # Find templates for rendering the heirarchy
            render_list.append(template)

    for template in render_list:
        path = template.filename.replace(f"{src_dir}/", "")
        target_path = f"{target_dir}/{path}"
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, "w") as f:
            f.write(template.render())

if __name__ == "__main__":
    main()
