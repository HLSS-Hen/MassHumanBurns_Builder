# MassHumanBurn Dataset Generator

This repository contains the dataset generation code for **MassHumanBurn**, a synthetic dataset of 3D human models with burn injuries. The dataset is designed for training and evaluating deep learning models for burned total body surface area (TBSA) estimation from 2D masks, as described in the paper:

> **BurnAreaNet: A Deep Learning Method for Estimating Burned Total Body Surface Area from 2D Masks**

The generated dataset is available on Hugging Face:  
[MassHumanBurns](https://huggingface.co/datasets/HLSS/MassHumanBurns)

## Overview

This codebase generates synthetic 3D human meshes with simulated burn patterns and exports corresponding 2D masks. The generation pipeline uses [MakeHuman](https://static.makehumancommunity.org/makehuman.html) to create base human meshes, which are then processed to apply realistic burn region distributions.

The pipeline produces the following outputs:
- **Synthetic RGB renderings** of burned human models
- **Binary burn masks** indicating affected regions
- **Metadata** including TBSA percentages
While the BurnAreaNet model described in the paper primarily relies on the 2D mask data, the RGB renderings are also provided to support potential downstream tasks may benefit from visual input.

## License
This project is licensed under the Apache License 2.0.

## Citation
If you use this dataset or code in your research, please cite:
```bibtex
@article{burnareanet,
  title={BurnAreaNet: A Deep Learning Method for Estimating Burned Total Body Surface Area from 2D Masks},
  author={Hao Wang, Kaize Zheng, Shuaidan Zeng, Yanyan Liang, Zhu Xiong},
  year={2026}
}
```
