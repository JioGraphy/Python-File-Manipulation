import xml.etree.ElementTree as ET

def parse_xml_et(fn):

        tree = ET.parse(fn)
        root = tree.getroot()
        print('Domains for: ' + root.attrib['name'])

        for child in root:
            print('\t' + child.attrib['name'], child.tag)


def add_xml_element(fn, el, attr, val):
      
      tree = ET.parse(fn)
      root = tree.getroot()
      child = ET.Element(el)
      child.attrib[attr] = val
      root.append(child)
      tree.write(fn)


def change_xml_element_et(fn, el, attr, oldval, newval):
      
      tree = ET.parse(fn) # read the XML file, parsing
      root = tree.getroot() # get the main node of the XML
      child = root.find("./" + el + "[@" + attr + "='" + oldval + "']")
      child.attrib[attr] = newval
      tree.write(fn) 


with open('./files-to-read/stack.txt') as stack:
    add_xml_element('./files-to-read/author.xml', 'domain', 'name', stack)
    # print(stack.read())


# add_xml_element('./files-to-read/author.xml', 'domain', 'name', stack)
# change_xml_element_et('./files-to-read/author.xml', 'domain', 'name', 'SQL', 'SQLlite') 
# parse_xml_et('./files-to-read/author.xml')
 

# skills = ['SQL', 'Linux', 'Bash']

# for tech in skills:
#       skill = tech
#       add_xml_element('./files-to-read/author.xml', 'domain', 'name', skill)
#       print(f'Successfully added: {skill}')




    