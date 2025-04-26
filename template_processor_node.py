import random

class TemplateProcessorNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "template": ("STRING", {}),
                "vars": ("LIST",),
                "trigger": ("FLOAT", {"default": 0.0})  # Added dummy input
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    FUNCTION = "process"

    CATEGORY = "Zygion Custom Nodes"

    def process(self, template, vars, trigger):
        var_map = {}
        for var in vars:
            name = var.get("name")
            items = var.get("items", [])
            if name and items:
                var_map[name] = random.choice(items)

        for key, val in var_map.items():
            template = template.replace(f"{{{key}}}", val)

        return (template,)
