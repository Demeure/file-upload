from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    # Must be replaced by your <storage_account_name>
    account_name = 'heerodjangotest'
    # Must be replaced by your <storage_account_key>
    account_key = 'TT+cRf1FXrHTFnD31tqv9SYMOOoAS/EMu64awuwRc56uk6I0R7RrpO6+J+xg9DkwrrKRfPoZboxyMXtBovUaVQ=='
    azure_container = 'heero-local'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    # Must be replaced by your storage_account_name
    account_name = 'heerodjangotest'
    # Must be replaced by your <storage_account_key>
    account_key = 'TT+cRf1FXrHTFnD31tqv9SYMOOoAS/EMu64awuwRc56uk6I0R7RrpO6+J+xg9DkwrrKRfPoZboxyMXtBovUaVQ=='
    azure_container = 'heero-local'
    expiration_secs = None
