# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['VolumeArgs', 'Volume']

@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *,
                 app: pulumi.Input[str],
                 name: pulumi.Input[str],
                 region: pulumi.Input[str],
                 size: pulumi.Input[int]):
        """
        The set of arguments for constructing a Volume resource.
        :param pulumi.Input[str] app: Name of app to attach to
        :param pulumi.Input[str] name: name
        :param pulumi.Input[str] region: region
        :param pulumi.Input[int] size: Size of volume in GB
        """
        pulumi.set(__self__, "app", app)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter
    def app(self) -> pulumi.Input[str]:
        """
        Name of app to attach to
        """
        return pulumi.get(self, "app")

    @app.setter
    def app(self, value: pulumi.Input[str]):
        pulumi.set(self, "app", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        region
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[int]:
        """
        Size of volume in GB
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[int]):
        pulumi.set(self, "size", value)


@pulumi.input_type
class _VolumeState:
    def __init__(__self__, *,
                 app: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Volume resources.
        :param pulumi.Input[str] app: Name of app to attach to
        :param pulumi.Input[str] name: name
        :param pulumi.Input[str] region: region
        :param pulumi.Input[int] size: Size of volume in GB
        """
        if app is not None:
            pulumi.set(__self__, "app", app)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if size is not None:
            pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter
    def app(self) -> Optional[pulumi.Input[str]]:
        """
        Name of app to attach to
        """
        return pulumi.get(self, "app")

    @app.setter
    def app(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        region
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        Size of volume in GB
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)


class Volume(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Fly volume resource

        ## Example Usage

        ## Import

        <break><break>```sh<break> $ pulumi import fly:index/volume:Volume exampleApp <app_id>,<volume_internal_id> <break>```<break><break>

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app: Name of app to attach to
        :param pulumi.Input[str] name: name
        :param pulumi.Input[str] region: region
        :param pulumi.Input[int] size: Size of volume in GB
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Fly volume resource

        ## Example Usage

        ## Import

        <break><break>```sh<break> $ pulumi import fly:index/volume:Volume exampleApp <app_id>,<volume_internal_id> <break>```<break><break>

        :param str resource_name: The name of the resource.
        :param VolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeArgs.__new__(VolumeArgs)

            if app is None and not opts.urn:
                raise TypeError("Missing required property 'app'")
            __props__.__dict__["app"] = app
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            if size is None and not opts.urn:
                raise TypeError("Missing required property 'size'")
            __props__.__dict__["size"] = size
        super(Volume, __self__).__init__(
            'fly:index/volume:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app: Name of app to attach to
        :param pulumi.Input[str] name: name
        :param pulumi.Input[str] region: region
        :param pulumi.Input[int] size: Size of volume in GB
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VolumeState.__new__(_VolumeState)

        __props__.__dict__["app"] = app
        __props__.__dict__["name"] = name
        __props__.__dict__["region"] = region
        __props__.__dict__["size"] = size
        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def app(self) -> pulumi.Output[str]:
        """
        Name of app to attach to
        """
        return pulumi.get(self, "app")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        region
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        Size of volume in GB
        """
        return pulumi.get(self, "size")

