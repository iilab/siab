#! /usr/bin/python

import urllib
import json
from sys import argv
import os
from slugify import slugify
import xml.etree.ElementTree as ET
import codecs

### Usage
usage_string = """
Usage: %s [<nid>] <directory>

<nid>:                The Drupal node ID for a Community Guide "wrapper." If
                      provided, only data from that node will be extracted.
                      If ommitted, all known published nodes will be extracted.

<directory>:          The directory within which one or more Tool and/or Tactics
                      Guides will be extracted as .json serializations and/or 
                      .md data structures. 

Python dependencies: python-slugify,  python-xml, ???
""" % argv[0]

### List of underlying guides (not Community Guide "wrappers") to skip
skip_list = { '342', '2525', '1597' }

### DEBUG: All (underlying) Tactics Guide and Tool Guide nids
# 
skip_list = { '342', '2525', '1420', '436', '396', '140', '578', '1466', '2243','2186', '465', '2219', \
                  '2222', '473', '597', '484', '620', '494', '638', '656', '512', '527', '674', '693', '539', \
                  '707', '549', '2216', '2250', '1489', '2225', '2228', '712', '768', '785', '2178', '2182', '2247', \
                  '2141', '818', '1402', '1008', '1026', '1032', '1047', '1056', '1064', '1074', '1407', \
                  '1085', '1104', '1107', '1113', '1115', '1117', '2394', '2409', \
                  '2398', '2405', '2422', '2412', '2429', '1597' }  # '380', '1434', '1082', '1084', '1154', '1326', '1333', '1185', '1119'

### List of legacy Tactics and Tool Guides to skip
legacy_skip_list = { '2086', '2099', '2119', '2152', '2116', '2121', '2124', '2127', '2128', '2133' }

if len(argv) < 2 or len(argv) > 3:
    print usage_string
    exit(2)

if len(argv) == 2:
    script, output_directory = argv
    input_nid = "all"

if len(argv) == 3:
    script, input_nid, output_directory = argv

### Return output of json.loads() on the string returned by the Drupal API at the specified nid
def fetch_nid(lang, nid):
    node_url = "https://securityinabox.org/%s/api/node/%s" % ( lang, nid )
    nh = urllib.urlopen(node_url)
    nj = nh.read()
    n_data = json.loads(nj)
    return n_data

### Build a community-appropriate URL for a Tactics Guide from a nid
def construct_tag_link(cg_data, nid):
    community = cg_data['field_relevant_community']['en'][0]['value']
    n_data = fetch_nid('en', nid)
    n_trans_title = n_data['field_htb_translatable_title']['en'][0]['value']
    n_title = n_data['title']
    output_url = "https://securityinabox.org/en/" + community.lower() + "/" + n_title.lower()
    output_dict = { "title": n_trans_title, "url": output_url }
    return output_dict

### Deal with a Tactics Guide Section Feature by constructing a node containing either
### a community-aware link to a Tool Guide or the text of a community snippet: 
### 
###   - For Tool Guide nids ("Hands on: Get started with <tool>"), we call construct_tog_link(); 
###   - For Snippet Selector nids (e.g. https://securityinabox.org/en/api/node/127.json), we call construct_tag_snippet()
def construct_tag_feature(cg_data, nid):
    community = cg_data['field_relevant_community']['en'][0]['value']
    n_data = fetch_nid('en', nid)
    if n_data['type'] == "hands_on_guide":
        return construct_tog_link(cg_data, n_data)
    elif n_data['type'] == "htb_snippet_selector":
        return construct_tag_snippet(cg_data, n_data)
    else:
        print "Attempted to construct a Tool Guide Feature from a nid that is neither a Snippet nor a Tool Guide"
        exit(2)
    
### Build a community-aware URL for a Tool Guide from the json data for a Tool Guide
def construct_tog_link(cg_data, n_data):
    n_trans_title = n_data['field_hog_translatable_title']['en'][0]['value']
    tool_guide_nid = n_data['nid']
    community_tactics_guide_wrapper_nid = cg_data['nid']
    ### Use the get_hog_pointer View (now exposed as an RSS feed) to get full Community Tool Guide URL. The View takes: 
    ###
    ###   - The nid of the underlying Tool Guide wrapped by the Community Tool Guide for which we want a URL
    ###   - The nid of the Community Tactics Guide (wrapper) where the "Hands-on: Get started with <tool>"
    ###     link is to be displayed. (This node is used to determine both the community and--absurdly--the OS suffix)
    view_url = "https://securityinabox.org/en/get_hog_pointer/%s/%s" % \
        ( tool_guide_nid, community_tactics_guide_wrapper_nid )
    vh = urllib.urlopen(view_url)
    vrss = vh.read()
    ### Extract correct URL (including OS suffix) from (RSS) XML returned by get_hog_pointer view
    vrsstree = ET.fromstring(vrss)
    output_url = vrsstree.findtext('./channel/item/link')
    output_dict = { "title": n_trans_title, "url": output_url }
    return output_dict

