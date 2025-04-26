import json

class SceneQueueNode:
    def __init__(self):
        self.last_json = None
        self.transcript_queue = []
        self.imageprompt_queue = []

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scene_json": ("STRING", {"multiline": True}),
                "trigger": ("STRING", {"default": ""}),  
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "pop_from_queue"
    CATEGORY = "Zygion Custom Nodes"

    def pop_from_queue(self, scene_json, queue_name, default_queue_name):
        if scene_json != self.last_json:
            try:
                data = json.loads(scene_json)
                scenes = data.get("scenes", [])
                self.transcript_queue = [s.get("transcript", "") for s in scenes]
                self.imageprompt_queue = [s.get("image_prompt", "") for s in scenes]
                self.last_json = scene_json
                if (default_queue_name == 'transcript'):
                    return (self.transcript_queue.pop(0) if self.transcript_queue else {},)
                return (self.imageprompt_queue.pop(0) if self.imageprompt_queue else {},)
            except Exception as e:
                return (f"JSON error: {e}",)
        
        queue = self.imageprompt_queue
        if (queue_name == "transcript"):
            queue = self.transcript_queue
        if (queue == None or queue.count == 0):
            return {}
        return queue.pop(0)
