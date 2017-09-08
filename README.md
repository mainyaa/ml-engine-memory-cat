# Google Cloud ML Engineのメモリを調べてみた

https://cloud.google.com/ml-engine/docs/concepts/training-overview

> Even though the exact specifications of the machine types are subject to change at any time, you can compare them in terms of relative capability. The following table uses rough "t-shirt" sizing to describe the machine types.

ココらへんがいまいち曖昧なので調べてみた

trainer/task.py
```python
import os

mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
mem_gib = mem_bytes/(1024.**3)  # e.g. 3.74
print(str(mem_gib)+"GB")
meminfo = dict((i.split()[0].rstrip(':'),int(i.split()[1])) for i in open('/proc/meminfo').readlines())
mem_kib = meminfo['MemTotal']  # e.g. 3921852
print(str(mem_kib)+"KB")
exit()
```

# BASIC
gcloud ml-engine jobs submit training $JOB_NAME \
--job-dir $OUTPUT_PATH \
--runtime-version 1.2 \
--module-name trainer.task \
--package-path trainer/ \
--region $REGION \
--scale-tier STANDARD_1 \
-- \
--train-files $TRAIN_DATA \
--eval-files $EVAL_DATA \
--train-steps 1000 \
--verbosity DEBUG

## BASIC Result
 - 14.6924285889GB
 - 15,406,128KB

## STANDARD_1
gcloud ml-engine jobs submit training $JOB_NAME \
--job-dir $OUTPUT_PATH \
--runtime-version 1.2 \
--module-name trainer.task \
--package-path trainer/ \
--region $REGION \
--scale-tier STANDARD_1 \
-- \
--train-files $TRAIN_DATA \
--eval-files $EVAL_DATA \
--train-steps 1000 \
--verbosity DEBUG

## STANDARD_1 Result
  - 7.01322555542GB
  - 7,353,900KB