### Extract a community Snippet from the json data for a How-to Booklet Snippet Selector
### There are 14 Snippet Selector nids: 379, 127, 128, 129, 130, 507, 509, 1315, 1316, 1317, 1318, 1319, 1320, and 1321
def construct_tag_snippet(cg_data, s_data):
    community = cg_data['field_relevant_community']['en'][0]['value']
    snippet_index = int(s_data['field_ordinal_selector']['und'][0]['value'])
    snippet_position = str(snippet_index + 1)
    s_title = "Snippet %s for the %s community" % ( snippet_position, community )
    ### TODO: Deal gracefully with cases where there are _some_ snippets, but not enough
    if cg_data['field_guide_snippets']:
        ### DEBUG
        # print "About to process %s" % s_title
        s_text = cg_data['field_guide_snippets']['und'][snippet_index]['value']
        output_dict = { "title": s_title, "value": s_text }
        return output_dict
    else:
        return s_data

### Fetch Tool Guide (ToG)
def fetch_tog(cg_data):

    ### Replace Tool Guide Section nid-stubs with data from the nids specified as "field_hog_element" in the underlying Tool Guide
    cg_data['field_guide']['und'][0]['field_hog_element']['und'] = \
        [fetch_nid('en', tog_section['target_id']) for tog_section in cg_data['field_guide']['und'][0]['field_hog_element']['und']]
    
    ### Replace Tool nid-stub with data from the nid specified as "field_hog_tool" in the underlying Tool Guide
    cg_data['field_guide']['und'][0]['field_hog_tool']['und'] = \
        [fetch_nid('en', tool['target_id']) for tool in cg_data['field_guide']['und'][0]['field_hog_tool']['und']]

    ### Replace Required Reading nid-stubs with the translatable titles of the nids specified as "field_hog_required_read" in the underlying Tool Guide
    if cg_data['field_guide']['und'][0]['field_hog_required_read']:
        lang = 'en' if cg_data['field_guide']['und'][0]['field_hog_required_read'].has_key('en') else 'und'
        cg_data['field_guide']['und'][0]['field_hog_required_read'][lang] = \
            [construct_tag_link(cg_data, required_reading['target_id']) \
                 for required_reading in cg_data['field_guide']['und'][0]['field_hog_required_read'][lang]]
    
    return cg_data

### Fetch Tactics Guide (TaG)
def fetch_tag(cg_data):

    ### Replace Tactics Guide Section nid-stubs with data from the "field_htb_chapter_element" nids specified in the underlying Tactics Guide
    cg_data['field_guide']['und'][0]['field_htb_chapter_element']['und'] = \
        [fetch_nid('en', tag_section['target_id']) for tag_section in cg_data['field_guide']['und'][0]['field_htb_chapter_element']['und']]

    ### Replace Tactics Guide Section Feature nid-stubs with data from the...
    ### 
    ###   - field_htb_chapter_feature_top, 
    ###   - field_htb_chapter_feature, and 
    ###   - field_htb_chapter_feature_bottom
    ### 
    ### ...nids specified in the Tool Guide Section. 
    for section in cg_data['field_guide']['und'][0]['field_htb_chapter_element']['und']:
        if section['field_htb_chapter_feature_top']:
            lang = 'en' if section['field_htb_chapter_feature_top'].has_key('en') else 'und'
            section['field_htb_chapter_feature_top']['und'] = \
                [construct_tag_feature(cg_data, top_feature['target_id']) \
                     for top_feature in section['field_htb_chapter_feature_top']['und']]
        if section['field_htb_chapter_feature']:
            lang = 'en' if section['field_htb_chapter_feature'].has_key('en') else 'und'
            section['field_htb_chapter_feature']['und'] = \
                [construct_tag_feature(cg_data, middle_feature['target_id']) \
                     for middle_feature in section['field_htb_chapter_feature']['und']]
        if section['field_htb_chapter_feature_bottom']:
            lang = 'en' if section['field_htb_chapter_feature_bottom'].has_key('en') else 'und'
            section['field_htb_chapter_feature_bottom'][lang] = \
                [construct_tag_feature(cg_data, bottom_feature['target_id']) \
                     for bottom_feature in section['field_htb_chapter_feature_bottom'][lang]]
    return cg_data

### Fetch a Community title
def construct_community(nid):
    c_data = fetch_nid('en', nid)
    c_title = c_data['field_menu_title_community']['und'][0]['value']
    c_value = c_data['title']
    output_dict = { "title": c_title, "value": c_value }
    return output_dict

