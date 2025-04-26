from .item_list_node import ItemListNode
from .template_input_node import TemplateInputNode
from .template_processor_node import TemplateProcessorNode
from .scene_queue_node import SceneQueueNode
from .trigger_passthrough_node import TriggerPassthroughNode

NODE_CLASS_MAPPINGS = {
    "ItemListNode": ItemListNode,
    "TemplateInputNode": TemplateInputNode,
    "TemplateProcessorNode": TemplateProcessorNode,
    "SceneQueueNode": SceneQueueNode,
    "TriggerPassthroughNode": TriggerPassthroughNode,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ItemListNode": "Item List",
    "TemplateInputNode": "Template Input",
    "TemplateProcessorNode": "Template Processor",
    "SceneQueueNode": "Scene Queue Node",
    "TriggerPassthroughNode": "Trigger Passthrough Node",
}
