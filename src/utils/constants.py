from pathlib import Path
from nltk.corpus import stopwords

path = Path(__file__).resolve().parent.parent
data_path = path / "dataset"
resume_path = data_path / "resumes"

stopwords = set(stopwords.words("english"))
