config = {'service_container': {}, 'router': {'rules': [{'regex': '^\\/(?P<user>[^/]+?)$', 'module': 'resources.lib.app.settings', 'target': 'Settings:show_settings', 'rule': '/<user>'}, {'regex': '^\\/$', 'module': 'resources.lib.app.settings', 'target': 'Settings:show_settings', 'rule': '/'}]}, 'plugin': {'name': 'plugin.audio.deezer', 'env': 'dev'}}