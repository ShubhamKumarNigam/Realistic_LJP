# Realistic Legal Judgment Prediction (LJP) Dataset Repository

This repository provides the datasets and detailed steps used to prepare the data for our experiments on Legal Judgment Prediction (LJP) with Explanation, focusing on realistic scenarios. The dataset preparation process involves segmenting legal judgments into rhetorical roles and creating variations of the dataset suitable for experiments with Large Language Models (LLMs).

## Dataset Preparation Steps

The following steps outline the process to prepare the dataset:

1. **Collect the Initial Dataset**  
   The initial dataset is sourced from the ILDC multi-dataset, as introduced in the paper:  
   [ILDC for CJPE: Indian Legal Documents Corpus for Court Judgment Prediction and Explanation](https://aclanthology.org/2021.acl-long.313/)  

   Access the dataset from the official GitHub page:  
   [https://github.com/Exploration-Lab/CJPE](https://github.com/Exploration-Lab/CJPE)  

   For our experiments, we use the **test portion** of the ILDC multi-dataset.

2. **Segmenting Legal Judgments into Rhetorical Roles**  
   To segment legal judgments into rhetorical roles, we use the **Hierarchical-BiLSTM CRF model** provided in the repository:  
   [https://github.com/Law-AI/semantic-segmentation](https://github.com/Law-AI/semantic-segmentation)

   - Run the `train.py` file to train the segmentation model. This will generate files like `model_state_fn.tar` and `data_state_fn.tar`.
   - Use the `infer.py` script with the ILDC multi test files placed in the `infer/data/` folder.  
   - This will produce segmented outputs categorizing sentences into rhetorical roles such as *facts*, *ruling by lower court*, *precedents*, *statutes*, and *arguments*.

3. **Creating Dataset Variations**  
   Group the sentences into specific categories based on rhetorical roles for experiments. We create four variations:  
   - **Variation 1:** All *facts* sentences grouped together.  
   - **Variation 2:** *Facts*, *statutes*, and *precedents* grouped together.  
   - **Variation 3:** *Facts*, *statutes*, *precedents*, and *rulings by lower courts* grouped together.  
   - **Variation 4:** *Facts*, *statutes*, *precedents*, *rulings by lower courts*, and *arguments* grouped together.

4. **Using the Variations for LLM Experiments**  
   Use these four dataset variations as input for LLM-based experiments, following the methodology described in our accompanying paper.

## Datasets on Hugging Face

The prepared and summarized datasets are available on Hugging Face for direct use in experiments:

- [Realistic LJP Facts](https://huggingface.co/datasets/L-NLProc/Realistic_LJP_Facts)
- [Realistic LJP CaseSummarizer](https://huggingface.co/datasets/L-NLProc/Realistic_LJP_CaseSummarizer)
- [Realistic LJP LetSum](https://huggingface.co/datasets/L-NLProc/Realistic_LJP_LetSum)
- [Realistic LJP SummaRuNNer](https://huggingface.co/datasets/L-NLProc/Realistic_LJP_SummaRuNNer)
- [Realistic LJP BertSum](https://huggingface.co/datasets/L-NLProc/Realistic_LJP_BertSum)

## Citation

If you use this dataset in your research, please cite our work appropriately. Details of the paper and citation format will be provided in this repository upon publication.

## Citation
If you use this dataset in your research, please cite our work appropriately. [Our paper](https://aclanthology.org/2024.nllp-1.6/):
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
