# YOLOv8 Data Augmentation Guide

This guide explains how to augment your data for the YOLOv8 object detection model and outlines the steps involved. Data
augmentation can help your model learn better and achieve higher accuracy.

## Requirements

To use this data augmentation guide, you'll need the following requirements:

- Python 3.x
- YOLOv8 installed and up and running
- Relevant dataset: This guide works with two main folders named "base_path" and "destination_path." "base_path"
  contains your original dataset, while "destination_path" will contain the augmented dataset. Additionally, within "
  base_path," there should be two subfolders named "images" and "labels."

## File Structure

The project expects the following file structure:

```
    base_path/
    |-- images/
    |   |-- image1.jpg
    |   |-- image2.jpg
    |   |-- ...
    |-- labels/
    |   |-- image1.txt
    |   |-- image2.txt
    |-- ...
```

## Usage

1. Clone this repository or download it as needed.
2. Ensure that your YOLOv8 model is installed and operational.
3. Place the original image files and label files in the "base_path" folder.
4. Run this command script in the main directory:

```bash
    python augmentation.py
```

5. When the process is complete, you can find the augmented dataset and labels in the "destination_path" folder.

## Example Usage

Here is an example command on how to use the data augmentation process:

```bash
python augmentation.py
```

This command will create the augmented dataset in the "destination_path" folder using the original dataset in the "
base_path" folder.

Mix Example Usage
If you want to use multiple methods together, you can write your code like this:

```python
brightness.mix(saturation.mix(hue.mix(exposure.mix(count=1), count=1), True)
```

The resulting image name will be in the following format:

```bash
image1-exposure-0.9358-hue-0.915-saturation-1.0685-brightness-0.9676.jpg
```

The mix function has 3 parameters:

1. classes: If you want to use another method before this one, you should create the class of the desired method and
   write
   it here.

2. is_last: This parameter should only be used in the outermost area to understand that the process is nearing
   completion.

3. count: If you want to update the data amount, this field has been added.

## License

This project is licensed under the MIT License. For more information, please refer to the [LICENSE](LICENSE.txt) file.

## Contribution

To contribute, please refer to the [contributions.md](contributions.md) file. Feel free to contribute!

## Contact

For questions or suggestions, please feel free to contact:

Muhammet Mustafa KOÇ <br>
Email: mmstfkc23.61@gmail.com

This README file provides detailed information about data augmentation with YOLOv8 and explains the steps to users.
Please tailor the requirements, usage instructions, license information, and contact details to your project as needed.