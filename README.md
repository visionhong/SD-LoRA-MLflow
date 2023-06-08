### Stable Diffusion LoRA with MLflow and Ray

#### Hyper-parameter Tuning

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
  
<img width="1272" alt="mlflow-res2" src="https://github.com/visionhong/SD-LoRA-MLflow/assets/53398821/1a1eb055-0f94-49d0-9278-a3dae98d2713">

<img width="1273" alt="mlflow-res1" src="https://github.com/visionhong/SD-LoRA-MLflow/assets/53398821/84c38ca5-4768-46c0-96ad-50b531c129bf">
