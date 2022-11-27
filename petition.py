from docx import Document
import re 

file_path = "template.docx"

replacement_list = [("<p_no>","0987323"),("<cm>","341"),("<inches>","134")]
doc = Document(file_path)
for para in doc.paragraphs:
            # Loop through runs (style spans)
            for run in para.runs:
                # if there is text on this run, replace it
                if run.text:
                    
                    if "p_no" in  run.text :
                        replaced_text = re.sub("p_no", "1434343", run.text, 999)
                    elif "cunt" in run.text: 
                        replaced_text = re.sub("cunt", "1434343", run.text, 999)
                    elif "dick" in run.text: 
                        replaced_text = re.sub("dick", "1434343", run.text, 999)
                    else:
                        replaced_text = run.text
                    if replaced_text != run.text:
                        # if the replaced text is not the same as the original
                        # replace the text and increment the number of occurences
                        run.text = replaced_text

new_file_path = file_path.replace(".docx", "_new.docx")
# save the new docx file
doc.save(new_file_path)