# YOLOv8 Data Augmentation Guide

This guide explains how to augment your existing data for the YOLOv8 object detection model and provides the steps for
the data augmentation process. Data augmentation can help your model learn better and achieve higher accuracy.

## Requirements

To use this data augmentation guide, you need the following requirements:

- Python 3.x
- YOLOv8 installed and operational
- Relevant dataset: This guide works with two main folders named "base_path" and "destination_path." "base_path"
  contains your original dataset, while "destination_path" will contain the augmented dataset. Additionally, within "
  base_path," there should be two subfolders named "images" and "labels."

## File Structure

To use the project, your files should follow the following structure:

- `base_path`: The main data directory.
    - `images`: Subdirectory containing image files. Image files should have the .jpg or .jpeg extension.
    - `labels`: Subdirectory containing label files. Label files should have the .txt extension and the same name as the
      corresponding images.

For example, the file structure should look like this:

```
base_path/
|-- images/
| |-- image1.jpg
| |-- image2.jpg
| |-- ...
|-- labels/
| |-- image1.txt
| |-- image2.txt
| |-- ...
```

## Usage

1. Clone this repository or download it as needed.
2. Ensure that your YOLOv8 model is installed and running.
3. Place the original images and label files in the "base_path" folder.
4. Run the command script in the root directory.

    ```bash
    python augmentation.py
    ```

5. When the process is complete, you can find the augmented dataset and labels in the "destination_path" folder.

## Example Usage

Below is an example command on how to use the data augmentation process:

```bash
python augmentation.py
```

This command uses the original dataset from the "base_path" folder to create an augmented dataset in the "
destination_path" folder.

## License
This project is licensed under the MIT License. For more information, refer to the [LICENSE](LICENSE.txt) file.

## Contributing
Check the [contributions.md](contributions.md) file for information on contributing. Feel free to contribute!

## Contact
For questions or suggestions, please feel free to contact us.

Muhammet Mustafa KOÇ
mmstfkc23.61@gmail.com

This README file provides detailed information about data augmentation with YOLOv8 and explains the steps to users.
Please adjust the requirements, usage instructions, license details, and contact information to fit your project's
needs.
