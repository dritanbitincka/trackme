import logging
import os, sys
import splunk
import json

logger = logging.getLogger(__name__)

splunkhome = os.environ['SPLUNK_HOME']
sys.path.append(os.path.join(splunkhome, 'etc', 'apps', 'trackme', 'lib'))

import rest_handler
import splunklib.client as client

class TrackMeHandlerAck_v1(rest_handler.RESTHandler):
    def __init__(self, command_line, command_arg):
        super(TrackMeHandlerAck_v1, self).__init__(command_line, command_arg, logger)

    # Get Ack by _key
    def get_ack_by_key(self, request_info, **kwargs):

        # By object_category and object
        key = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        key = resp_dict['_key']
        
        try:

            collection_name = "kv_trackme_alerts_ack"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Get the record
            record = json.dumps(collection.data.query_by_id(key), indent=1)

            # Render result
            if record is not None and len(record)>2:
                return {
                    "payload": str(record),
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

    # Get Ack by object name
    def get_ack_by_object(self, request_info, **kwargs):

        # By object_category and object
        object_category_value = None
        object_value = None
        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        object_value = resp_dict['object']
        object_category_value = resp_dict['object_category']

        # Define the KV query
        query_string = '{ "$and": [ { "object_category": "' + object_category_value + '" }, { "object' + '": "' + object_value + '" } ] }'
        
        try:

            collection_name = "kv_trackme_alerts_ack"            
            service = client.connect(
                owner="nobody",
                app="trackme",
                token=request_info.session_key
            )
            collection = service.kvstore[collection_name]

            # Get the record
            record = json.dumps(collection.data.query(query=str(query_string)), indent=1)

            # Render result
            if record is not None and len(record)>2:
                return {
                    "payload": str(record),
                    'status': 200 # HTTP status code
                }

            else:
                return {
                    "payload": 'Warn: resource not found ' + str(query_string),
                    'status': 404 # HTTP status code
                }


        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }

    # Enable Ack by object name
    def post_ack_enable_by_object(self, request_info, **kwargs):

        # By object_category and object
        object_category_value = None
        object_value = None
        # Creating an Ack requires additional fields
        ack_period = None
        ack_mtime = None
        ack_state = None

        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        object_value = resp_dict['object']
        object_category_value = resp_dict['object_category']
        ack_period = resp_dict['ack_period']
        ack_state = "active"
        # Note: ack_mtime will be defined as the current epoch time

        # Define the KV query
        query_string = '{ "$and": [ { "object_category": "' + object_category_value + '" }, { "object' + '": "' + object_value + '" } ] }'
        
        try:

            collection_name = "kv_trackme_alerts_ack"            
            service = client.connect(
                owner="nobody",
                app="trackme",
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

            # An ack record exists already in the collection, perform an update
            import time
            ack_mtime = time.time()
            ack_expiration = ack_mtime + int(ack_period)

            # Render result
            if key is not None and len(key)>2:

                # Update the record
                collection.data.update(str(key), json.dumps({"object": object_value,
                    "object_category": object_category_value,
                    "ack_expiration": str(ack_expiration),
                    "ack_state": str(ack_state),
                    "ack_mtime": str(ack_mtime)}))

                return {
                    "payload": json.dumps(collection.data.query_by_id(key), indent=1),
                    'status': 200 # HTTP status code
                }

            else:

                # Insert the record
                collection.data.insert(json.dumps({"object": object_value,
                    "object_category": object_category_value,
                    "ack_expiration": str(ack_expiration),
                    "ack_state": str(ack_state),
                    "ack_mtime": str(ack_mtime)}))

                return {
                    "payload": json.dumps(collection.data.query(query=str(query_string)), indent=1),
                    'status': 200 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }


    # Disable Ack
    def post_ack_disable_by_object(self, request_info, **kwargs):

        # By object_category and object
        object_category_value = None
        object_value = None
        # Creating an Ack requires additional fields
        ack_expiration = "N/A"
        ack_mtime = "N/A"
        ack_state = "inactive"

        query_string = None

        # Retrieve from data
        resp_dict = json.loads(str(request_info.raw_args['payload']))
        object_value = resp_dict['object']
        object_category_value = resp_dict['object_category']

        # Define the KV query
        query_string = '{ "$and": [ { "object_category": "' + object_category_value + '" }, { "object' + '": "' + object_value + '" } ] }'
        
        try:

            collection_name = "kv_trackme_alerts_ack"            
            service = client.connect(
                owner="nobody",
                app="trackme",
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

            # An ack record exists already in the collection, perform an update
            import time
            ack_mtime = time.time()

            # Render result
            if key is not None and len(key)>2:

                # Update the record
                collection.data.update(str(key), json.dumps({"object": object_value,
                    "object_category": object_category_value,
                    "ack_expiration": str(ack_expiration),
                    "ack_state": str(ack_state),
                    "ack_mtime": str(ack_mtime)}))

                return {
                    "payload": json.dumps(collection.data.query_by_id(key), indent=1),
                    'status': 200 # HTTP status code
                }

            else:

                # Insert the record
                collection.data.insert(json.dumps({"object": object_value,
                    "object_category": object_category_value,
                    "ack_expiration": str(ack_expiration),
                    "ack_state": str(ack_state),
                    "ack_mtime": str(ack_mtime)}))

                return {
                    "payload": json.dumps(collection.data.query(query=str(query_string)), indent=1),
                    'status': 200 # HTTP status code
                }

        except Exception as e:
            return {
                'payload': 'Warn: exception encountered: ' + str(e) # Payload of the request.
            }
