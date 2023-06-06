# NLP_Assignment
This Solution is to extract skill from the resumes provided as input of file like: PDF, IMAGE, WORD DOCUMENT,
Approach followed in building the solution:

    Prepared a dataset containing skills,

    Done preprocessing of data which involves:
        data cleaning, data formatting, tokenization, vectorization etc.

    Prepared the model using Cosine Similarity Algorithm.

Steps to trigger the model training:

    Trigger model training: Make Get Request From Postman,
        Request URL: "http://127.0.0.1:5000" (This is local hosted address, it might change in depending upon the port specified in different system.),
        Request Type: "GET" >> Send,
        Response: "Model Trained Successfully".

Steps to get extracted skills from resume:

    Get Extracted Skills: Make Post Request From Postman,

        Request URL: "http://127.0.0.1:5000" (This is local hosted address, it might change in depending upon the port specified in different system.),
        Request Type: "POST",
        Steps: Body: "form-data" >> Key: "file" (select = File in key panel) >> Value: "Select File" >> Send,
        Response: Extracted Skills from Resume: List Format. 


Libraries Used:

    Flask~=2.3.2 >> pip install flask,

    gensim~=4.3.1 >> pip install gensim,

    nltk~=3.8.1 >> pip install nltk,

    pandas==2.0.2 >> pip install pandas,

    pathlib~=1.0.1 >> default available in pyhon,

    Pillow~=9.5.0 >> pip install Pillow,

    pypdf2~=3.0.1 >> pip install PyPDF2,

    pytesseract~=0.3.10 >> pip install pytesseract,

    python-magic~=0.4.27 >> pip install python-magic,

    textract~=1.6.5 >> pip install textract


    