### Fetch a Tactics or Tool Guide and write its content to a json file
# 
# TODO: This "already fetched" logic is a bit tortured. Would be cleaner to follow the Drupal data model
#       and separate underlying content entirely from CG wrappers...
def fetch_guide(nid, underlying_guides_already_fetched):

    ### Get top-level Community Guide "wrapper"
    cg_data = fetch_nid('en', nid)
    ### The nid of the underlying guide wrapped by this Community Tactics or Tool Guide
    underlying_guide = cg_data['field_guide']['und'][0]['target_id']

    if underlying_guide in skip_list:
        ### Avoid fetching the rest of the guide if it's on the skip_list
        print "Skipping (cg: %s) <- (g: %s) or already have the underlying content." % ( nid, underlying_guide )        

    else: 
        print "Fetching or stubbing out (cg: %s) <- (g: %s)" % ( nid, underlying_guide )
    
        ### Replace underlying Guide nid-stub with data from the nid specified as "field_guide" in the Community Guide wrapper
        cg_data['field_guide']['und'] = [fetch_nid('en', guide['target_id']) for guide in cg_data['field_guide']['und']]

        ### Replace relevant community nid-stub with data from the nid specified as "field_relevant_community" in the Communigy Guide wrapper
        cg_data['field_relevant_community']['en'] = \
            [construct_community(community_nid['target_id']) for community_nid in cg_data['field_relevant_community']['en']]
        output_community_segment = slugify(cg_data['field_relevant_community']['en'][0]['value'])

        ### Determine whether we're fetching a Tactics Guide or a Tool Guide. If we have not yet seen this underlying content
        ### fetch it. If we have, create a YAML stub
        guide_type = cg_data['field_guide']['und'][0]['type']
        if guide_type == "how_to_booklet_chapter":
            output_title_field = "field_htb_translatable_title"
            output_type_segment = "tactics"
            output_os_segment = ""
            cg_data = cg_data if underlying_guides_already_fetched.has_key(underlying_guide) else fetch_tag(cg_data)
        elif guide_type == "hands_on_guide":
            output_type_segment = "tools"
            output_os_segment = cg_data['path'].split("/").pop()
            output_title_field = "field_hog_translatable_title"
            cg_data = cg_data if underlying_guides_already_fetched.has_key(underlying_guide) else fetch_tog(cg_data)
        else:
            print "Attempted to fetch a node that is neither a Community Tactics Guide nor a Community Tool Guide"
            exit(2)

        ### Assemble remaining namespace values for .json output and front_matter values for md formatting and output
        output_ordinal = cg_data['field_weight_in_lists']['und'][0]['value'].zfill(3) if cg_data['field_weight_in_lists'] else '100'
        output_node = cg_data['nid'].zfill(4)
        guide_title = cg_data['field_guide']['und'][0][output_title_field]['en'][0]['value']
        output_title = slugify(guide_title)
        output_filename = "%s-node_%s-%s.json" % ( output_ordinal, output_node, output_title )
        output_path = os.path.join(output_directory, "json", "en", output_community_segment, output_type_segment)
        output_path = os.path.join(output_path, output_os_segment) if guide_type == 'hands_on_guide' else output_path

        ### Write guide as .json
        output_json(output_path, output_filename, cg_data, False)

        ### Assemble remaining namespace values to output .md stub or as master source for future community guides 
        ### based on this underlying content
        output_filename = "index.md"
        output_guide_folder = "%s-%s" % ( output_ordinal, output_title )
        output_path = os.path.join(output_directory, "md", "en", output_community_segment, output_type_segment)
        output_path = os.path.join(output_path, output_os_segment) if guide_type == 'hands_on_guide' else output_path
        output_path = os.path.join(output_path, output_guide_folder)

        ### Create .md YAML stub and output snippets if underlying content has already been fetched
        if underlying_guides_already_fetched.has_key(underlying_guide):
            content_source = underlying_guides_already_fetched[underlying_guide]
            front_matter = "---\nsource: %s\n---\n" % content_source
            formatted_output = front_matter
            write_output(output_path, output_filename, formatted_output)
            ### Write out snippets for non-master community guide wrappers
            if output_type_segment == "tactics" and cg_data['field_guide_snippets']:
                output_path = os.path.join(output_path, "snippets")
                snippet_position = 1
                for snippet in cg_data['field_guide_snippets']['und']:
                    snippet_filename = "snippet_%s" % str(snippet_position).zfill(2)
                    write_output(output_path, snippet_filename, snippet['value'])
                    snippet_position = snippet_position + 1

        else:
            ### Assemble absolute URL to this .md file as master source for future community guides based upon it
            content_source_folder = output_guide_folder
            content_source = os.path.join("/", output_community_segment, output_type_segment)
            content_source = os.path.join(content_source, output_os_segment) if guide_type == 'hands_on_guide' else content_source
            content_source = os.path.join(content_source, content_source_folder)
    
            ### Write guide as markdown if this is the first time we've seen this underlying content
            if output_type_segment == "tactics":
                front_matter = [ "en", output_community_segment, output_type_segment, output_ordinal, guide_title ]
                output_tactic_md( front_matter, cg_data)
            elif output_type_segment == "tools":
                front_matter = [ "en", output_community_segment, output_type_segment, output_os_segment, output_ordinal, guide_title ]
                output_tool_md( front_matter, cg_data)

        ### Return nid of underlying guide and source of "master" so we can update our list of guides not to fetch again
        return ( underlying_guide, content_source )

