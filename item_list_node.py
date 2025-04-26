class ItemListNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING", {"default": "adjective"}),
                "items": ("STRING", {
                    "multiline": True,
                    "default": "sunny\ncloudy\nrainy"
                }),
            }
        }

    RETURN_TYPES = ("LIST",)
    RETURN_NAMES = ("var",)
    FUNCTION = "generate"

    CATEGORY = "Zygion Custom Nodes"

    def generate(self, name, items):
        item_list = [item.strip() for item in items.splitlines() if item.strip()]
        return ([{"name": name, "items": item_list}],)
