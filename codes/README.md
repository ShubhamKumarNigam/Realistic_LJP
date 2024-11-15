# Realistic Legal Judgment Prediction (LJP) Code Repository

This repository contains the implementation of models and methods for legal judgment prediction and explanation, simulating realistic scenarios using various transformer models and large language models (LLMs). The provided scripts support both binary classification (judgment prediction) and rationale generation (explanation).

## Code Files

The following are the main scripts included in the repository:

- **`gpt.py`**: Implements legal judgment prediction using GPT models without Chain-of-Thought (CoT) prompting.
- **`gpt_cot.py`**: Extends GPT models to use Chain-of-Thought (CoT) prompting for enhanced prediction and explanation.
- **`llama1.py`**: Llama-2 (13b) model implementation for judgment prediction without CoT prompting.
- **`llama1_cot.py`**: Llama-2 (13b) model with Chain-of-Thought (CoT) prompting.
- **`llama2.py`**: Llama-2 (70b) model implementation for judgment prediction without CoT prompting.
- **`llama2_cot.py`**: Llama-2 (70b) model with Chain-of-Thought (CoT) prompting.
- **`transformer_binary_classification.py`**: Implements binary classification using transformer models like BERT, InLegalBERT, and XLNet.

## Summarization Methods

The dataset preparation and summarization methods used in this repository leverage pre-trained summarization models available from:  
[https://github.com/Law-AI/summarization](https://github.com/Law-AI/summarization)

Summarized inputs are critical for fitting lengthy legal texts into models with token length constraints, such as GPT and Llama.