### Fetch all Tactics and Tool Guides and write their contents to a json file
def fetch_all_guides():
    ### Get a list of all guide nids from an RSS Drupal view at: 
    ### https://securityinabox.org/en/all-guides-feed
    ### THIS LIST MUST BE SORTED so that default ("guide") community guides 
    ### are returned first
    view_url = "https://securityinabox.org/en/all-guides-feed"
    vh = urllib.urlopen(view_url)
    vrss = vh.read()

    ### Extract all nids 
    vrsstree = ET.fromstring(vrss)
    guides = vrsstree.findall('./channel/item/guid')
    guides = [guide.text for guide in guides]

    ### Make sure we really want to do this
    raw_input("""
Press <Enter> to check %s English guides and fetch all those with 
unique ("underlying") content. This should include about 70 English
guides and about 30 multilingual "Legacy" guides. It should total 
about 200 MB of data and may take up to 45 minutes.
Press <Ctrl>-C to exit\n""" % len(guides))


    ### A running list of the underlying Tactics and Tactics guides that we have already fetched and printed
    underlying_guides_already_fetched = dict()

    ### Fetch all guides
    for guide in guides:
        guide_to_cg_map = fetch_guide(guide, underlying_guides_already_fetched)
        if guide_to_cg_map:
            underlying_nid, source_url = guide_to_cg_map
            underlying_guides_already_fetched[underlying_nid] = source_url

    print "\nFetched %s guides" % len(underlying_guides_already_fetched)

### Selectively preserve fields of a particular language in a Legacy book page (parent or child)
def construct_language_specific_legacy_page(lang, legacy_data):
    language_version = dict()
    short_lang = lang.split("-")[0]
    if not legacy_data['title_field'].has_key(lang):
        return dict()
    else:
        for field in legacy_data:
        ### DEBUG
        # print "Field: %s" % field
            if legacy_data[field] and isinstance(legacy_data[field], dict) and legacy_data[field].has_key(lang):
                language_version[field] = dict()
                language_version[field][short_lang] = legacy_data[field][lang]
            else:
                language_version[field] = legacy_data[field]

        return language_version

### Fetch a single Legacy Tactics or Tool Guides and write its contents (including book children) to a json file
def fetch_legacy_guide(nid, legacy_index):

    print "Fetching (lg: %s)" % nid
    
    ### Fetch the book parent
    legacy_data = fetch_nid('en', nid)

    ### Fetch data from book children and add them as elements of a list referenced by the 'book_children' key
    legacy_data['book_children'] = [fetch_nid('en', book_child_nid) for book_child_nid in legacy_index[nid]]

    ### Create language-specific versions of the guide
    for lang in legacy_data['title_field']:
        ### DEBUG
        print "  - Isolating %s version" % lang
        
        ### Prune other languages from book_parent
        language_version = construct_language_specific_legacy_page(lang, legacy_data)

        ### Prune other languages from book_children
        language_version['book_children'] = \
            [construct_language_specific_legacy_page(lang, book_child) for book_child in language_version['book_children']]

        ### Extract namespace values
        guide_type = legacy_data['type']
        if guide_type == 'legacy_how_to_booklet_chapter':
            output_type_segment = "tactics"
            output_os_segment = ""
        elif guide_type == 'legacy_hands_on_guide':
            output_type_segment = "tools"
            os_taxonomy_term = legacy_data['field_legacy_hog_category']['xx'][0]['tid']
            if os_taxonomy_term == "114":
                output_os_segment = "android"
            elif os_taxonomy_term == "115":
                output_os_segment = "windows"
            elif os_taxonomy_term == "117":
                output_os_segment = "internet"
            else:
                print "Attempted to fetch a legacy Tool Guide that is not for Windows, Internet or Android"
                exit(2)
        else:
            print "Attempted to fetch a legacy guide that is neither a Legacy Hands-on Guide or a Legacy How-to Booklet Chapter"
            exit(2)
        
        ### Assemble remaining namespace values for .json output and front_matter values for md formatting and output
        output_ordinal = language_version['field_weight_in_lists']['und'][0]['value'].zfill(3)
        output_node = language_version['nid'].zfill(4)
        guide_title = legacy_data['title_field']['xx'][0]['value']
        output_title = slugify(guide_title)
        output_filename = "%s-node_%s-%s.json" % ( output_ordinal, output_node, output_title )
        output_lang_segment = lang.split("-")[0] 
        output_path = os.path.join(output_directory, "json", output_lang_segment, "guide", output_type_segment)
        output_path = os.path.join(output_path, output_os_segment) if guide_type == 'legacy_hands_on_guide' else output_path

        ### Write language-version of full Legacy guide as .json
        # TODO: Confirm that we want translated .json content as \uXXXX-encoded ascii rather than Unicode.
        output_json(output_path, output_filename, language_version, True)
        
        ### Write language-version of full legacy guide as Markdown
        if output_type_segment == "tactics":
            front_matter = [ output_lang_segment, "guide", output_type_segment, output_ordinal, guide_title ]
            output_legacy_tactic_md(front_matter, language_version)
        elif output_type_segment == "tools":
            front_matter = [ output_lang_segment, "guide", output_type_segment, output_os_segment, output_ordinal, guide_title ]
            output_legacy_tool_md( front_matter, language_version)

