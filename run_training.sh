# rationale generation
CUDA_VISIBLE_DEVICES=0,1 python main.py \
    --model models/rationale \
    --user_msg rationale --img_type detr \
    --data_root ../../FolkScope \
    --bs 2 --eval_bs 1 --eval_acc 10 --output_len 512 --epoch 2 \
    --final_eval --prompt_format QCM-LE --output_dir test

## answer inference
#CUDA_VISIBLE_DEVICES=0,1 python main1.py \
#    --model allenai/unifiedqa-t5-base \
#    --user_msg answer --img_type detr \
#    --bs 8 --eval_bs 4 --eval_acc 10 --output_len 64 \
#    --final_eval --prompt_format QCMG-A \
#    --eval_le experiments/rationale_allenai-unifiedqa-t5-base_detr_QCM-LE_lr5e-05_bs16_op512_ep20/predictions_ans_eval.json \
#    --test_le experiments/rationale_allenai-unifiedqa-t5-base_detr_QCM-LE_lr5e-05_bs16_op512_ep20/predictions_ans_test.json