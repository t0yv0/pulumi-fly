// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Fly.Inputs
{

    public sealed class MachineServicePortArgs : global::Pulumi.ResourceArgs
    {
        [Input("handlers")]
        private InputList<string>? _handlers;
        public InputList<string> Handlers
        {
            get => _handlers ?? (_handlers = new InputList<string>());
            set => _handlers = value;
        }

        [Input("port", required: true)]
        public Input<int> Port { get; set; } = null!;

        public MachineServicePortArgs()
        {
        }
        public static new MachineServicePortArgs Empty => new MachineServicePortArgs();
    }
}