### Request a list of all legacy nids, and their parent nids, from the all-legacy-nodes-feed RSS View
def create_legacy_guide_index():
    view_url = "https://securityinabox.org/en/all-legacy-nodes-feed"
    vh = urllib.urlopen(view_url)
    vrss = vh.read()
    vrsstree = ET.fromstring(vrss)
    legacy_nodes = vrsstree.findall('./channel/item')
    legacy_index = dict()
    for legacy_node in legacy_nodes:
        ### guid = nid; description = nid of book parent
        this_child_node = legacy_node.findtext('guid')
        book_parent = legacy_node.findtext('description')
        ### legacy_index is a dict of lists; each key is a book parent nid; each list contains the book children nids
        list_of_book_children = legacy_index[book_parent] if legacy_index.has_key(book_parent) else list()
        list_of_book_children.append(this_child_node)
        legacy_index[book_parent] = list_of_book_children
    return legacy_index

### Fetch all Legacy Tactics and Tool Guides and write their contents to a json file
def fetch_all_legacy_guides():
    legacy_index = create_legacy_guide_index()
    num_legacy_guides = 0
    for legacy_nid in legacy_index:
        if legacy_nid not in legacy_skip_list:            
            fetch_legacy_guide(legacy_nid, legacy_index)
            num_legacy_guides = num_legacy_guides + 1
    print "\nFetched %s multilingual legacy guides" % num_legacy_guides
        
### TODO: Flesh out validation logic
def validate_nid(nid):
    legacy_index = create_legacy_guide_index()

    if legacy_index.has_key(nid):
        fetch_legacy_guide(nid, legacy_index)
    else:
        fetch_guide(nid, set())

### Format json output and send it to be written
def output_json(output_path, output_filename, output_data, ascii):
    formatted_output = json.dumps(output_data, indent=4, sort_keys=True, ensure_ascii=ascii)
    write_output(output_path, output_filename, formatted_output)
    
