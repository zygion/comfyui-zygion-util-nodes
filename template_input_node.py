class TemplateInputNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "template": ("STRING", {"multiline": True, "default": "Today is a {adjective} day."}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("template_out",)
    FUNCTION = "output_template"

    CATEGORY = "Zygion Custom Nodes"

    def output_template(self, template):
        return (template,)
