## mlflow tracking server with http basic authentication

Run the Dockerfile with the http basic authentication added in mlflow tracking server.
Check out how to use it in the blog below.

https://visionhong.github.io/aws/AWS-MLflow-SD-LoRA/{:target="_blank"}

<br>



## Stable Diffusion LoRA with MLflow and Ray

### Hyper-parameter Tuning

``` bash
export MLFLOW_TRACKING_URI="<ECS 태스크 Public IP>"
export MLFLOW_TRACKING_USERNAME="<대시보드 username>"
export MLFLOW_TRACKING_PASSWORD="<대시보드 비밀번호>"
export AWS_ACCESS_KEY_ID="<IAM 사용자 Access Key>"
export AWS_SECRET_ACCESS_KEY="<IAM 사용자 Secret Key>"
```

``` bash
python train_tune.py \
  --pretrained_model_name_or_path="stabilityai/stable-diffusion-2-1-base" \
  --dataset_name="zoheb/sketch-scene" \
  --dataloader_num_workers=8 \
  --width=256 --height=256 --center_crop --random_flip \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --max_train_steps=1000 \
  --learning_rate=1e-04 \
  --lr_scheduler="cosine" --lr_warmup_steps=0 \
  --experiments_name='sketch_ray_tune' \
  --seed=1337 \
  --mixed_precision='fp16' \
  --enable_xformers_memory_efficient_attention \
  --tune \
  --gpus_per_trial=1
  ```
  
<br>

result:

<img width="700" alt="mlflow-res2" src="https://github.com/visionhong/SD-LoRA-MLflow/assets/53398821/1a1eb055-0f94-49d0-9278-a3dae98d2713">
<img width="700" alt="mlflow-res1" src="https://github.com/visionhong/SD-LoRA-MLflow/assets/53398821/84c38ca5-4768-46c0-96ad-50b531c129bf">

<br>

### Hyper-parameter Tuning

``` bash
accelerate launch --mixed_precision="fp16" train_tune.py \
  --pretrained_model_name_or_path="stabilityai/stable-diffusion-2-1-base" \
  --dataset_name="zoheb/sketch-scene" \
  --dataloader_num_workers=8 \
  --width=256 --height=256 --center_crop --random_flip \
  --train_batch_size=2 \
  --gradient_accumulation_steps=4 \
  --num_train_epochs=10 \
  --learning_rate=1e-03 \
  --lr_scheduler="cosine" --lr_warmup_steps=500 \
  --output_dir="LoRA_sketch_output" \
  --experiments_name='sketch' \
  --checkpointing_steps=5000 \
  --validation_prompt="a man swimming in the sea" \
  --validation_epochs=1 \
  --num_validation_images=2 \
  --seed=1337 \
  --enable_xformers_memory_efficient_attention
```

<br>

result:

<img width="700" alt="mlflow-loss" src="https://github.com/visionhong/SD-LoRA-MLflow/assets/53398821/c105a27c-185d-40c8-89d8-5817e88e48a6">
<img width="700" alt="mlflow-res3" src="https://github.com/visionhong/SD-LoRA-MLflow/assets/53398821/a5298faf-9bbe-4c84-9b2b-b1fe19c84ada">




