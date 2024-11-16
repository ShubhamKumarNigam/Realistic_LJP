<h1 align="center">
<img src="Assets/L-NLP_Logo_Transparent.png" width="100" alt="L-NLP" />
<br>
Rethinking Legal Judgement Prediction in a Realistic Scenario in the Era of Large Language Models (NLLP@EMNLP 2024)
</h1>

![task_desc](https://github.com/ShubhamKumarNigam/Realistic_LJP/blob/main/Assets/workflow.jpg)

<p align="center">
  <a href="https://huggingface.co/L-NLProc"><b>[🌐 Website]</b></a> •
  <a href="https://aclanthology.org/2024.nllp-1.6/"><b>[📜 Proceedings]</b></a> •
  <a href="https://arxiv.org/pdf/2410.10542"><b>[📜 ArXiv]</b></a> •
  <a href="https://huggingface.co/collections/L-NLProc/realistic-ljp-models-671e8ed671a1f530eeb81221"><b>[🤗 HF Models]</b></a> •
  <a href="https://huggingface.co/collections/L-NLProc/realistic-ljp-datasets-670ccbeab5aea07a37e86df8"><b>[🤗 HF Dataset]</b></a> •
  <a href="https://github.com/ShubhamKumarNigam/Realistic_LJP"><b>[🐱 GitHub]</b></a>
</p>

<p align="center">
  This is the official implementation of the paper:
</p>

<p align="center">
  <a href="https://sites.google.com/view/shubhamkumarnigam">Shubham Kumar Nigam</a>, <a href="https://sites.google.com/view/aniket-deroy-profile/home">Aniket Deroy</a>, <a href="https://sites.google.com/view/subhankarmaity/home">Subhankar Maity</a>, and <a href="https://www.cse.iitk.ac.in/users/arnabb/">Arnab Bhattacharya</a>:
</p>

This study investigates judgment prediction in a realistic scenario within the context of Indian judgments, utilizing a range of transformer-based models, including InLegalBERT, BERT, and XLNet, alongside LLMs such as Llama-2 and GPT-3.5 Turbo. In this realistic scenario, we simulate how judgments are predicted at the point when a case is presented for a decision in court, using only the information available at that time, such as the facts of the case, statutes, precedents, and arguments. This approach mimics real-world conditions, where decisions must be made without the benefit of hindsight, unlike retrospective analyses often found in previous studies. For transformer models, we experiment with hierarchical transformers and the summarization of judgment facts to optimize input for these models. Our experiments with LLMs reveal that GPT-3.5 Turbo excels in realistic scenarios, demonstrating robust performance in judgment prediction. Furthermore, incorporating additional legal information, such as statutes and precedents, significantly improves the outcome of the prediction task. The LLMs also provide explanations for their predictions. To evaluate the quality of these predictions and explanations, we introduce two human evaluation metrics: **Clarity** and **Linking**. Our findings from both automatic and human evaluations indicate that, despite advancements in LLMs, they are yet to achieve expert-level performance in judgment prediction and explanation tasks.


## Citation
If you use our method or models, please cite [our paper](https://aclanthology.org/2024.nllp-1.6/):
```
@inproceedings{nigam-etal-2024-rethinking,
    title = "Rethinking Legal Judgement Prediction in a Realistic Scenario in the Era of Large Language Models",
    author = "Nigam, Shubham Kumar  and
      Deroy, Aniket  and
      Maity, Subhankar  and
      Bhattacharya, Arnab",
    editor = "Aletras, Nikolaos  and
      Chalkidis, Ilias  and
      Barrett, Leslie  and
      Goan{\textcommabelow{t}}{\u{a}}, C{\u{a}}t{\u{a}}lina  and
      Preo{\textcommabelow{t}}iuc-Pietro, Daniel  and
      Spanakis, Gerasimos",
    booktitle = "Proceedings of the Natural Legal Language Processing Workshop 2024",
    month = nov,
    year = "2024",
    address = "Miami, FL, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.nllp-1.6",
    pages = "61--80",
    abstract = "This study investigates judgment prediction in a realistic scenario within the context of Indian judgments, utilizing a range of transformer-based models, including InLegalBERT, BERT, and XLNet, alongside LLMs such as Llama-2 and GPT-3.5 Turbo. In this realistic scenario, we simulate how judgments are predicted at the point when a case is presented for a decision in court, using only the information available at that time, such as the facts of the case, statutes, precedents, and arguments. This approach mimics real-world conditions, where decisions must be made without the benefit of hindsight, unlike retrospective analyses often found in previous studies. For transformer models, we experiment with hierarchical transformers and the summarization of judgment facts to optimize input for these models. Our experiments with LLMs reveal that GPT-3.5 Turbo excels in realistic scenarios, demonstrating robust performance in judgment prediction. Furthermore, incorporating additional legal information, such as statutes and precedents, significantly improves the outcome of the prediction task. The LLMs also provide explanations for their predictions. To evaluate the quality of these predictions and explanations, we introduce two human evaluation metrics: Clarity and Linking. Our findings from both automatic and human evaluations indicate that, despite advancements in LLMs, they are yet to achieve expert-level performance in judgment prediction and explanation tasks."
}
```
