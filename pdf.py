import enum
from weasyprint import HTML
import utils
import os
import chromedriver

def convert_htmls(remove_guid = False, use_chrome = False, preserve_hierarchy = False):
  '''
  Use weasyprint to convert htmls to pdf files if not specified
  '''
  try:
    output_path = utils.create_dir('pdf')
    htmls = utils.get_all_htmls(utils.get_file_path(), 'html')
    if use_chrome:
      convert_htmls_chrome(output_path, htmls, remove_guid)
    else:
      convert_htmls_weasy(output_path, htmls, remove_guid)
   
  except Exception as e:
    print(f"Catch an exception: {str(e)}")


def convert_htmls_weasy(output_path, htmls, remove_guid):
  for i, (level, root, filename) in enumerate(htmls):
    outname = retrieve_outname(remove_guid, filename)    
    document = HTML(filename).render()        
    document.write_pdf(target=f"{output_path}\{outname}.pdf")
    utils.printProgressBar(i, len(htmls) - 1, prefix = 'Progress:', suffix = 'Complete', length = 50)

def convert_htmls_chrome(output_path, htmls, remove_guid):
  driver = chromedriver.set_driver(output_path)
  for i, (level, root, filename) in enumerate(htmls):
    outname = retrieve_outname(remove_guid, filename)        
    driver.get(filename)
    driver.execute_script('window.print();')
    utils.printProgressBar(i, len(htmls) - 1, prefix = 'Progress:', suffix = 'Complete', length = 50)
  driver.quit()


def retrieve_outname(remove_guid, filename) -> str:
  outname = os.path.basename(filename).split('.')[0]
  return ' '.join(outname.split(' ')[:-1]) if remove_guid else outname