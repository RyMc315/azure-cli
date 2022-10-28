# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network ddos-protection update",
)
class Update(AAZCommand):
    """Update a DDoS protection plan.

    :example: Add a Vnet to a DDoS protection plan in the same subscription.
        az network ddos-protection update -g MyResourceGroup -n MyDdosPlan --vnets MyVnet

    :example: Update a DDoS protection plan. (autogenerated)
        az network ddos-protection update --name MyDdosPlan --tags foo=boo --resource-group MyResourceGroup
    """

    _aaz_info = {
        "version": "2022-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/ddosprotectionplans/{}", "2022-05-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the DDoS protection plan.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Space-separated tags: key[=value] [key[=value] ...].",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.DdosProtectionPlansGet(ctx=self.ctx)()
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        yield self.DdosProtectionPlansCreateOrUpdate(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DdosProtectionPlansGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ddosProtectionPlans/{ddosProtectionPlanName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "ddosProtectionPlanName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _build_schema_ddos_protection_plan_read(cls._schema_on_200)

            return cls._schema_on_200

    class DdosProtectionPlansCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ddosProtectionPlans/{ddosProtectionPlanName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "ddosProtectionPlanName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _build_schema_ddos_protection_plan_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("tags", AAZDictType, ".tags")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


_schema_ddos_protection_plan_read = None


def _build_schema_ddos_protection_plan_read(_schema):
    global _schema_ddos_protection_plan_read
    if _schema_ddos_protection_plan_read is not None:
        _schema.etag = _schema_ddos_protection_plan_read.etag
        _schema.id = _schema_ddos_protection_plan_read.id
        _schema.location = _schema_ddos_protection_plan_read.location
        _schema.name = _schema_ddos_protection_plan_read.name
        _schema.properties = _schema_ddos_protection_plan_read.properties
        _schema.tags = _schema_ddos_protection_plan_read.tags
        _schema.type = _schema_ddos_protection_plan_read.type
        return

    _schema_ddos_protection_plan_read = AAZObjectType()

    ddos_protection_plan_read = _schema_ddos_protection_plan_read
    ddos_protection_plan_read.etag = AAZStrType(
        flags={"read_only": True},
    )
    ddos_protection_plan_read.id = AAZStrType(
        flags={"read_only": True},
    )
    ddos_protection_plan_read.location = AAZStrType()
    ddos_protection_plan_read.name = AAZStrType(
        flags={"read_only": True},
    )
    ddos_protection_plan_read.properties = AAZObjectType(
        flags={"client_flatten": True},
    )
    ddos_protection_plan_read.tags = AAZDictType()
    ddos_protection_plan_read.type = AAZStrType(
        flags={"read_only": True},
    )

    properties = _schema_ddos_protection_plan_read.properties
    properties.provisioning_state = AAZStrType(
        serialized_name="provisioningState",
        flags={"read_only": True},
    )
    properties.public_ip_addresses = AAZListType(
        serialized_name="publicIpAddresses",
        flags={"read_only": True},
    )
    properties.resource_guid = AAZStrType(
        serialized_name="resourceGuid",
        flags={"read_only": True},
    )
    properties.virtual_networks = AAZListType(
        serialized_name="virtualNetworks",
        flags={"read_only": True},
    )

    public_ip_addresses = _schema_ddos_protection_plan_read.properties.public_ip_addresses
    public_ip_addresses.Element = AAZObjectType(
        flags={"read_only": True},
    )
    _build_schema_sub_resource_read(public_ip_addresses.Element)

    virtual_networks = _schema_ddos_protection_plan_read.properties.virtual_networks
    virtual_networks.Element = AAZObjectType(
        flags={"read_only": True},
    )
    _build_schema_sub_resource_read(virtual_networks.Element)

    tags = _schema_ddos_protection_plan_read.tags
    tags.Element = AAZStrType()

    _schema.etag = _schema_ddos_protection_plan_read.etag
    _schema.id = _schema_ddos_protection_plan_read.id
    _schema.location = _schema_ddos_protection_plan_read.location
    _schema.name = _schema_ddos_protection_plan_read.name
    _schema.properties = _schema_ddos_protection_plan_read.properties
    _schema.tags = _schema_ddos_protection_plan_read.tags
    _schema.type = _schema_ddos_protection_plan_read.type


_schema_sub_resource_read = None


def _build_schema_sub_resource_read(_schema):
    global _schema_sub_resource_read
    if _schema_sub_resource_read is not None:
        _schema.id = _schema_sub_resource_read.id
        return

    _schema_sub_resource_read = AAZObjectType(
        flags={"read_only": True}
    )

    sub_resource_read = _schema_sub_resource_read
    sub_resource_read.id = AAZStrType(
        flags={"read_only": True},
    )

    _schema.id = _schema_sub_resource_read.id


__all__ = ["Update"]
