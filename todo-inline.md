---
header-includes: "<style>\nbody {\n  max-width: 50em;\n}\n</style>"
source: https://github.com/knc-neural-calculus/knc-tools
title: todo-inline
updated: '2022-09-08 12:45:35'

metadata:
  files_with_todos: 1
  num_items: 31
  num_unique_tags: 14
  searched_files: 4

# suggested command for conversion to html
cmd: "pandoc todo-inline.md -o todo-inline.html --from markdown+backtick_code_blocks+fenced_code_attributes --standalone --toc --toc-depth 1"
---
# [`./inline_todo/inline_todo.py`](./inline_todo/inline_todo.py) -- 31 items
## **!!!** -- 1 item
 - [ ] !!!", 
	(line 85)
	
	<details>
	```{.python .numberLines startFrom="85"}
	        "!!!",
	        "OLD"
	    ],
	},
	# 'comments' : {
	```
	</details>

## **BUG** -- 2 items
 - [ ] BUG", 
	(line 76)
	
	<details>
	```{.python .numberLines startFrom="76"}
	"BUG",
	"DEBUG",
	"UGLY",
	"HACK",
	"NOTE",
	```
	</details>

 - [ ] BUG", 
	(line 77)
	
	<details>
	```{.python .numberLines startFrom="77"}
	"DEBUG",
	"UGLY",
	"HACK",
	"NOTE",
	"IDEA",
	```
	</details>

