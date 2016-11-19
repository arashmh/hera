'''
    The Hera Callback
'''


from __future__ import absolute_import

import json

from keras.callbacks import Callback
from heraspy.util import to_jsonable_dict

from heraspy.events import (
    TRAIN_BEGIN, TRAIN_END,
    EPOCH_BEGIN, EPOCH_END,
    BATCH_BEGIN, BATCH_END
)

class HeraCallback(Callback):


    '''
        A Keras callback streaming data to a hera socket server
    '''

    def __init__(
            self,
            namespace,
            hera_config,
            dispatch_message
        ):

        self.dispatch_message = dispatch_message
        self.namespace = namespace
        self.model_config = model_config
        self.server_address = get_server_url(hera_config)

        super(HeraCallback, self).__init__()

    def on_train_begin(self, *args):

        self.dispatch_message(
            self.namespace,
            TRAIN_BEGIN,
            {
                'trainConfig': self.params,
                'modelJson': json.loads(self.model.to_json()),
            }
        )


    def on_train_end(self, *args):

        self.dispatch_message(
            self.namespace,
            TRAIN_END
        )


    def on_epoch_begin(self, *args):

        self.dispatch_message(
            self.namespace,
            EPOCH_BEGIN
        )

    def on_epoch_end(self, *args):
        self.dispatch_message(
            self.namespace,
            EPOCH_END,
            {
                'logs': to_jsonable_dict(logs),
            }
        )

    def on_batch_begin(self, *args):
        self.dispatch_message(
            self.namespace,
            BATCH_BEGIN,
            {
                'data': 1,
            }
        )


    def on_batch_end(self, *args):
        self.dispatch_message(
            self.namespace,
            BATCH_END,
            {
                'data': 1,
            }
        )
