class TriggerPassthroughNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "image": ("IMAGE",),
                "text": ("STRING",),
                "trigger": ("STRING", {"default": "Triggering next..."}),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING", "STRING")
    FUNCTION = "pass_through"
    CATEGORY = "Zygion Custom Nodes"

    def pass_through(self, image, text, trigger):
        return (image, text, trigger)