### Format Markdown output for an English Tactics Guide and send it to be written
def output_tactic_md(front_matter, output_data):
    guide_lang, guide_community, guide_type, guide_weight, guide_title = front_matter
    formatted_output = """
---

lang: %s
community: %s
type: %s
weight: %s
title: %s

---

""" % ( guide_lang, guide_community, guide_type, guide_weight, guide_title )

    ### Format intro
    if output_data['field_guide']['und'][0]['field_htb_introduction']:
        formatted_output += output_data['field_guide']['und'][0]['field_htb_introduction']['en'][0]['value'] + "\n\n"

    ### Format "What you can learn from this guide"
    if output_data['field_guide']['und'][0]['field_htb_learning_goals']:
        formatted_output += "# What you can learn from this guide\n\n"
        for learning_goal in output_data['field_guide']['und'][0]['field_htb_learning_goals']['en']:
            formatted_output += "- %s\n" % learning_goal['value']

    ### Format Tactics Guide Sections
    # TODO: Move chapter_element code to a function
    snippet_position = 1
    snippet_output_guide_folder = "%s-%s" % ( guide_weight, slugify(guide_title) )
    snippet_path = os.path.join(output_directory, "md", guide_lang, guide_community, guide_type, snippet_output_guide_folder, "snippets")
    snippet_placeholder = "\n:[](snippets/%s)\n\n"
    tool_pointer_placeholder = "\n:[](../../tools/%s)\n\n"
    for section in output_data['field_guide']['und'][0]['field_htb_chapter_element']['und']:
        section_body = ""
        ### DEBUG
        # print "section"
        section_title = section['field_htb_translatable_title']['en'][0]['value']
        depth = section['field_htb_chapter_content_level']['und'][0]['tid']
        if depth == '81':
            heading_level = '#'
        elif depth == '82':
            heading_level = '##'
        else:
            ### BTW: 83
            heading_level = '###'

        top_text = section['field_chapter_text_zero']['en'][0]['value'] if section['field_chapter_text_zero'] else ""
        section_body += top_text + "\n"
        ### Deal with chapter_feature
        if section['field_htb_chapter_feature_top']:
            ### DEBUG
            # print "has feature"
            lang = 'en' if section['field_htb_chapter_feature_top'].has_key('en') else 'und'
            if section['field_htb_chapter_feature_top'][lang][0]['title'].split(" ")[0] == "Snippet":
                ### Snippet
                ### DEBUG
                # print "has snippet #%s" % snippet_position
                snippet_name = "snippet_%s" % str(snippet_position).zfill(2)
                snippet_filename = "%s.md" % snippet_name
                # TODO: Add front-matter to Snippet files?
                snippet_content = section['field_htb_chapter_feature_top'][lang][0]['value'] + "\n"
                write_output(snippet_path, snippet_filename, snippet_content)
                section_body += snippet_placeholder % snippet_name
                snippet_position = snippet_position + 1
            elif section['field_htb_chapter_feature_top'][lang][0].has_key('url'):
                ### Tool Guide Pointer
                ### DEBUG
                # print "has tool link"
                tool_url = section['field_htb_chapter_feature_top'][lang][0]['url'].split("/")
                tool_link = os.path.join(tool_url[6], tool_url[5])
                section_body += tool_pointer_placeholder % tool_link
            else:
                ### Still has a Snippet Placeholder in Drupal, but it hasn't been re-constructed, 
                ### probably because there is no matching snippet in the Community Guide wrapper
                snippet_name = "snippet_%s" % str(snippet_position).zfill(2)
                section_body += snippet_placeholder % snippet_name
                snippet_position = snippet_position + 1                

        middle_text = section['field_htb_chapter_text']['en'][0]['value'] if section['field_htb_chapter_text'] else ""
        section_body += middle_text + "\n"
        ### Deal with chapter_feature
        if section['field_htb_chapter_feature']:
            ### DEBUG
            # print "has feature"
            lang = 'en' if section['field_htb_chapter_feature'].has_key('en') else 'und'
            if section['field_htb_chapter_feature'][lang][0]['title'].split(" ")[0] == "Snippet":
                ### DEBUG
                # print "has snippet #%s" % snippet_position
                snippet_name = "snippet_%s" % str(snippet_position).zfill(2)
                snippet_filename = "%s.md" % snippet_name
                # TODO: Add front-matter to Snippet files?
                snippet_content = section['field_htb_chapter_feature'][lang][0]['value'] + "\n"
                write_output(snippet_path, snippet_filename, snippet_content)
                section_body += snippet_placeholder % snippet_name
                snippet_position = snippet_position + 1
            elif section['field_htb_chapter_feature'][lang][0].has_key('url'):
                ### DEBUG
                # print "has tool link"
                tool_url = section['field_htb_chapter_feature'][lang][0]['url'].split("/")
                tool_link = os.path.join(tool_url[6], tool_url[5])
                section_body += tool_pointer_placeholder % tool_link
            else:
                ### Still has a Snippet Placeholder in Drupal, but it hasn't been re-constructed, 
                ### probably because there is no matching snippet in the Community Guide wrapper
                snippet_name = "snippet_%s" % str(snippet_position).zfill(2)
                section_body += snippet_placeholder % snippet_name
                snippet_position = snippet_position + 1                

        bottom_text = section['field_htb_chapter_text_two']['en'][0]['value'] if section['field_htb_chapter_text_two'] else ""
        section_body += bottom_text + "\n"
        ### Deal with chapter_feature
        if section['field_htb_chapter_feature_bottom']:
            ### DEBUG
            # print "has feature"
            lang = 'en' if section['field_htb_chapter_feature_bottom'].has_key('en') else 'und'
            if section['field_htb_chapter_feature_bottom'][lang][0]['title'].split(" ")[0] == "Snippet":
                ### DEBUG
                # print "has snippet #%s" % snippet_position
                snippet_name = "snippet_%s" % str(snippet_position).zfill(2)
                snippet_filename = "%s.md" % snippet_name
                # TODO: Add front-matter to Snippet files?
                snippet_content = section['field_htb_chapter_feature_bottom'][lang][0]['value'] + "\n"
                write_output(snippet_path, snippet_filename, snippet_content)
                section_body += snippet_placeholder % snippet_name
                snippet_position = snippet_position + 1
            elif section['field_htb_chapter_feature_bottom'][lang][0].has_key('url'):
                ### DEBUG
                # print "has tool link"
                tool_url = section['field_htb_chapter_feature_bottom'][lang][0]['url'].split("/")
                tool_link = os.path.join(tool_url[6], tool_url[5])
                section_body += tool_pointer_placeholder % tool_link
            else:
                ### Still has a Snippet Placeholder in Drupal, but it hasn't been re-constructed, 
                ### probably because there is no matching snippet in the Community Guide wrapper
                snippet_name = "snippet_%s" % str(snippet_position).zfill(2)
                section_body += snippet_placeholder % snippet_name
                snippet_position = snippet_position + 1                

        formatted_output += """
%s %s
%s
""" % (heading_level, section_title, section_body)

    ### Format "Further reading"
    if output_data['field_guide']['und'][0]['field_htb_further_reading']:
        formatted_output += "# Further reading\n\n"
        for reference in output_data['field_guide']['und'][0]['field_htb_further_reading']['en']:
            formatted_output += "- %s\n" % reference['value']
    
    ### Write markdown-formatted guide
    output_filename = "index.md"
    output_guide_folder = "%s-%s" % ( guide_weight, slugify(guide_title) )
    output_path = os.path.join(output_directory, "md", guide_lang, guide_community, guide_type, output_guide_folder)
    write_output(output_path, output_filename, formatted_output)

