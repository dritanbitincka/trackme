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

class TrackMeHandlerDataSampling_v1(rest_handler.RESTHandler):
    def __init__(self, command_line, command_arg):
        super(TrackMeHandlerDataSampling_v1, self).__init__(command_line, command_arg, logger)

    # Get the entire collection as a Python array
    def get_data_sampling_collection(self, request_info, **kwargs):

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            collection_name = "kv_trackme_data_sampling"            
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

    # Get data_name record
    def get_data_sampling_by_name(self, request_info, **kwargs):

        # By data_name
        data_name = None

        # query_string to find records
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_name = resp_dict['data_name']

        # Define the KV query
        query_string = '{ "data_name": "' + data_name + '" }'
        
        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            collection_name = "kv_trackme_data_sampling"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None

            # Render result
            if key is not None and len(key)>2:

                return {
                    "payload": json.dumps(collection.data.query_by_id(key), indent=1),
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

    # Delete a data sampling record
    def delete_data_sampling_del(self, request_info, **kwargs):

        # Declare
        data_name = None
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_name = resp_dict['data_name']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_name": "' + data_name + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_sampling"            
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
                        "change_type": "delete data sampling record",
                        "object": str(data_name),
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

    # Reset and run sampling
    def post_data_sampling_reset(self, request_info, **kwargs):

        # Declare
        data_name = None
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        data_name = resp_dict['data_name']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "data_name": "' + data_name + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_sampling"
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
                        "change_type": "data sampling clear state",
                        "object": str(data_name),
                        "object_category": "data_source",
                        "object_attrs": str(record),
                        "result": "N/A",
                        "comment": str(update_comment)
                        }))

                except Exception as e:
                    return {
                        'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
                    }

                # Run and update sampling
                data_sample_status_colour = "unknown"

                import splunklib.results as results

                kwargs_search = {"app": "trackme", "earliest_time": "-7d", "latest_time": "now"}
                searchquery = "| savedsearch \"TrackMe - Data sampling engine for target\" key=\"" + str(key) + "\""

                # spawn the search and get the results
                searchresults = service.jobs.oneshot(searchquery, **kwargs_search)

                # Get the results and display them using the ResultsReader
                try:
                    reader = results.ResultsReader(searchresults)
                    for item in reader:
                        query_result = item
                    data_sample_status_colour = query_result["data_sample_status_colour"]

                except Exception as e:
                    data_sample_status_colour = "unknown"

                return {
                    "payload": "Data sampling state for: " + str(data_name) + " was cleared and sampling operation ran, data sampling state is: " + str(data_sample_status_colour),
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

    # Get the entire collection as a Python array
    def get_data_sampling_models(self, request_info, **kwargs):

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            collection_name = "kv_trackme_data_sampling_custom_models"            
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


    # Get model
    def get_data_sampling_models_by_name(self, request_info, **kwargs):

        # By model_name
        model_name = None

        # query_string to find records
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        model_name = resp_dict['model_name']

        # Define the KV query
        query_string = '{ "model_name": "' + model_name + '" }'
        
        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            collection_name = "kv_trackme_data_sampling_custom_models"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                port=splunkd_port,
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Get the current record
            # Notes: the record is returned as an array, as we search for a specific record, we expect one record only
            
            try:
                record = collection.data.query(query=str(query_string))
                key = record[0].get('_key')

            except Exception as e:
                key = None

            # Render result
            if key is not None and len(key)>2:

                return {
                    "payload": json.dumps(collection.data.query_by_id(key), indent=1),
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


    # Add new allowlist index if does not exist yet
    def post_data_sampling_models_add(self, request_info, **kwargs):

        # Declare
        model_name = None
        model_regex = None
        model_type = None

        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        model_name = resp_dict['model_name']
        model_regex = resp_dict['model_regex']
        model_type = resp_dict['model_type']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # sourcetype_scope is optional, if unset it will be defined to * (any)
        try:
            sourcetype_scope = resp_dict['sourcetype_scope']
        except Exception as e:
            sourcetype_scope = "*"

        # Define the KV query
        query_string = '{ "model_name": "' + model_name + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_sampling_custom_models"            
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
            if key is not None and len(key)>2 and model_type in("inclusive", "exclusive"):

                # This record exists already
                model_id = record[0].get('model_id')

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                # Update the record
                collection.data.update(str(key), json.dumps({"model_name": model_name, "model_regex": model_regex, "model_type": model_type, "model_id": model_id, "sourcetype_scope": sourcetype_scope, "mtime": current_time}))

                # Store the record for audit purposes
                record = str(json.dumps(collection.data.query_by_id(key), indent=1))

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add data parsing custom rule",
                        "object": str(model_name),
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

            elif model_type in("inclusive", "exclusive"):

                # This record does not exist yet

                import hashlib
                model_id = hashlib.md5(model_name.encode('utf-8')).hexdigest()

                # Record an audit change
                import time
                current_time = int(round(time.time() * 1000))
                user = "nobody"

                # Insert the record
                collection.data.insert(json.dumps({"model_name": model_name, "model_regex": model_regex, "model_type": model_type, "model_id": model_id, "sourcetype_scope": sourcetype_scope, "mtime": current_time}))

                # Get record
                record = json.dumps(collection.data.query(query=str(query_string)), indent=1)

                try:

                    # Insert the record
                    collection_audit.data.insert(json.dumps({    
                        "time": str(current_time),
                        "user": str(user),
                        "action": "success",
                        "change_type": "add data parsing custom rule",
                        "object": str(model_name),
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

                return {
                    "payload": "bad request",
                    'status': 404 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Delete a custom model
    def delete_data_sampling_models_del(self, request_info, **kwargs):

        # Declare
        model_name = None
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        model_name = resp_dict['model_name']

        # Update comment is optional and used for audit changes
        try:
            update_comment = resp_dict['update_comment']
        except Exception as e:
            update_comment = "API update"

        # Define the KV query
        query_string = '{ "model_name": "' + model_name + '" }'

        # Get splunkd port
        entity = splunk.entity.getEntity('/server', 'settings',
                                            namespace='trackme', sessionKey=request_info.session_key, owner='-')
        splunkd_port = entity['mgmtHostPort']

        try:

            # Data collection
            collection_name = "kv_trackme_data_sampling_custom_models"            
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
                        "change_type": "delete data parsing custom rule",
                        "object": str(model_name),
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
