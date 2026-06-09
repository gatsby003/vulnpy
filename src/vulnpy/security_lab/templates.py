from string import Template


def render_preview_template(template_text, values):
    return Template(template_text).safe_substitute(values)


def render_admin_banner(user_input):
    return "<section class='admin-banner'>{}</section>".format(user_input)


def render_inline_script(script_body):
    return "<script>{}</script>".format(script_body)
