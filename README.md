
# ButlerManagementSystem-solution

## how do run the code?

1. ```  cd '{target directory}'   ```

2. ```  pip install -r ./requirements.txt   ```

3. ```  python main.py   ```

4. ```  python JSON_.py   ```

## what does these code do?

1. **main.py**: \n1. This demo will randomly generate items for testing. \n2. This demo will check whether the input name exists or not automatically (under current folder) \n3. Generated data will be appended into an existing file, or created a new file. \nPlease input a file name for testing (Case sensitive!!!); e.g. "sample.json" or "new_file.json"\n'.

```  
pip install snscrape
```

2. **data**: all data are put under this folder; please donot change any file's location or name under this folder, or it will cause loading paths errors. If adding folder or chaning names of folder is necessary, please direct to **Config.py** and make corresponsing changes firstly.

3. **Config.py**: Again! Go to this file for making any changes on settings paths. And the system will load changes automatically

4. **ModelPrediction.py**: apply selected model and make the prediction. ```single_list_pred()``` applies to a list, and ```folder_pred()``` applies to a folder.

5. **Models.py**: storing models' details

6. **NaturalLangProcessing.py**: do NLP prepreocessing stuffs...

7. **nice_functions.py**: includes some fundamental, common, and useful functions, like reading file; reading dictionary; calculating ambilence and generating results; writing contents to tsv (most data are stored as .tsv) ...

8. **RAEDFILE.py**: most of operations on folder and files are stored at here; It also has checking-path function (setting ```CHECK_PATH=True``` when calling readFile class)

9. **scraperData.py**: all codes of scrapering data are stored there.
    - reading keyword file, and storing data based on the keyword category
    - obtaining the lastest date of existing file of selected keyword, and then scrapering data from lastest date to today
    - we keep the file with a reasonable size for speeding the process of reading file and saving PC momery
        + if a file has more than 49999 lines, the system will create a new file with selected keyword with a newer timestamp
        + if an time-range inputting of a keyword is longer than 1 hour, the system will stop this keyword and continue to the next keyword
10. **test.ipynb**, **test.py** and **test.tsv** are for usage of testing.

11. **TextData.py**: defining the ```Dataset``` class, which stores data for machine learning. Refer to this file for more details.

12. **timeGen.py**: all time-related generators

13. **news.py**: all processing functions about news are stored there, like parsing news raw file (HTML format); writing parsing data into .tsv; we also created a new keyword list, including districts, places, events, and attractions in HongKong. Then, ```filter_out_news_based_on_filterwords()``` can filter out news based on the new keyword list.

# **Bonus**

## install CUDA (optional)

1. check your GPU version. e.g. NVIDIA GeForce RTX 3060 Ti

2. google 'CUDA Capability GPU': https://developer.nvidia.com/cuda-gpus, and find the compatible version of CUDA e.g. >=8.6

3. download CUDA toolkit: https://developer.nvidia.com/cuda-downloads

4. download pytorch: https://pytorch.org/

## generate requirements.txt (optional)

``` 
python -m  pipreqs.pipreqs --encoding utf-8  ./ --force 
```

## converting markdown to PDF (optional)

1. search ```Markdown PDF``` within extension

2. press ```F1```

3. select or input: ```markdown-pdf: Export (pdf)```


## topic modelling

1. fix GPU issue when appling Top2Vec:
    https://stackoverflow.com/questions/59823283/could-not-load-dynamic-library-cudart64-101-dll-on-tensorflow-cpu-only-install