### Format Markdown output for an English Tool Guide and send it to be written
def output_tool_md(front_matter, output_data):
    guide_lang, guide_community, guide_type, guide_os, guide_weight, guide_title = front_matter
    formatted_output = """

---

lang: %s
community: %s
type: %s
os: %s
weight: %s
title: %s

---

""" % ( guide_lang, guide_community, guide_type, guide_os, guide_weight, guide_title )

    ### Format intro
    formatted_output += output_data['field_guide']['und'][0]['field_hog_introduction']['en'][0]['value'] + "\n\n"

    ### Format "Required reading"
    # TODO: Links won't currently work due to mismatch between long-names and short-names for Tactics Guides
    required_reading_placeholder = "\n:[](../../../tactics/%s)\n\n"
    if output_data['field_guide']['und'][0]['field_hog_required_read']:
        formatted_output += "# Required reading\n\n"
        lang = 'en' if output_data['field_guide']['und'][0]['field_hog_required_read'].has_key('en') else 'und' 
        for required_read in output_data['field_guide']['und'][0]['field_hog_required_read'][lang]:
            read_url = required_read['url'].split("/")
            read_link = os.path.join(read_url[5])
            formatted_output += required_reading_placeholder % read_link

    ### Format tool info
    tool_guide_folder = "%s-%s" % ( guide_weight, slugify(guide_title) )
    tool_path = os.path.join(output_directory, "md", guide_lang, guide_community, guide_type, guide_os, tool_guide_folder)
    tool_placeholder =  "\n:[](%s)\n\n"
    tool_filename = "%s.md" % slugify(guide_title)
    tool_data = output_data['field_guide']['und'][0]['field_hog_tool']['und'][0]
    tool_content = ""
    tool_icon = tool_data['field_tool_logo']['en'][0]['filename']
    tool_icon_link = "https://securityinabox.org/sites/securityinabox.org/files/media/tool/logo/%s" % tool_icon
    tool_content += "![](%s)\n" % tool_icon_link
    if tool_data['field_tool_link_to_website']:
        tool_website_link = tool_data['field_tool_link_to_website']['en'][0]['url']
        tool_content += "[Project website](%s)\n" % tool_website_link
    if tool_data['field_tool_download_link']:
        for download_link in tool_data['field_tool_download_link']['en']:
            tool_content += "[%s](%s)\n" % ( download_link['title'], download_link['url'] )
    tool_version = tool_data['field_tool_version']['en'][0]['value']
    tool_content += "Version used in this guide: %s\n" % tool_version
    tool_license_term = tool_data['field_tool_license']['en'][0]['tid']
    if tool_license_term == '1':
        tool_license = "Free and Open Source Software"
    elif tool_license_term == '2':
        tool_license = "Free Proprietary Software"
    elif tool_license_term == '3':
        tool_license = "Proprietary Software"
    elif tool_license_term == '112':
        tool_license = "Free Service"
    elif tool_license_term == '113':
        tool_license = "Free Commercial Service"
    tool_content += "License: %s\n" % tool_license
    if tool_data['field_tool_system_requirements']:
        tool_system_requirements = tool_data['field_tool_system_requirements']['en'][0]['value']
        tool_content += "System requirements:\n%s\n" % tool_system_requirements

    ### Get tool content and put it in tool_content
    write_output(tool_path, tool_filename, tool_content)
    formatted_output += tool_placeholder % slugify(guide_title)

    ### Format "What you will get from this guide"
    formatted_output += "# What you will get from this guide\n\n"
    if output_data['field_guide']['und'][0]['field_hog_what_you_get']:
        for learning_goal in output_data['field_guide']['und'][0]['field_hog_what_you_get']['en']:
            formatted_output += "- %s\n" % learning_goal['value']

    for section in output_data['field_guide']['und'][0]['field_hog_element']['und']:
        section_body = ""
        ### Deals with "Node ???? could not be found" errors that occur when blank guide sections are "skipped" in Drupal
        if isinstance(section, list):
            print "Possible error: %s" % ( section[0] )
        else:            
            section_title = section['field_hog_translatable_title']['en'][0]['value']
            depth = section['field_hog_content_level']['und'][0]['tid']
            if depth == '81' or depth == '109':
                heading_level = '#'
            elif depth == '82' or depth == '110':
                heading_level = '##'
            else:
                ### BTW: 83 or 111
                heading_level = '###'

            section_body = section['field_section_intro']['en'][0]['value'] if section['field_section_intro'] else "\n\n"
            formatted_output += """
%s %s

%s
""" % ( heading_level, section_title, section_body )

    ### Format FAQ
    if output_data['field_guide']['und'][0]['field_hog_faq']:
        formatted_output += "\n# FAQ\n\n"
        formatted_output += output_data['field_guide']['und'][0]['field_hog_faq']['en'][0]['value']

    output_filename = "index.md"
    output_guide_folder = "%s-%s" % ( guide_weight, slugify(guide_title) )
    output_path = os.path.join(output_directory, "md", guide_lang, guide_community, guide_type, guide_os, output_guide_folder)
    write_output(output_path, output_filename, formatted_output)

