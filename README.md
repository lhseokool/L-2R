# L-2R
## Dataset
### LoTTE
You can download the LoTTE dataset from this link: [LoTTE Dataset](https://downloads.cs.stanford.edu/nlp/data/colbert/colbertv2/lotte.tar.gz)

### LL-LoTTE
Additional LL-LoTTE data can be accessed from the following link: [LL-LoTTE](https://drive.google.com/drive/folders/1Gbka5Fb2jHsKPeHwJw8lF52-H34pqogi?usp=drive_link)

### Project Directory Structure
The project and dataset directories are organized as follows:
```
|-- data
	|-- lotte
		|-- writing
			|-- dev
				|-- collection.tsv
				|-- metadata.jsonl
				|-- questions.search.tsv
				|-- qas.search.jsonl
				|-- questions.forum.tsv
				|-- qas.forum.jsonl
			|-- test
				|-- collection.tsv
				|-- ...
		|-- recreation
			|-- ...
		|-- ...

|-- data_incre_aug
	|-- session_{1,2,3,4}
	|-- train_dir
	|-- run_bm25.sh
	|-- run_bm25_test.sh
	|-- train_query.tsv
```