# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AppArgs', 'App']

@pulumi.input_type
class AppArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 org: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a App resource.
        :param pulumi.Input[str] name: Name of application
        :param pulumi.Input[str] org: Optional org slug to operate upon
        """
        pulumi.set(__self__, "name", name)
        if org is not None:
            pulumi.set(__self__, "org", org)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of application
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def org(self) -> Optional[pulumi.Input[str]]:
        """
        Optional org slug to operate upon
        """
        return pulumi.get(self, "org")

    @org.setter
    def org(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org", value)


@pulumi.input_type
class _AppState:
    def __init__(__self__, *,
                 appurl: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org: Optional[pulumi.Input[str]] = None,
                 orgid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering App resources.
        :param pulumi.Input[str] appurl: readonly appUrl
        :param pulumi.Input[str] name: Name of application
        :param pulumi.Input[str] org: Optional org slug to operate upon
        :param pulumi.Input[str] orgid: readonly orgid
        """
        if appurl is not None:
            pulumi.set(__self__, "appurl", appurl)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org is not None:
            pulumi.set(__self__, "org", org)
        if orgid is not None:
            pulumi.set(__self__, "orgid", orgid)

    @property
    @pulumi.getter
    def appurl(self) -> Optional[pulumi.Input[str]]:
        """
        readonly appUrl
        """
        return pulumi.get(self, "appurl")

    @appurl.setter
    def appurl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "appurl", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of application
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def org(self) -> Optional[pulumi.Input[str]]:
        """
        Optional org slug to operate upon
        """
        return pulumi.get(self, "org")

    @org.setter
    def org(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org", value)

    @property
    @pulumi.getter
    def orgid(self) -> Optional[pulumi.Input[str]]:
        """
        readonly orgid
        """
        return pulumi.get(self, "orgid")

    @orgid.setter
    def orgid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "orgid", value)


class App(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Fly app resource

        ## Example Usage

        ## Import

        <break><break>```sh<break> $ pulumi import fly:index/app:App exampleApp <app_id> <break>```<break><break>

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of application
        :param pulumi.Input[str] org: Optional org slug to operate upon
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Fly app resource

        ## Example Usage

        ## Import

        <break><break>```sh<break> $ pulumi import fly:index/app:App exampleApp <app_id> <break>```<break><break>

        :param str resource_name: The name of the resource.
        :param AppArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppArgs.__new__(AppArgs)

            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["org"] = org
            __props__.__dict__["appurl"] = None
            __props__.__dict__["orgid"] = None
        super(App, __self__).__init__(
            'fly:index/app:App',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            appurl: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            org: Optional[pulumi.Input[str]] = None,
            orgid: Optional[pulumi.Input[str]] = None) -> 'App':
        """
        Get an existing App resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] appurl: readonly appUrl
        :param pulumi.Input[str] name: Name of application
        :param pulumi.Input[str] org: Optional org slug to operate upon
        :param pulumi.Input[str] orgid: readonly orgid
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AppState.__new__(_AppState)

        __props__.__dict__["appurl"] = appurl
        __props__.__dict__["name"] = name
        __props__.__dict__["org"] = org
        __props__.__dict__["orgid"] = orgid
        return App(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def appurl(self) -> pulumi.Output[str]:
        """
        readonly appUrl
        """
        return pulumi.get(self, "appurl")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of application
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def org(self) -> pulumi.Output[str]:
        """
        Optional org slug to operate upon
        """
        return pulumi.get(self, "org")

    @property
    @pulumi.getter
    def orgid(self) -> pulumi.Output[str]:
        """
        readonly orgid
        """
        return pulumi.get(self, "orgid")

