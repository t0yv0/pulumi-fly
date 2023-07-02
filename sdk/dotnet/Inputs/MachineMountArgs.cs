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

    public sealed class MachineMountArgs : global::Pulumi.ResourceArgs
    {
        [Input("encrypted")]
        public Input<bool>? Encrypted { get; set; }

        /// <summary>
        /// Path for volume to be mounted on vm
        /// </summary>
        [Input("path", required: true)]
        public Input<string> Path { get; set; } = null!;

        [Input("sizeGb")]
        public Input<int>? SizeGb { get; set; }

        /// <summary>
        /// Name or ID of volume
        /// </summary>
        [Input("volume", required: true)]
        public Input<string> Volume { get; set; } = null!;

        public MachineMountArgs()
        {
        }
        public static new MachineMountArgs Empty => new MachineMountArgs();
    }
}
