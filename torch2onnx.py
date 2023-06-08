import torch

def export(pipeline, device, weight_dtype, onnx_path):
    
    unet_in_channels = pipeline.unet.config.in_channels
    unet_sample_size = pipeline.unet.config.sample_size
    num_tokens = pipeline.text_encoder.config.max_position_embeddings
    text_hidden_size = pipeline.text_encoder.config.hidden_size
    
    torch.onnx.export(
        pipeline.unet,  # pipeline에서 unet 모듈만 선택
        (
            torch.randn(2, unet_in_channels, unet_sample_size, unet_sample_size).to(device=device, dtype=weight_dtype),
            torch.randn(2).to(device=device, dtype=weight_dtype),
            torch.randn(2, num_tokens, text_hidden_size).to(device=device, dtype=weight_dtype),
            False
        ),
        f=onnx_path,
        input_names=["sample", "timestep", "encoder_hidden_states", "return_dict"],
        output_names=["out_sample"],
        dynamic_axes={
                "sample": {0: "example", 1: "channels", 2: "height", 3: "width"},
                "timestep": {0: "batch"},
                "encoder_hidden_states": {0: "example", 1: "sequence"},
            },
        do_constant_folding=True,
        opset_version=16)