import logging
import os, sys
import splunk
import splunk.entity
import splunk.Intersplunk
import json

logger = logging.getLogger(__name__)

splunkhome = os.environ['SPLUNK_HOME']
sys.path.append(os.path.join(splunkhome, 'etc', 'apps', 'trackme', 'lib'))

import rest_handler
import splunklib.client as client

class TrackMeHandlerBlockList_v1(rest_handler.RESTHandler):
    def __init__(self, command_line, command_arg):
        super(TrackMeHandlerBlockList_v1, self).__init__(command_line, command_arg, logger)

    # Get the entire collection as a Python array
    def get_blocklist_ds_host(self, request_info, **kwargs):

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            collection_name = "kv_trackme_data_source_monitoring_blacklist_host"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Render
            return {
                "payload": json.dumps(collection.data.query(), indent=1),
                'status': 200 # HTTP status code
            }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Get the entire collection as a Python array
    def get_blocklist_ds_index(self, request_info, **kwargs):

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            collection_name = "kv_trackme_data_source_monitoring_blacklist_index"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Render
            return {
                "payload": json.dumps(collection.data.query(), indent=1),
                'status': 200 # HTTP status code
            }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Get the entire collection as a Python array
    def get_blocklist_ds_sourcetype(self, request_info, **kwargs):

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            collection_name = "kv_trackme_data_source_monitoring_blacklist_sourcetype"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Render
            return {
                "payload": json.dumps(collection.data.query(), indent=1),
                'status': 200 # HTTP status code
            }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Get the entire collection as a Python array
    def get_blocklist_dh_host(self, request_info, **kwargs):

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            collection_name = "kv_trackme_data_host_monitoring_blacklist_host"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Render
            return {
                "payload": json.dumps(collection.data.query(), indent=1),
                'status': 200 # HTTP status code
            }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Get the entire collection as a Python array
    def get_blocklist_dh_index(self, request_info, **kwargs):

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            collection_name = "kv_trackme_data_host_monitoring_blacklist_index"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Render
            return {
                "payload": json.dumps(collection.data.query(), indent=1),
                'status': 200 # HTTP status code
            }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Get the entire collection as a Python array
    def get_blocklist_dh_sourcetype(self, request_info, **kwargs):

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            collection_name = "kv_trackme_data_host_monitoring_blacklist_sourcetype"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Render
            return {
                "payload": json.dumps(collection.data.query(), indent=1),
                'status': 200 # HTTP status code
            }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Get the entire collection as a Python array
    def get_blocklist_mh_host(self, request_info, **kwargs):

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            collection_name = "kv_trackme_metric_host_monitoring_blacklist_host"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Render
            return {
                "payload": json.dumps(collection.data.query(), indent=1),
                'status': 200 # HTTP status code
            }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Get the entire collection as a Python array
    def get_blocklist_mh_index(self, request_info, **kwargs):

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            collection_name = "kv_trackme_metric_host_monitoring_blacklist_index"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Render
            return {
                "payload": json.dumps(collection.data.query(), indent=1),
                'status': 200 # HTTP status code
            }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Get the entire collection as a Python array
    def get_blocklist_mh_metric_category(self, request_info, **kwargs):

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            collection_name = "kv_trackme_metric_host_monitoring_blacklist_metric_category"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Render
            return {
                "payload": json.dumps(collection.data.query(), indent=1),
                'status': 200 # HTTP status code
            }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }

    # Add new blocklist index if does not exist yet
    def post_blocklist_ds_host_add(self, request_info, **kwargs):

        # Declare
        data_host = None
        query_string = None
        data_blacklist_state = "true"

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_host = resp_dict['data_host']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_host": "' + data_host + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_source_monitoring_blacklist_host"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist host",
                        "object": str(data_host),
                        "object_category": "data_source",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

            else:

                # This record does not exist yet

                # Insert the record
                collection.data.insert(json.dumps({"data_host": data_host, "data_blacklist_state": data_blacklist_state}))

                # Get record
                record = json.dumps(collection.data.query(query=str(query_string)), indent=1)

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist host",
                        "object": str(data_host),
                        "object_category": "data_source",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }

    # Add new blocklist index if does not exist yet
    def post_blocklist_ds_index_add(self, request_info, **kwargs):

        # Declare
        data_index = None
        query_string = None
        data_blacklist_state = "true"

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_index = resp_dict['data_index']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_index": "' + data_index + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_source_monitoring_blacklist_index"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist index",
                        "object": str(data_index),
                        "object_category": "data_source",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

            else:

                # This record does not exist yet

                # Insert the record
                collection.data.insert(json.dumps({"data_index": data_index, "data_blacklist_state": data_blacklist_state}))

                # Get record
                record = json.dumps(collection.data.query(query=str(query_string)), indent=1)

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist index",
                        "object": str(data_index),
                        "object_category": "data_source",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Add new blocklist index if does not exist yet
    def post_blocklist_ds_sourcetype_add(self, request_info, **kwargs):

        # Declare
        data_sourcetype = None
        query_string = None
        data_blacklist_state = "true"

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_sourcetype = resp_dict['data_sourcetype']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_sourcetype": "' + data_sourcetype + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_source_monitoring_blacklist_sourcetype"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist sourcetype",
                        "object": str(data_sourcetype),
                        "object_category": "data_source",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

            else:

                # This record does not exist yet

                # Insert the record
                collection.data.insert(json.dumps({"data_sourcetype": data_sourcetype, "data_blacklist_state": data_blacklist_state}))

                # Get record
                record = json.dumps(collection.data.query(query=str(query_string)), indent=1)

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist sourcetype",
                        "object": str(data_sourcetype),
                        "object_category": "data_source",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Add new blocklist index if does not exist yet
    def delete_blocklist_ds_host_del(self, request_info, **kwargs):

        # Declare
        data_host = None
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_host = resp_dict['data_host']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_host": "' + data_host + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_source_monitoring_blacklist_host"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Remove the record
                    collection.data.delete(json.dumps({"_key":key}))

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "delete blocklist host",
                        "object": str(data_host),
                        "object_category": "data_source",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": "Record with _key " + str(key) + " was deleted from the collection.",
                    'status': 200 # HTTP status code
                }

            else:

                return {
                    "payload": 'Warn: resource not found ' + str(key),
                    'status': 404 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Add new blocklist index if does not exist yet
    def delete_blocklist_ds_index_del(self, request_info, **kwargs):

        # Declare
        data_index = None
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_index = resp_dict['data_index']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_index": "' + data_index + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_source_monitoring_blacklist_index"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Remove the record
                    collection.data.delete(json.dumps({"_key":key}))

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "delete blocklist index",
                        "object": str(data_index),
                        "object_category": "data_source",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": "Record with _key " + str(key) + " was deleted from the collection.",
                    'status': 200 # HTTP status code
                }

            else:

                return {
                    "payload": 'Warn: resource not found ' + str(key),
                    'status': 404 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Add new blocklist index if does not exist yet
    def delete_blocklist_ds_sourcetype_del(self, request_info, **kwargs):

        # Declare
        data_sourcetype = None
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_sourcetype = resp_dict['data_sourcetype']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_sourcetype": "' + data_sourcetype + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_source_monitoring_blacklist_sourcetype"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Remove the record
                    collection.data.delete(json.dumps({"_key":key}))

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "delete blocklist sourcetype",
                        "object": str(data_sourcetype),
                        "object_category": "data_source",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": "Record with _key " + str(key) + " was deleted from the collection.",
                    'status': 200 # HTTP status code
                }

            else:

                return {
                    "payload": 'Warn: resource not found ' + str(key),
                    'status': 404 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }

    # Add new blocklist index if does not exist yet
    def post_blocklist_dh_host_add(self, request_info, **kwargs):

        # Declare
        data_host = None
        query_string = None
        data_blacklist_state = "true"

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_host = resp_dict['data_host']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_host": "' + data_host + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_host_monitoring_blacklist_host"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist host",
                        "object": str(data_host),
                        "object_category": "data_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

            else:

                # This record does not exist yet

                # Insert the record
                collection.data.insert(json.dumps({"data_host": data_host, "data_blacklist_state": data_blacklist_state}))

                # Get record
                record = json.dumps(collection.data.query(query=str(query_string)), indent=1)

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist host",
                        "object": str(data_host),
                        "object_category": "data_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }

    # Add new blocklist index if does not exist yet
    def post_blocklist_dh_index_add(self, request_info, **kwargs):

        # Declare
        data_index = None
        query_string = None
        data_blacklist_state = "true"

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_index = resp_dict['data_index']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_index": "' + data_index + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_host_monitoring_blacklist_index"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist index",
                        "object": str(data_index),
                        "object_category": "data_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

            else:

                # This record does not exist yet

                # Insert the record
                collection.data.insert(json.dumps({"data_index": data_index, "data_blacklist_state": data_blacklist_state}))

                # Get record
                record = json.dumps(collection.data.query(query=str(query_string)), indent=1)

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist index",
                        "object": str(data_index),
                        "object_category": "data_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Add new blocklist index if does not exist yet
    def post_blocklist_dh_sourcetype_add(self, request_info, **kwargs):

        # Declare
        data_sourcetype = None
        query_string = None
        data_blacklist_state = "true"

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_sourcetype = resp_dict['data_sourcetype']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_sourcetype": "' + data_sourcetype + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_host_monitoring_blacklist_sourcetype"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist sourcetype",
                        "object": str(data_sourcetype),
                        "object_category": "data_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

            else:

                # This record does not exist yet

                # Insert the record
                collection.data.insert(json.dumps({"data_sourcetype": data_sourcetype, "data_blacklist_state": data_blacklist_state}))

                # Get record
                record = json.dumps(collection.data.query(query=str(query_string)), indent=1)

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist sourcetype",
                        "object": str(data_sourcetype),
                        "object_category": "data_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Add new blocklist index if does not exist yet
    def delete_blocklist_dh_host_del(self, request_info, **kwargs):

        # Declare
        data_host = None
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_host = resp_dict['data_host']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_host": "' + data_host + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_host_monitoring_blacklist_host"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Remove the record
                    collection.data.delete(json.dumps({"_key":key}))

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "delete blocklist host",
                        "object": str(data_host),
                        "object_category": "data_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": "Record with _key " + str(key) + " was deleted from the collection.",
                    'status': 200 # HTTP status code
                }

            else:

                return {
                    "payload": 'Warn: resource not found ' + str(key),
                    'status': 404 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Add new blocklist index if does not exist yet
    def delete_blocklist_dh_index_del(self, request_info, **kwargs):

        # Declare
        data_index = None
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_index = resp_dict['data_index']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_index": "' + data_index + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_host_monitoring_blacklist_index"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Remove the record
                    collection.data.delete(json.dumps({"_key":key}))

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "delete blocklist index",
                        "object": str(data_index),
                        "object_category": "data_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": "Record with _key " + str(key) + " was deleted from the collection.",
                    'status': 200 # HTTP status code
                }

            else:

                return {
                    "payload": 'Warn: resource not found ' + str(key),
                    'status': 404 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Add new blocklist index if does not exist yet
    def delete_blocklist_dh_sourcetype_del(self, request_info, **kwargs):

        # Declare
        data_sourcetype = None
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_sourcetype = resp_dict['data_sourcetype']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_sourcetype": "' + data_sourcetype + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_host_monitoring_blacklist_sourcetype"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Remove the record
                    collection.data.delete(json.dumps({"_key":key}))

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "delete blocklist sourcetype",
                        "object": str(data_sourcetype),
                        "object_category": "data_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": "Record with _key " + str(key) + " was deleted from the collection.",
                    'status': 200 # HTTP status code
                }

            else:

                return {
                    "payload": 'Warn: resource not found ' + str(key),
                    'status': 404 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }

    # Add new blocklist index if does not exist yet
    def post_blocklist_mh_host_add(self, request_info, **kwargs):

        # Declare
        metric_host = None
        query_string = None
        data_blacklist_state = "true"

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        metric_host = resp_dict['metric_host']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "metric_host": "' + metric_host + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_metric_host_monitoring_blacklist_host"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist host",
                        "object": str(metric_host),
                        "object_category": "metric_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

            else:

                # This record does not exist yet

                # Insert the record
                collection.data.insert(json.dumps({"metric_host": metric_host, "data_blacklist_state": data_blacklist_state}))

                # Get record
                record = json.dumps(collection.data.query(query=str(query_string)), indent=1)

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist host",
                        "object": str(metric_host),
                        "object_category": "metric_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }

    # Add new blocklist index if does not exist yet
    def post_blocklist_mh_index_add(self, request_info, **kwargs):

        # Declare
        metric_index = None
        query_string = None
        data_blacklist_state = "true"

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        metric_index = resp_dict['metric_index']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "metric_index": "' + metric_index + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_metric_host_monitoring_blacklist_index"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist index",
                        "object": str(metric_index),
                        "object_category": "metric_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

            else:

                # This record does not exist yet

                # Insert the record
                collection.data.insert(json.dumps({"metric_index": metric_index, "data_blacklist_state": data_blacklist_state}))

                # Get record
                record = json.dumps(collection.data.query(query=str(query_string)), indent=1)

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist index",
                        "object": str(metric_index),
                        "object_category": "metric_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Add new blocklist index if does not exist yet
    def post_blocklist_mh_metric_category_add(self, request_info, **kwargs):

        # Declare
        metric_category = None
        query_string = None
        data_blacklist_state = "true"

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        metric_category = resp_dict['metric_category']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "metric_category": "' + metric_category + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_metric_host_monitoring_blacklist_metric_category"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist metric_category",
                        "object": str(metric_category),
                        "object_category": "metric_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

            else:

                # This record does not exist yet

                # Insert the record
                collection.data.insert(json.dumps({"metric_category": metric_category, "data_blacklist_state": data_blacklist_state}))

                # Get record
                record = json.dumps(collection.data.query(query=str(query_string)), indent=1)

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add blocklist metric_category",
                        "object": str(metric_category),
                        "object_category": "metric_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Add new blocklist index if does not exist yet
    def delete_blocklist_mh_host_del(self, request_info, **kwargs):

        # Declare
        metric_host = None
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        metric_host = resp_dict['metric_host']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "metric_host": "' + metric_host + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_metric_host_monitoring_blacklist_host"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Remove the record
                    collection.data.delete(json.dumps({"_key":key}))

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "delete blocklist host",
                        "object": str(metric_host),
                        "object_category": "metric_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": "Record with _key " + str(key) + " was deleted from the collection.",
                    'status': 200 # HTTP status code
                }

            else:

                return {
                    "payload": 'Warn: resource not found ' + str(key),
                    'status': 404 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Add new blocklist index if does not exist yet
    def delete_blocklist_mh_index_del(self, request_info, **kwargs):

        # Declare
        metric_index = None
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        metric_index = resp_dict['metric_index']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "metric_index": "' + metric_index + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_metric_host_monitoring_blacklist_index"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Remove the record
                    collection.data.delete(json.dumps({"_key":key}))

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "delete blocklist index",
                        "object": str(metric_index),
                        "object_category": "metric_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": "Record with _key " + str(key) + " was deleted from the collection.",
                    'status': 200 # HTTP status code
                }

            else:

                return {
                    "payload": 'Warn: resource not found ' + str(key),
                    'status': 404 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Add new blocklist index if does not exist yet
    def delete_blocklist_mh_metric_category_del(self, request_info, **kwargs):

        # Declare
        metric_category = None
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        metric_category = resp_dict['metric_category']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "metric_category": "' + metric_category + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_metric_host_monitoring_blacklist_metric_category"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Audit collection
            collection_name_audit = "kv_trackme_audit_changes"            
            service_audit = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection_audit = service_audit.kvstore[collection_name_audit]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None
                
            # Render result
            if key is not None and len(key)>2:

                # This record exists already

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                try:

                    # Remove the record
                    collection.data.delete(json.dumps({"_key":key}))

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "delete blocklist metric_category",
                        "object": str(metric_category),
                        "object_category": "metric_host",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                return {
                    "payload": "Record with _key " + str(key) + " was deleted from the collection.",
                    'status': 200 # HTTP status code
                }

            else:

                return {
                    "payload": 'Warn: resource not found ' + str(key),
                    'status': 404 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }

