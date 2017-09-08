# Google Cloud ML Engineのメモリを調べてみた

https://cloud.google.com/ml-engine/docs/concepts/training-overview

> Even though the exact specifications of the machine types are subject to change at any time, you can compare them in terms of relative capability. The following table uses rough "t-shirt" sizing to describe the machine types.

ココらへんがいまいち曖昧なので調べてみた


# Results

Scale tier

## BASIC
- single
  - 14.6924285889GB

## STANDARD_1
- single
  - 7.01322555542GB
- master
  - 7.01322555542GB
- ps
  - 14.6924285889GB
- worker
  - 7.01322555542GB

## PREMIUM_1
- single
  - 14.0992164612GB
- master
  - 14.0992164612GB
- ps
  - 51.1138572693GB
- worker
  - 14.0992164612GB

## BASIC_GPU
- single
 - 29.4575538635GB

# CUSTOM

Machine type

## standard
- 14.6924285889GB

## large_model
- 51.1138572693GB

## complex_model_s
- 7.01327514648GB

## complex_model_m
- 14.0991668701GB

## complex_model_l
- 28.272064209GB

## standard_gpu
- 29.4575538635GB

## complex_model_m_gpu
- 118.048339844GB

## complex_model_l_gpu
- 118.048339844GB

