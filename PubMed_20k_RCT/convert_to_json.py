from cgitb import text
import json

# { abstract_id: str, sentences: [str], labels: [str] }

in_fps = ["./dev.txt", "./test.txt", "./train.txt"]

for fp in in_fps:

  with open(fp, "r") as in_file:
    text_data = in_file.readlines()


  # out_data = []

  with open(fp.replace(".txt", ".jsonl"), "w") as out_fp:
    for i, line in enumerate(text_data):
      if i == 0:
        inst = {}
        sentences = []
        labels = []

      if line.startswith("###"):
        if i != 0:
          inst['sentences'] = sentences
          inst['labels'] = labels

          out_fp.write(json.dumps(inst))
          out_fp.write("\n")

          inst = {}
          sentences = []
          labels = []
        
        inst['abstract_id'] = line.replace("###", "").strip()

      elif line.strip() != "" and line.strip() != "\n":
        labels.append(line.split("\t")[0].strip().lower())
        sentences.append(line.split("\t")[1].strip())

  
