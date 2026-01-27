#!/bin/bash
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --time=4-00:00:00
#SBATCH --job-name=trainable_data
#SBATCH --output=trainable_data_job.out
#SBATCH --error=trainable_data_job.err
#SBATCH --exclusive
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

ulimit -s unlimited
ulimit -c unlimited

module purge
source /scratch/$USER/miniconda3/bin/activate
conda activate /scratch/$USER/mtp_maithri/maithri

cd $SLURM_SUBMIT_DIR
export CUDA_VISIBLE_DEVICES=0
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

CUDA_VISIBLE_DEVICES=0 python3 run_mybart.py \
  --model_name_or_path facebook/bart-base \
  --do_train --do_eval \
  --train_file cnndm_wiki_pubmed_train.json \
  --validation_file cnndm_wiki_pubmed_valid.json \
  --test_file cnndm_wiki_pubmed_test.json \
  --output_dir das \
  --exp_name first \
  --max_source_length 1024 \
  --max_target_length 300 \
  --gene_dataset_path cnndm_wiki_pubmed
