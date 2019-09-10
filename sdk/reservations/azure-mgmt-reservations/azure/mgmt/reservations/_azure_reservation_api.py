# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import AzureReservationAPIConfiguration
from .operations import AzureReservationAPIOperationsMixin
from .operations import ReservationOperations
from .operations import ReservationOrderOperations
from .operations import OperationOperations
from . import models


class AzureReservationAPI(AzureReservationAPIOperationsMixin, SDKClient):
    """This API describe Azure Reservation

    :ivar config: Configuration for client.
    :vartype config: AzureReservationAPIConfiguration

    :ivar reservation: Reservation operations
    :vartype reservation: azure.mgmt.reservations.operations.ReservationOperations
    :ivar reservation_order: ReservationOrder operations
    :vartype reservation_order: azure.mgmt.reservations.operations.ReservationOrderOperations
    :ivar operation: Operation operations
    :vartype operation: azure.mgmt.reservations.operations.OperationOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = AzureReservationAPIConfiguration(credentials, base_url)
        super(AzureReservationAPI, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-04-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.reservation = ReservationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.reservation_order = ReservationOrderOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self.config, self._serialize, self._deserialize)