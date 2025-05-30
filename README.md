<a id="readme-top"></a>

# Awesome Action Quality Assessment (AQA)

[![Project Page](https://img.shields.io/badge/Project-Page-blue.svg)](https://zhoukanglei.github.io/AQA-Survey)
[![Page Views Count](https://badges.toozhao.com/badges/01JDKP6H9FYE9WEX7ADV27SFW4/green.svg)](https://badges.toozhao.com/stats/01JDKP6H9FYE9WEX7ADV27SFW4 "Get your own page views count badge on badges.toozhao.com")

> Pull requests are welcome if you find any interesting paper is missing.
>
> - 🔥🔥🔥 denotes the highly recommended papers for the novel insights and new directions.
> - We have created a [Wechat group](./imgs/aqa-wechat-group.png) for our colleagues to exchange and discuss the latest progress in the field of AQA, contributing to the development of this field. If it expires, please scan my [personal account](./imgs/ZKL.png).

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents: Papers and Datasets</summary>
  <ol>
    <li>
      <a href="#papers">Papers</a>
      <ul>
        <li><a href="#sports">Sports</a></li>
        <li><a href="#medical-care">Medical Care</a></li>
        <li><a href="#skill-assessment">Skill Assessment</a></li>
      </ul>
    </li>
    <li><a href="#datasets">Datasets</a></li>
  </ol>
</details>

# Papers

Currently, AQA is widely applied in sports, medical care (_e.g._, rehabilitation), skill assessment, _etc_.

## Highly Recommended Survey and Benchmark

- [arXiv 2024] A Comprehensive Survey of Action Quality Assessment: Method and Benchmark. [PDF](https://arxiv.org/pdf/2412.11149) | [Github](https://github.com/ZhouKanglei/AQA-Benchmark) | $\color{orange}\textsf{Survey} + \color{orange}\textsf{Benchmark}$
- [ESWA 2024] Vision-based human action quality assessment: A systematic review. [DOI](https://doi.org/10.1016/j.eswa.2024.125642) | $\color{orange}\textsf{Survey}$
- [arXiv 2025] A Decade of Action Quality Assessment: Largest Systematic Survey of Trends, Challenges, and Future Directions. [PDF](https://arxiv.org/pdf/2502.02817) | $\color{orange}\textsf{Survey}$

## Sports

### 2025

- [TPAMI 2025] Human-centric Fine-grained Action Quality Assessment. [DOI](https://doi.org/10.1109/TPAMI.2025.3556935) | [PDF](papers/25-tpami-human_centric.pdf)
- [TIP 2025] PHI: Bridging Domain Shift in Long-Term Action Quality Assessment via Progressive Hierarchical Instruction. [PDF](https://arxiv.org/abs/2505.19972) | [Github](https://github.com/ZhouKanglei/PHI_AQA) | $\color{magenta}\textsf{Domain Shift}$
- [TCSVT 2025] Adaptive Spatiotemporal Graph Transformer Network for Action Quality Assessment. [DOI](https://doi.org/10.1109/TCSVT.2025.3541456) | [PDF](papers/25-tcsvt-st_graph_transformer.pdf)
- [TCSVT 2024] Visual-semantic Alignment Temporal Parsing for Action Quality Assessment. [DOI](https://doi.org/10.1109/TCSVT.2024.3487242) | [PDF](papers/25-tcsvt-visual_semantic_alignment.pdf) | $\color{cyan}\textsf{Video + Text}$
- [TOMM 2025] Scaled Background Swap: Video Augmentation for Action Quality Assessment with Background Debiasing. [DOI](https://dl.acm.org/doi/10.1145/3737461) | [PDF](papers/25-tomm-backgroud_debiasing.pdf) | [Github](https://github.com/Emy-cv/Scaled-Background-Swap)

---

- [CVPR 2025] BASKET: A Large-Scale Video Dataset for Fine-Grained Skill Estimation. [PDF](https://arxiv.org/pdf/2503.20781) | [Github](https://github.com/yulupan00/BASKET)
- [AAAI 2025] DanceFix: An Exploration in Group Dance Neatness Assessment Through Fixing Abnormal Challenges of Human Pose. [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/32959)
- [CVPRW 2025] FineCausal: A Causal-Based Framework for Interpretable Fine-Grained Action Quality Assessment. [PDF](https://arxiv.org/pdf/2503.23911) | [Github](https://github.com/Harrison21/FineCausal) | $\color{magenta}\textsf{Interpretable Reasoning}$

---

- [arXiv 2025] A Decade of Action Quality Assessment: Largest Systematic Survey of Trends, Challenges, and Future Directions. [PDF](https://arxiv.org/pdf/2502.02817) | $\color{orange}\textsf{Survey}$
- [arXiv 2025] Action Quality Assessment via Hierarchical Pose-guided Multi-stage Contrastive Regression. [PDF](https://arxiv.org/pdf/2501.03674) | [Github](https://github.com/Lumos0507/HP-MCoRe) | $\color{lime}\textsf{Contrastive Regression}$

### 2024

- [IJCV 2024] Procedure-Aware Action Quality Assessment: Datasets and Performance Evaluation. [PDF](https://link.springer.com/article/10.1007/s11263-024-02146-z) | [Github](https://github.com/xujinglin/FineDiving)
- [TIP 2024] Self-supervised subaction Parsing Network for Semi-supervised Action Quality Assessment. [DOI](https://doi.org/10.1109/TIP.2024.3468870) | [PDF](papers/24-tip-subaction_parsing_network.pdf)
- [TIP 2024] Multimodal Action Quality Assessment. [PDF](https://arxiv.org/pdf/2402.09444.pdf) | [Github](https://github.com/qinghuannn/PAMFN) | $\color{yellow}\textsf{Video + Audio}\color{yellow}\textsf{ + Flow}$
- [TCSVT 2024] Continual Action Assessment via Task-Consistent Score-Discriminative Feature Distribution Modeling. [PDF](https://arxiv.org/pdf/2309.17105.pdf) | [Github](https://github.com/iSEE-Laboratory/Continual-AQA) | 🧠 $\color{pink}\textsf{Continual Learning}$
- [Information Sciences 2024] Two-path target-aware contrastive regression for action quality assessment. [DOI](https://doi.org/10.1016/j.ins.2024.120347) | [PDF](papers/24-infsci-two_path.pdf) | [Github](https://github.com/XuHuangbiao/T2CR) | $\color{lime}\textsf{Contrastive Regression}$ 
- [TIM 2024] Learning Sparse Temporal Video Mapping for Action Quality Assessment in Floor Gymnastics. [PDF](https://arxiv.org/pdf/2301.06103) | $\color{lightgreen}\textsf{Video + Skeleton}$
- [TCE 2024] ResFNN: Residual Structure-Based Feedforward Neural Network for Action Quality Assessment in Sports Consumer Electronics. [DOI](https://doi.org/10.1109/TCE.2024.3482560)
- [Applied Intelligence 2024] Assessing action quality with semantic-sequence performance regression and densely distributed sample weighting. [DOI](https://doi.org/10.1007/s10489-024-05349-6)
- [Neurocomputing 2024] Dual-referenced assistive network for action quality assessment. [DOI](https://doi.org/10.1016/j.neucom.2024.128786)
- [ESWA 2024] Vision-based human action quality assessment: A systematic review. [DOI](https://doi.org/10.1016/j.eswa.2024.125642) | $\color{orange}\textsf{Survey}$

---

- [NeurIPS 2024 **Spotlight**] GAIA: Rethinking Action Quality Assessment for AI-Generated Videos. [PDF](https://arxiv.org/pdf/2406.06087) | [Github](https://github.com/zijianchen98/GAIA) |🔥🔥🔥
- [NeurIPS 2024] LucidAction: A Hierarchical and Multi-model Dataset for Comprehensive Action Quality Assessment. [NeurIPS 2024 Website](https://nips.cc/virtual/2024/poster/97542) | $\color{lightgreen}\textsf{Video + Skeleton}$
- [CVPR 2024 **Oral**] FineParser: A Fine-grained Spatio-temporal Action Parser for Human-centric Action Quality Assessment. [PDF](https://arxiv.org/pdf/2405.06887) | [Github](https://github.com/PKU-ICST-MIPL/FineParser_CVPR2024)
- [CVPR 2024] Narrative Action Evaluation with Prompt-Guided Multimodal Interaction. [PDF](https://arxiv.org/pdf/2404.14471) | [Github](https://github.com/shiyi-zh0408/NAE_CVPR2024) | $\color{magenta}\textsf{Interpretable Feedback}$, $\color{cyan}\textsf{Video + Text}$
- [ECCV 2024 **Oral**] MAGR: Manifold-Aligned Graph Regularization for Continual Action Quality Assessment. [PDF](https://arxiv.org/pdf/2403.04398.pdf) | [Github](https://github.com/ZhouKanglei/MAGR_CAQA) | 🧠 $\color{pink}\textsf{Continual Learning}$
- [ECCV 2024] RICA^2: Rubric-Informed, Calibrated Assessment of Actions. [PDF](https://arxiv.org/pdf/2408.02138) | [Github](https://github.com/abrarmajeedi/rica2_aqa) | $\color{cyan}\textsf{Video + Text}$
- [ECCV 2024] Semi-Supervised Teacher-Reference-Student Architecture for Action Quality Assessment. [PDF](https://arxiv.org/pdf/2407.19675)
- [ECCV 2024] Vision-Language Action Knowledge Learning for Semantic-Aware Action Quality Assessment. [PDF](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05909.pdf) | $\color{cyan}\textsf{Video + Text}$
- [IJCAI 2024] CoFInAl: Enhancing Action Quality Assessment with Coarse-to-Fine Instruction Alignment. [PDF](https://arxiv.org/pdf/2404.13999.pdf) | [Github](https://github.com/ZhouKanglei/CoFInAl_AQA) | $\color{magenta}\textsf{Domain Shift}$
- [ACM MM 2024] 2M-AF: A Strong Multi-Modality Framework For Human Action Quality Assessment with Self-supervised Representation Learning. [PDF](https://openreview.net/forum?id=oEhi4pd0e1)
- [BMVC 2024] Interpretable Long-term Action Quality Assessment. [PDF](https://arxiv.org/pdf/2408.11687) | [Github](https://github.com/dx199771/Interpretability-AQA)
- [WACV 2024 **Oral**] PECoP: Parameter Efficient Continual Pretraining for Action Quality Assessment. [PDF](https://arxiv.org/pdf/2311.07603.pdf) | [Github](https://github.com/Plrbear/PECoP) | 🧠 $\color{pink}\textsf{Continual Learning}$ | $\color{magenta}\textsf{Domain Shift}$
- [ICASSP 2024] Multi-Stage Contrastive Regression for Action Quality Assessment. [PDF](https://arxiv.org/pdf/2401.02841) | [Github](https://github.com/Angel-1999/MCoRe) | $\color{lime}\textsf{Contrastive Regression}$
- [CVPRW 2024] Hierarchical NeuroSymbolic Approach for Comprehensive and Explainable Action Quality Assessment. [PDF](https://arxiv.org/pdf/2403.13798) | [Github](https://github.com/laurenok24/NSAQA) | $\color{magenta}\textsf{Interpretable Feedback}$

---

- [arXiv 2024] Learning to Score Sign Language with Two-stage Method. [PDF](https://arxiv.org/pdf/2404.10383)
- [arXiv 2024] TechCoach: Towards Technical Keypoint-Aware Descriptive Action Coaching. [PDF](https://arxiv.org/pdf/2411.17130) | $\color{magenta}\textsf{Interpretable Feedback}$
- [arXiv 2024] ExpertAF: Expert Actionable Feedback from Video. [PDF](https://arxiv.org/pdf/2408.00672) | $\color{magenta}\textsf{Interpretable Feedback}$

### 2023

- [IJCV 2023] Automatic Modelling for Interactive Action Assessment. [DOI](https://doi.org/10.1007/s11263-022-01695-5) | [PDF](papers/23-ijcv-automatic_interactive_modelling.pdf)
- [TIP 2023] Fine-grained Spatio-temporal Parsing Network for Action Quality Assessment. [DOI](https://doi.org/10.1109/TIP.2023.3331212) | [PDF](papers/23-tip-fspn.pdf)
- [TCSVT 2023] Hierarchical Graph Convolutional Networks for Action Quality Assessment. [PDF](http://hubertshum.com/publications/tcsvt2023aqa/files/tcsvt2023aqa.pdf) | [DOI](https://doi.org/10.1109/TCSVT.2023.3281413) | [Github](https://github.com/ZhouKanglei/HGCN_AQA)
- [TMM 2023] Learning Semantics-Guided Representations for Scoring Figure Skating. [DOI](https://doi.org/10.1109/TMM.2023.3328180) | $\color{cyan}\textsf{Video + Text}$
- [NCAA 2023] Auto-encoding score distribution regression for action quality assessment. [PDF](https://arxiv.org/pdf/2111.11029.pdf) | [DOI](https://doi.org/10.1007/s00521-023-09068-w) | [Github](https://github.com/InfoX-SEU/DAE-AQA)
- [Applied Intelligence 2023] Multi-skeleton structures graph convolutional network for action quality assessment in long videos. [DOI](https://doi.org/10.1007/s10489-023-04613-5)
- [Applied Intelligence 2023] Label-reconstruction-based pseudo-subscore learning for action quality assessment in sporting events. [DOI](https://doi.org/10.1007/s10489-022-03984-5)
- [Applied Intelligence 2023] Improving action quality assessment with across-staged temporal reasoning on imbalanced data. [DOI](https://doi.org/10.1007/s10489-023-05166-3)

---

- [CVPR 2023] LOGO: A Long-Form Video Dataset for Group Action Quality Assessment. [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhang_LOGO_A_Long-Form_Video_Dataset_for_Group_Action_Quality_Assessment_CVPR_2023_paper.pdf) | [Github](https://github.com/shiyi-zh0408/LOGO)
- [AAAI 2023] Skating-Mixer: Long-Term Sport Audio-Visual Modeling with MLPs. [PDF](https://arxiv.org/pdf/2203.03990.pdf) | [Github](https://github.com/AndyFrancesco29/Audio-Visual-Figure-Skating) | $\color{yellow}\text{Video + Audio}$
- [ACM MM 2023] A Figure Skating Jumping Dataset for Replay-Guided Action Quality Assessment. [DOI](https://dl.acm.org/doi/abs/10.1145/3581783.3613774)
- [ACM MM 2023] Localization-assisted Uncertainty Score Disentanglement Network for Action Quality Assessment. [DOI](https://dl.acm.org/doi/abs/10.1145/3581783.3613795) | [Github - FineFS dataset avail, code not avail](https://github.com/yanliji/FineFS-dataset)
- [IUI 2023] IRIS: Interpretable Rubric-Informed Segmentation for Action Quality Assessment. [PDF](https://arxiv.org/pdf/2303.09097.pdf) | [Github](https://github.com/shiyi-zh0408/LOGO)
- [ICASSP 2023] Contrastive Self-Supervised Learning for Automated Multi-Modal Dance Performance Assessment. [DOI](https://doi.org/10.1109/ICASSP49357.2023.10096824) | $\color{lime}\textsf{Contrastive Regression}$

### 2022

- [TCSVT 2022] Semi-Supervised Action Quality Assessment With Self-Supervised Segment Feature Recovery. [DOI](https://doi.org/10.1109/TCSVT.2022.3143549)
- [JVCIR 2022] Skeleton-based deep pose feature learning for action quality assessment on figure skating videos. [DOI](https://doi.org/10.1016/j.jvcir.2022.103625)

---

- [CVPR 2022 **Oral**] FineDiving: A Fine-grained Dataset for Procedure-aware Action Quality Assessment. [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Xu_FineDiving_A_Fine-Grained_Dataset_for_Procedure-Aware_Action_Quality_Assessment_CVPR_2022_paper.pdf) | [Github](https://github.com/xujinglin/FineDiving)
- [CVPR 2022] Likert Scoring with Grade Decoupling for Long-term Action Assessment. [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Xu_Likert_Scoring_With_Grade_Decoupling_for_Long-Term_Action_Assessment_CVPR_2022_paper.pdf) | [Github](https://github.com/xuangch/CVPR22_GDLT)
- [ECCV 2022] Action Quality Assessment with Temporal Parsing Transformer. [PDF](https://arxiv.org/pdf/2207.09270.pdf) | [Github](https://github.com/baiyang4/aqa_tpt)
- [ECCV 2022] Pairwise Contrastive Learning Network for Action Quality Assessment. [PDF](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136640450.pdf) | $\color{lime}\textsf{Contrastive Regression}$

### 2021

- [TPAMI 2021] Adaptive Action Assessment. [DOI](https://doi.org/10.1109/TPAMI.2021.3126534)
- [TOMM 2021] Will You Ever Become Popular? Learning to Predict Virality of Dance Clips. [PDF](https://arxiv.org/pdf/2111.03819)

---

- [CVPR 2021] AIFit: Automatic 3D Human-Interpretable
  Feedback Models for Fitness Training. [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Fieraru_AIFit_Automatic_3D_Human-Interpretable_Feedback_Models_for_Fitness_Training_CVPR_2021_paper.pdf) | $\color{magenta}\textsf{Interpretable Feedback}$
- [ICCV 2021] Group-aware Contrastive Regression for Action Quality Assessment. [PDF](https://openaccess.thecvf.com/content/ICCV2021/papers/Yu_Group-Aware_Contrastive_Regression_for_Action_Quality_Assessment_ICCV_2021_paper.pdf) | [Github](https://github.com/yuxumin/CoRe) | $\color{lime}\textsf{Contrastive Regression}$
- [ACM MM 2021] TSA-Net: Tube Self-Attention Network for Action Quality Assessment. [PDF](https://arxiv.org/pdf/2201.03746.pdf) | [Github](https://github.com/Shunli-Wang/TSA-Net)
- [WACV 2021] EAGLE-Eye: Extreme-pose Action Grader using detaiL bird’s-Eye view. [PDF](https://openaccess.thecvf.com/content/WACV2021/papers/Nekoui_EAGLE-Eye_Extreme-Pose_Action_Grader_Using_Detail_Birds-Eye_View_WACV_2021_paper.pdf)
- [ICIP 2021] Action quality assessment with ignoring scene context. [DOI](https://doi.org/10.1109/ICIP42928.2021.9506257)
- [PETRA 2021] Towards Improved and Interpretable Action Quality Assessment with Self-Supervised Alignment. [PDF](https://users.ics.forth.gr/~argyros/mypapers/2021_06_PETRA_AQA-Roditakis.pdf)
- [INSAI 2021] A survey of video-based action quality assessment. [PDF](https://arxiv.org/pdf/2204.09271.pdf) | $\color{orange}\textsf{Survey}$

### 2020

- [CVPR 2020] Uncertainty-aware Score Distribution Learning for Action Quality Assessment. [PDF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Tang_Uncertainty-Aware_Score_Distribution_Learning_for_Action_Quality_Assessment_CVPR_2020_paper.pdf) | [Github](https://github.com/nzl-thu/MUSDL)
- [ECCV 2020] An Asymmetric Modeling for Action Assessment. [PDF](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123750222.pdf)

### 2019 and Before

- [CVPR 2019] What and How Well You Performed? A Multitask Learning Approach to Action Quality Assessment. [PDF](https://openaccess.thecvf.com/content_CVPR_2019/papers/Parmar_What_and_How_Well_You_Performed_A_Multitask_Learning_Approach_CVPR_2019_paper.pdf) | [Github](https://github.com/ParitoshParmar/MTL-AQA)
- [ICCV 2019] Action Assessment by Joint Relation Graphs. [PDF](https://openaccess.thecvf.com/content_ICCV_2019/papers/Pan_Action_Assessment_by_Joint_Relation_Graphs_ICCV_2019_paper.pdf)
- [WACV 2019] Action Quality Assessment Across Multiple Actions. [PDF](https://arxiv.org/pdf/2111.11029)
- [PCM 2018] End-to-end learning for action quality assessment. [DOI](https://doi.org/10.1007/978-3-030-00767-6_12)
- [ICIP 2018] S3d: Stacking segmental p3d for action quality assessment. [DOI](https://doi.org/10.1109/ICIP.2018.8451364)
- [ACCV 2018] Scoringnet: Learning key fragment for action quality assessment with ranking loss in skilled sports. [DOI](https://doi.org/10.1007/978-3-030-20876-9_10)
- [ICCV 2017] Am I a Baller? Basketball Performance Assessment from First-Person Videos. [PDF](https://openaccess.thecvf.com/content_ICCV_2017/papers/Bertasius_Am_I_a_ICCV_2017_paper.pdf)
- [BMVC 2015] Dynamical Regularity for Action Analysis. [PDF](https://bmva-archive.org.uk/bmvc/2015/papers/paper067/paper067.pdf)
- [ECCV 2014] Assessing the Quality of Actions. [PDF](https://core.ac.uk/download/pdf/78056242.pdf) | [Project](https://redirect.cs.umbc.edu/~hpirsiav/quality.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Medical Care

### 2024

- [TPAMI 2024] EGCN++: A New Fusion Strategy for Ensemble Learning in Skeleton-based Rehabilitation Exercise Assessment. [PDF](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10475587) | [GitHub - EGCN++ not avail. EHE dataset avail.](https://github.com/bruceyo/egcnplusplus)
- [TNSRE 2024] Automatic Assessment of Upper Extremity Function and Mobile Application for Self-Administered Stroke Rehabilitation. [DOI](https://doi.org/10.1109/TNSRE.2024.3358497)
- [TNSRE 2024] An Expert-Knowledge-Based Graph Convolutional Network for Skeleton- Based Physical Rehabilitation Exercises Assessment. [DOI](https://doi.org/10.1109/TNSRE.2024.3400790)

---

- [CVPRW 2024] FineRehab: A Multi-modality and Multi-task Dataset for Rehabilitation Analysis. [PDF](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Li_FineRehab_A_Multi-modality_and_Multi-task_Dataset_for_Rehabilitation_Analysis_CVPRW_2024_paper.pdf) | [Project](https://bsu3dvlab.github.io/FineRehab/)

### 2023

- [TVCG 2023] A Video-Based Augmented Reality System for Human-in-the-Loop Muscle Strength Assessment of Juvenile Dermatomyositis. [PDF](http://hubertshum.com/publications/tvcg2023jdm/files/tvcg2023jdm.pdf) | [DOI](https://doi.org/10.1109/TVCG.2023.3247092) | [Video](https://www.youtube.com/watch?v=ASxzXP3bemY) | $\color{magenta}\textsf{Interpretable Feedback}$
- [TNSRE 2023] A Contrastive Learning Network for Performance Metric and Assessment of Physical Rehabilitation Exercises. [PDF](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10256137) | $\color{lime}\textsf{Contrastive Regression}$
- [TNSRE 2023] A Skeleton-Based Rehabilitation Exercise Assessment System With Rotation Invariance. [DOI](https://doi.org/10.1109/TNSRE.2023.3282675) | [Github](https://github.com/Kelly510/RehabExerAssess)

---

- [CHASE 2023] Short: Deep Learning Approach to Skeletal Performance Evaluation of Physical Therapy Exercises. [DOI](https://doi.org/10.1145/3580252.3586984)
- [ICCVW 2023] Personalized Monitoring in Home Healthcare: An Assistive System for Post Hip Replacement Rehabilitation. [PDF](https://openaccess.thecvf.com/content/ICCV2023W/ACVR/papers/Kryeem_Personalized_Monitoring_in_Home_Healthcare_An_Assistive_System_for_Post_ICCVW_2023_paper.pdf)

### 2022

- [TNSRE 2022] Graph convolutional networks for assessment of physical rehabilitation exercises. [DOI](https://doi.org/10.1109/TNSRE.2022.3150392)

---

- [IJCAI 2022] EGCN: An Ensemble-based Learning Framework for Exploring Effective Skeleton-based Rehabilitation Exercise Assessment. [PDF](https://www.ijcai.org/proceedings/2022/0511.pdf) | [Github](https://github.com/bruceyo/EGCN)

### 2021

- [PR 2021] Skeleton-based human action evaluation using graph convolutional network for monitoring Alzheimer’s progression. [PDF](https://www.sciencedirect.com/science/article/pii/S003132032100282X) | [DOI](https://doi.org/10.1016/j.patcog.2021.108095)

### 2020

- [TNSRE 2020] A Deep Learning Framework for Assessing Physical Rehabilitation Exercises. [PDF](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8957502) | [DOI](https://doi.org/10.1109/TNSRE.2020.2966249)
- [Sensors 2020] VI-Net: View-Invariant Quality of Human Movement Assessment. [PDF](https://arxiv.org/pdf/2008.04999)

### 2019 and Before

- [TNSRE 2019] The KIMORE Dataset: KInematic Assessment of MOvement and Clinical Scores for Remote Monitoring of Physical REhabilitation. [PDF](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8736767) | [DOI](https://doi.org/10.1109/TNSRE.2019.2923060)
- [Data 2018] A Data Set of Human Body Movements for Physical Rehabilitation Exercises. [PDF](https://www.mdpi.com/2306-5729/3/1/2)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Skill Assessment

### 2024

- [TCSVT 2024] Rhythmer: Ranking-based Skill Assessment with Rhythm-aware Transformer. [DOI](https://doi.org/10.1109/TCSVT.2024.3459938)
- [TMM 2024] Adaptive Stage-Aware Assessment Skill Transfer for Skill Determination. [DOI](https://doi.org/10.1109/TMM.2023.3294800)

---

- [ICASSP 2024] Which is the Better Teacher Action? A New Ranking Model and Dataset. [DOI](https://doi.org/10.1109/ICASSP48485.2024.10448158) | [Github](https://github.com/MingZier/TAQR-Dataset)

### 2023

- [RA-L 2023] Keep Your Eye on the Best: Contrastive Regression Transformer for Skill Assessment in Robotic Surgery. [PDF](https://discovery.ucl.ac.uk/id/eprint/10164755/2/Anastasiou_Keep%20Your%20Eye%20on%20the%20Best_AAM.pdf) | [Github](https://github.com/anastadimi/Contra-Sformer) | $\color{lime}\textsf{Contrastive Regression}$

---

- [MICCAI 2023] Sedskill: Surgical events driven method for skill assessment from thoracoscopic surgical videos. [PDF](https://xmengli.github.io/papers/2023MICCAI-XDing.pdf) | [Github](https://github.com/xmed-lab/SEDSkill)

### 2022

- [ECCV 2022] Domain knowledge-informed self-supervised representations for workout form assessment. [PDF](https://arxiv.org/pdf/2202.14019) | [Github](https://github.com/ParitoshParmar/Fitness-AQA)
- [MICCAI 2022] Surgical skill assessment via video semantic aggregation. [PDF](https://arxiv.org/pdf/2208.02611) | [Github](https://github.com/shinkyo0513/Surgical-Skill-Assessment-via-Video-Semantic-Aggregation)
- [MICCAI 2022] Video-based surgical skills assessment using long term tool tracking. [PDF](https://arxiv.org/pdf/2207.02247)

### 2021

- [CVPR 2021] Towards unified surgical skill assessment. [PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Liu_Towards_Unified_Surgical_Skill_Assessment_CVPR_2021_paper.pdf)

- [MMSP 2021] Piano-Skills-Assessment. [DOI](https://doi.org/10.1109/MMSP53017.2021.9733638) | [Github](https://github.com/ParitoshParmar/Piano-Skills-Assessment)

### 2020

- [MICCAI 2020] Towards accurate and interpretable surgical skill assessment: A video-based method incorporating recognized surgical gestures and skill levels. [PDF](https://www.researchgate.net/profile/Tianyu-Wang-65/publication/345262769_Towards_Accurate_and_Interpretable_Surgical_Skill_Assessment_A_Video-Based_Method_Incorporating_Recognized_Surgical_Gestures_and_Skill_Levels/links/65e547c6adf2362b636a736c/Towards-Accurate-and-Interpretable-Surgical-Skill-Assessment-A-Video-Based-Method-Incorporating-Recognized-Surgical-Gestures-and-Skill-Levels.pdf)

### 2019 and Before

- [CVPR 2019] The pros and cons: Rank-aware temporal attention for skill determination in long videos. [PDF](https://openaccess.thecvf.com/content_CVPR_2019/papers/Doughty_The_Pros_and_Cons_Rank-Aware_Temporal_Attention_for_Skill_Determination_CVPR_2019_paper.pdf)
- [ICCVW 2019] Manipulation-skill assessment from videos with spatial attention network. [PDF](https://openaccess.thecvf.com/content_ICCVW_2019/papers/EPIC/Li_Manipulation-Skill_Assessment_from_Videos_with_Spatial_Attention_Network_ICCVW_2019_paper.pdf)
- [CVPR 2018] Who's better? who's best? pairwise deep ranking for skill determination. [PDF](https://openaccess.thecvf.com/content_cvpr_2018/papers/Doughty_Whos_Better_Whos_CVPR_2018_paper.pdf)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Datasets

| **Dataset**  | **Year** | **Modality**                          | **Domains**      | **# Classes** | **# Samples** | **# Avg. Frames**                                              | **Annotations**                               | **URL**                                                                  |
| ------------ | -------- | ------------------------------------- | ---------------- | ------------- | ------------- | -------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------ |
| MIT Olympic  | 2014     | Video, 2D Skeleton                    | Sports           | 2             | 309           | Dive: 150, Figure Skate: 4200                                  | Score                                         | [Link](https://userpages.cs.umbc.edu/hpirsiav/quality.html)              |
| UNLV Olympic | 2017     | Video                                 | Sports           | 3             | 717           | Dive: 150, Figure Skate: 4200, Vault: 75                       | Score                                         | [Link](http://rtis.oit.unlv.edu/datasets.html)                           |
| AQA-7        | 2019     | Video                                 | Sports           | 7             | 1189          | Dive: 97-105-156, Vault: 87, Big Air: 122-132, Trampoline: 634 | Score                                         | [Link](http://rtis.oit.unlv.edu/datasets/)                               |
| MTL-AQA      | 2019     | Video                                 | Sports           | 16            | 1412          | 96                                                             | Score                                         | [Link](https://github.com/Luciferbobo/DAE-AQA)                           |
| Fis-V        | 2019     | Video                                 | Sports           | 1             | 500           | 4300                                                           | TES PCS                                       | [Link](https://github.com/chmxu/MS_LSTM)                                 |
| RG           | 2020     | Video                                 | Sports           | 1             | 250           | 2375                                                           | Difficulty, Execution, Total                  | [Link](https://github.com/qinghuannn/ACTION-NET)                         |
| FineDiving   | 2022     | Video                                 | Sports           | 52            | 3000          | 105                                                            | Step, Score                                   | [Link](https://github.com/xujinglin/FineDiving)                          |
| FS1000       | 2023     | Video, Audio                          | Sports           | 7             | 1604          | 5000                                                           | TES PCS, detailed PCS                         | [Link](https://github.com/AndyFrancesco29/Audio-Visual-Figure-Skating)   |
| FineFS       | 2023     | Video, 2D/3D Skeleton                 | Sports           | 4             | 1167          | 5000                                                           | detailed Score, Subaction Class, Segmentation | [Link](https://github.com/yanliji/FineFS-dataset)                        |
| LOGO         | 2023     | Video                                 | Sports           | 12            | 200           | 5100                                                           | Action Class, Formation, Score                | [Link](https://github.com/shiyi-zh0408/LOGO)                             |
| GAIA         | 2024     | Video (AI Gen.)                       | All              | 510           | 9180          | 70                                                             | Subject, Completeness, Interaction            | [Link](https://github.com/zijianchen98/GAIA)                             |
| JIGSAWS      | 2014     | Video                                 | Skill Assessment | 3             | 103           | --                                                             | Surgemes Class, Rating                        | [Link](https://cirl.lcsr.jhu.edu/research/hmm/datasets/jigsaws_release/) |
| EPIC-Skills  | 2018     | Video                                 | Skill Assessment | 7             | 216           | --                                                             | Relative Rank                                 | [Link](https://github.com/hazeld/rank-aware-attention-network)           |
| BEST         | 2019     | Video                                 | Skill Assessment | 5             | 500           | 6400                                                           | Relative Rank                                 | [Link](https://github.com/hazeld/rank-aware-attention-network)           |
| PISA         | 2021     | Video, Audio                          | Skill Assessment | 1             | 992           | 160                                                            | Skill Level, Difficulty                       | [Link](https://github.com/ParitoshParmar/Piano-Skills-Assessment)        |
| TAQR         | 2024     | Video                                 | Skill Assessment | 4             | 300           | 488                                                            | Relative Rank                                 | [Link](https://github.com/MingZier/TAQR-Dataset)                         |
| UI-PRMD      | 2018     | 3D Skeleton, Joint Pos. & Ori.        | Medical Care     | 10            | 1326          | --                                                             | Binary Class                                  | [Link](https://webpages.uidaho.edu/ui-prmd/)                             |
| KIMORE       | 2019     | Video, 3D Skeleton, Joint Pos. & Ori. | Medical Care     | 5             | 1560          | --                                                             | Score                                         | [Link](https://vrai.dii.univpm.it/content/kimore-dataset)                |
| EHE          | 2021     | 3D Skeleton, Joint Pos. & Ori.        | Medical Care     | 6             | 869           | --                                                             | Binary Class                                  | [Link](https://github.com/bruceyo/egcnplusplus/tree/main/EHE_dataset)    |
| FineRehab    | 2024     | Video, 3D Skeleton, Joint Pos. & Ori. | Medical Care     | 16            | 4215          | --                                                             | Score                                         | [Link](https://bsu3dvlab.github.io/FineRehab/)                           |

<p align="right">(<a href="#readme-top">back to top</a>)</p>
