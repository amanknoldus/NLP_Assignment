from pathlib import Path
from nltk.corpus import stopwords

path = Path(__file__).resolve().parent.parent
data_path = path / "dataset"
resume_path = data_path / "resumes"
file_path = data_path / "extraction_skill.csv"


stopwords = set(stopwords.words("english"))