## **CONFIG** -- 4 items
 - [ ] CONFIG_DEFAULT` 
	(line 414)
	
	<details>
	```{.python .numberLines startFrom="414"}
	 - `CONFIG_DEFAULT`
	 - file specified by `CONFIG_DEFAULT['config']['file_in']`
	 - command line args
	 - file specified by command line arg `--config.file_in`
	
	```
	</details>

 - [ ] CONFIG_DEFAULT` 
	(line 420)
	
	<details>
	```{.python .numberLines startFrom="420"}
	- `CONFIG_DEFAULT`
	- file specified by `CONFIG_DEFAULT['config']['file_in']`
	- file specified by command line arg `--config.file_in`
	- command line args
	```
	</details>

 - [ ] CONFIG_DEFAULT : DictConfig = OmegaConf.create({ 
	(line 54)
	
	<details>
	```{.python .numberLines startFrom="54"}
	CONFIG_DEFAULT : DictConfig = OmegaConf.create({
	    'config' : {
	        'file_in' : 'itodo.yml',
	        'file_out' : None,
	    },
	```
	</details>

 - [ ] CONFIG", 
	(line 84)
	
	<details>
	```{.python .numberLines startFrom="84"}
	        "CONFIG",
	        "!!!",
	        "OLD"
	    ],
	},
	```
	</details>

## **CRIT** -- 2 items
 - [ ] CRIT: there is some sort of bug with loading configs that I can't pin down 
	(line 1151)
	
	<details>
	```{.python .numberLines startFrom="1151"}
	# CRIT: there is some sort of bug with loading configs that I can't pin down
	data : str = write_items_ms_template(
	    td_items = todo_items,
	    item_format = cfg['write']['item_format'],
	    attr_sort_order = cfg['write']['attr_sort_order'],
	```
	</details>

 - [ ] CRIT", 
	(line 72)
	
	<details>
	```{.python .numberLines startFrom="72"}
	"CRIT",
	"TODO",
	"FIXME",
	"FIX",
	"BUG",
	```
	</details>

## **FIX** -- 2 items
 - [ ] FIX' : '@', 
	(line 101)
	
	<details>
	```{.python .numberLines startFrom="101"}
	#     'PREFIX' : '@',
	#     'require' : False,
	#     'always_accept' : False,
	# },
	'SOURCE_FILES' : [
	```
	</details>

 - [ ] FIX", 
	(line 75)
	
	<details>
	```{.python .numberLines startFrom="75"}
	"FIX",
	"BUG",
	"DEBUG",
	"UGLY",
	"HACK",
	```
	</details>

## **FIXME** -- 1 item
 - [ ] FIXME", 
	(line 74)
	
	<details>
	```{.python .numberLines startFrom="74"}
	"FIXME",
	"FIX",
	"BUG",
	"DEBUG",
	"UGLY",
	```
	</details>

## **HACK** -- 3 items
 - [ ] HACK: patches the chevron renderer to not replace html strings 
	(line 1038)
	
	<details>
	```{.python .numberLines startFrom="1038"}
	# HACK: patches the chevron renderer to not replace html strings
	chevron.renderer._html_escape = lambda string: string
	rendered : str = chevron.render(
	    ms_template,
	```
	</details>

 - [ ] HACK", 
	(line 274)
	
	<details>
	```{.python .numberLines startFrom="274"}
	"h1": "HACK",
	"ul1": [
	    {
	        "h2": "foo.cpp",
	        "ul2": [
	```
	</details>

 - [ ] HACK", 
	(line 79)
	
	<details>
	```{.python .numberLines startFrom="79"}
	"HACK",
	"NOTE",
	"IDEA",
	"REVIEW",
	"OPTIMIZE",
	```
	</details>

## **IDEA** -- 1 item
 - [ ] IDEA", 
	(line 81)
	
	<details>
	```{.python .numberLines startFrom="81"}
	"IDEA",
	"REVIEW",
	"OPTIMIZE",
	"CONFIG",
	"!!!",
	```
	</details>

## **NOTE** -- 2 items
 - [ ] NOTE: moustance wants double curly braces 
	(line 226)
	
	<details>
	```{.python .numberLines startFrom="226"}
	# NOTE: moustance wants double curly braces
	return (
	    '\n'
	    .join(output)
	    .replace('{', '{{')
	```
	</details>

 - [ ] NOTE", 
	(line 80)
	
	<details>
	```{.python .numberLines startFrom="80"}
	"NOTE",
	"IDEA",
	"REVIEW",
	"OPTIMIZE",
	"CONFIG",
	```
	</details>

## **OLD** -- 1 item
 - [ ] OLD" 
	(line 86)
	
	<details>
	```{.python .numberLines startFrom="86"}
	        "OLD"
	    ],
	},
	# 'comments' : {
	#     'require' : False,
	```
	</details>

## **OPTIMIZE** -- 1 item
 - [ ] OPTIMIZE", 
	(line 83)
	
	<details>
	```{.python .numberLines startFrom="83"}
	    "OPTIMIZE",
	    "CONFIG",
	    "!!!",
	    "OLD"
	],
	```
	</details>

## **REVIEW** -- 4 items
 - [ ] REVIEW: this function should eventually be replaced by `write_items_ms_template()`, 
	(line 1069)
	
	<details>
	```{.python .numberLines startFrom="1069"}
	REVIEW: this function should eventually be replaced by `write_items_ms_template()`,
	but can be preserved as a fallback for when `chevron` is not installed
	prints in markdown format, with h1 headings for tags and h2 headings for files. 
	then, print ordered by line number
	```
	</details>

 - [ ] REVIEW: so now, after spending several hours, I look in a separate cloned version of this project and find a commit that adds this function (to `itodo.py`, which im deleting in this commit), and remember that I wanted to store both configs and the written data in the same markdown file. this might not be the best idea, but maybe its worth looking into later. For now, the plan was to write metadata (count of items, files, lines, etc) in the yaml front matter. maybe store the config in there too though (but this would make it tough to write the yaml to an html file). either way, this function is still useful. 
	(line 328)
	
	<details>
	```{.python .numberLines startFrom="328"}
	REVIEW: so now, after spending several hours, I look in a separate cloned version of this project and find a commit that adds this function (to `itodo.py`, which im deleting in this commit), and remember that I wanted to store both configs and the written data in the same markdown file. this might not be the best idea, but maybe its worth looking into later. For now, the plan was to write metadata (count of items, files, lines, etc) in the yaml front matter. maybe store the config in there too though (but this would make it tough to write the yaml to an html file). either way, this function is still useful.
	### Parameters:
	 - `filename : str`   
	   markdown file
	```
	</details>

 - [ ] REVIEW: `split_by_attribute()` does this and more, code should be removed at some point 
	(line 793)
	
	<details>
	```{.python .numberLines startFrom="793"}
	REVIEW: `split_by_attribute()` does this and more, code should be removed at some point 
	"""
	items_byTag : Dict[str, List[TodoItem]] = dict()
	```
	</details>

 - [ ] REVIEW", 
	(line 82)
	
	<details>
	```{.python .numberLines startFrom="82"}
	"REVIEW",
	"OPTIMIZE",
	"CONFIG",
	"!!!",
	"OLD"
	```
	</details>

## **TODO** -- 6 items
 - [ ] TODO: replace any chars that need to be escaped that arent inside code blocks 
	(line 1036)
	
	<details>
	```{.python .numberLines startFrom="1036"}
	# TODO: replace any chars that need to be escaped that arent inside code blocks
	# HACK: patches the chevron renderer to not replace html strings
	chevron.renderer._html_escape = lambda string: string
	```
	</details>

 - [ ] TODO: print to console if no output file specified 
	(line 1167)
	
	<details>
	```{.python .numberLines startFrom="1167"}
	# TODO: print to console if no output file specified
	with open(cfg['file_todo'], 'w', encoding = 'utf-8') as fout:
	    print('---', file = fout)
	    print(yaml.dump(HEADER_YAML), file = fout)
	    print(yaml.dump(metadata_dict), file = fout)
	```
	</details>

 - [ ] TODO", 
	(line 255)
	
	<details>
	```{.python .numberLines startFrom="255"}
	"h1": "TODO",
	"ul1": [
	    {
	        "h2": "foo.cpp",
	        "ul2": [
	```
	</details>

 - [ ] TODO: do this using globs 
	(line 648)
	
	<details>
	```{.python .numberLines startFrom="648"}
	# TODO: do this using globs
	for ex in exclude:
	    sw : str = os.path.join(searchdir, ex)
	    files_search = [
	        unixPath(x)
	```
	</details>

 - [ ] TODO", 
	(line 73)
	
	<details>
	```{.python .numberLines startFrom="73"}
	"TODO",
	"FIXME",
	"FIX",
	"BUG",
	"DEBUG",
	```
	</details>

 - [ ] TODO: use defaultdict here 
	(line 848)
	
	<details>
	```{.python .numberLines startFrom="848"}
	# TODO: use defaultdict here
	items_byAttr : Dict[str, List[TodoItem]] = dict()
	
	# actually filter everything by the attribute value
	for itm in td_items:
	```
	</details>

## **UGLY** -- 1 item
 - [ ] UGLY", 
	(line 78)
	
	<details>
	```{.python .numberLines startFrom="78"}
	"UGLY",
	"HACK",
	"NOTE",
	"IDEA",
	"REVIEW",
	```
	</details>


