import pdf
import sys
import os.path

if __name__ == "__main__":  
  if len(sys.argv) == 2 and sys.argv[1].lower() == '-c':
    pdf.convert_htmls(remove_guid=True, use_chrome=True)
  else:
    pdf.convert_htmls(remove_guid=True)
  print("Done!")    
  

# Pending:
  # Preserve directory hierarchy
  # Combine all pdfs to one single file