### Format Markdown output for a Legacy Tactics Guide and send it to be written
def output_legacy_tactic_md(front_matter, output_data):
    guide_lang, guide_community, guide_type, guide_weight, guide_title = front_matter
    formatted_output = """

---

lang: %s
community: %s
type: %s
legacy: True
child: False
weight: %s
title: %s

---

%s

""" % ( guide_lang, guide_community, guide_type, guide_weight, guide_title, output_data['body'][guide_lang][0]['value'] )

    output_guide_folder = "%s-%s" % ( guide_weight, slugify(guide_title) )
    output_filename = "index.md" 
    output_path = os.path.join(output_directory, "md", guide_lang, guide_community, guide_type, output_guide_folder)
    write_output(output_path, output_filename, formatted_output)

    ### Output book_children
    # TODO: May need to be recursive for three-level books (such as Social Media)
    #       but we'll first need to enhance the all-legacy-nodes-feed Drupal view 

    for book_child in output_data['book_children']:
        if book_child:
            book_child_title = book_child['title_original']
            book_child_weight = book_child['book']['weight']
            book_child_depth = book_child['book']['depth']
            book_child_has_children = book_child['book']['has_children']
            if book_child_has_children == "1":
                print "Book child has children. They will be ignored. Fix first in Drupal 'all-legacy-nodes-feed' view"
            # TODO: make sure grandchildren sort correctly
            book_child_sorting_trick = book_child_weight.zfill(2) + "0" if book_child_depth == "3" else "999"

            ### Update formatted_child_output
            formatted_child_output = """

---

lang: %s
community: %s
type: %s
legacy: True
child: True
weight: %s
depth: %s
title: %s

---

%s

""" % ( guide_lang, guide_community, guide_type, book_child_weight, book_child_depth, book_child_title, book_child['body'][guide_lang][0]['value'] )

            child_output_filename = "%s-%s.md" % ( book_child_sorting_trick, slugify(book_child_title) )
            child_output_path = os.path.join(output_directory, "md", guide_lang, guide_community, guide_type, output_guide_folder)
            write_output(child_output_path, child_output_filename, formatted_child_output)


### Format Markdown output for a Legacy Tool Guide and send it to be written
def output_legacy_tool_md(front_matter, output_data):
    guide_lang, guide_community, guide_type, guide_os, guide_weight, guide_title = front_matter
    formatted_output = """

---

lang: %s
community: %s
type: %s
legacy: True
child: False
os: %s
weight: %s
title: %s

---

%s

""" % ( guide_lang, guide_community, guide_type, guide_os, guide_weight, guide_title, output_data['body'][guide_lang][0]['value'] )

    output_guide_folder = "%s-%s" % ( guide_weight, slugify(guide_title) )
    output_filename = "index.md" 
    output_path = os.path.join(output_directory, "md", guide_lang, guide_community, guide_type, guide_os, output_guide_folder)
    write_output(output_path, output_filename, formatted_output)

    ### Output book_children
    # TODO: May need to be recursive for three-level books (such as Social Media)
    #       but we'll first need to enhance the all-legacy-nodes-feed Drupal view 

    for book_child in output_data['book_children']:
        if book_child:
            book_child_title = book_child['title_original']
            book_child_weight = book_child['book']['weight']
            book_child_depth = book_child['book']['depth']
            book_child_has_children = book_child['book']['has_children']
            if book_child_has_children == "1":
                print "Book child has children. They will be ignored. Fix first in Drupal 'all-legacy-nodes-feed' view"
            # TODO: make sure grandchildren sort correctly
            book_child_sorting_trick = book_child_weight.zfill(2) + "0" if book_child_depth == "3" else "999"

            ### Update formatted_child_output
            formatted_child_output = """

---

lang: %s
community: %s
type: %s
legacy: True
child: True
os: %s
weight: %s
depth: %s
title: %s

---

%s

""" % ( guide_lang, guide_community, guide_type, guide_os, book_child_weight, book_child_depth, book_child_title, book_child['body'][guide_lang][0]['value'] )

            child_output_filename = "%s-%s.md" % ( book_child_sorting_trick, slugify(book_child_title) )
            child_output_path = os.path.join(output_directory, "md", guide_lang, guide_community, guide_type, guide_os, output_guide_folder)
            write_output(child_output_path, child_output_filename, formatted_child_output)


### Write content to a file
def write_output(output_path, output_filename, contents):
    ### Create directories if necessary
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
    output_filepath = os.path.join(output_path, output_filename)
    output_file = codecs.open(output_filepath, mode='w', encoding='utf-8')
    output_file.write(contents)
    output_file.close()

### Pretty print json for debugging
def pp(json_data):
    print json.dumps(json_data, indent=4, sort_keys=True)

###
### Do the thing
### 

if input_nid == "all":
    fetch_all_guides()
    # fetch_all_legacy_guides()

else:
    validate_nid(input_nid)

###
### TODO
### 
#
# - Deal with Snippets more gracefully
#   - Fetch Community-specific Snippets
# 
# - Improve Markdown output
#   - All files should use short titles rather than long ones
#     - bug: administrative title value may only be displayed through .../xx/api/node/####.json, 
#       but only .../en/api/node/####.json is accessible without authentication
#   - Deal gracefully with html tags in legacy content (e.g. <div class="background"> around snippets)
#   - Deal gracefully with html content (e.g. chapter-1 in ar, es & fr)
# 
# - Improve fetch_legacy_guide(nid)
#   - Deal with three-level books such as the Social Networking Tactics Guide (w/out including top-level HtB, HoG and Mobile book roots
# 
# - Data structure
#   - Media
#   - Community linkages
#     - TODO: Record snippets (only) from guides for which underlying content has already been fetched
#     - TODO: Create relation tables between those snippets and the "placeholders" in the corresponding core guide?
#   - Transformable links that
#     - Work locally
#     - Are community-aware
# 
# - Fetch media
# 
# - Clean up code
#   - Write a function that uses a dict to output both keys and values of YAML front-matter
#   - fetch_xml() for reading RSS Drupal Views?
#   - Clean up output_tool_md() and output_tactic_md()
#   - Use iterator to prune language-versions from legacy nodes?
# 
###
