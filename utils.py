prefix = "https://github.com/ndhieunguyen/accomplishment/blob/main/images/"


def make_clickable(link: str):
    return f'<a target="_blank" href="{prefix+link}">{"View"}</a>'


def create_clickable_link(name: str, link: str):
    if not link.startswith("https"):
        link = prefix + link
    return f'<a target="_blank" href="{link}">{name}</a>'
