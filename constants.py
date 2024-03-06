"""_summary_
"""
import pluggy

PROJECT_NAME = "plugin_example"
HOOK_NAMESPACE = "plugin_example"

hook_spec = pluggy.HookspecMarker(HOOK_NAMESPACE)
hook_impl = pluggy.HookimplMarker(HOOK_NAMESPACE)
