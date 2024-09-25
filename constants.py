"""_summary_
"""
import pluggy

PROJECT_NAME = "resoqu"
HOOK_NAMESPACE = "resoqu"

hook_spec = pluggy.HookspecMarker(HOOK_NAMESPACE)
hook_impl = pluggy.HookimplMarker(HOOK_NAMESPACE)
