# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_ddl_parser', 'simple_ddl_parser.dialects', 'simple_ddl_parser.output']

package_data = \
{'': ['*']}

install_requires = \
['ply>=3.11,<4.0']

entry_points = \
{'console_scripts': ['sdp = simple_ddl_parser.cli:main']}

setup_kwargs = {
    'name': 'simple-ddl-parser',
    'version': '0.21.1',
    'description': 'Simple DDL Parser to parse SQL & dialects like HQL, TSQL (MSSQL), Oracle, AWS Redshift, Snowflake, MySQL, PostgreSQL, etc ddl files to json/python dict with full information about columns: types, defaults, primary keys, etc.; sequences, alters, custom types & other entities from ddl.',
    'long_description': '\nSimple DDL Parser\n-----------------\n\n\n.. image:: https://img.shields.io/pypi/v/simple-ddl-parser\n   :target: https://img.shields.io/pypi/v/simple-ddl-parser\n   :alt: badge1\n \n.. image:: https://img.shields.io/pypi/l/simple-ddl-parser\n   :target: https://img.shields.io/pypi/l/simple-ddl-parser\n   :alt: badge2\n \n.. image:: https://img.shields.io/pypi/pyversions/simple-ddl-parser\n   :target: https://img.shields.io/pypi/pyversions/simple-ddl-parser\n   :alt: badge3\n \n.. image:: https://github.com/xnuinside/simple-ddl-parser/actions/workflows/main.yml/badge.svg\n   :target: https://github.com/xnuinside/simple-ddl-parser/actions/workflows/main.yml/badge.svg\n   :alt: workflow\n\n\nBuild with ply (lex & yacc in python). A lot of samples in \'tests/.\n\nIs it Stable?\n^^^^^^^^^^^^^\n\nYes, library already has about 7000+ downloads per day - https://pypistats.org/packages/simple-ddl-parser.\n\nAs maintainer, I guarantee that any backward incompatible changes will not be done in patch or minor version. Only additionals & new features.\n\nHowever, in process of adding support for new statements & features I see that output can be structured more optimal way and I hope to release version ``1.0.*`` with more struct output result. But, it will not be soon, first of all, I want to add support for so much statements as I can. So I don\'t think make sense to expect version 1.0.* before, for example, version ``0.26.0`` :)\n\nHow does it work?\n^^^^^^^^^^^^^^^^^\n\nParser tested on different DDLs mostly for PostgreSQL & Hive. But idea to support as much as possible DDL dialects (AWS \nRedshift, Oracle, Hive, MsSQL, etc.). You can check dialects sections after ``Supported Statements`` section to get more information that statements from dialects already supported by parser.\n\nFeel free to open Issue with DDL sample\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n**If you need some statement, that not supported by parser yet**\\ : please provide DDL example & information about that is it SQL dialect or DB.\n\nTypes that are used in your DB does not matter, so parser must also work successfuly to any DDL for SQL DB. Parser is NOT case sensitive, it did not expect that all queries will be in upper case or lower case. So you can write statements like this:\n\n.. code-block:: sql\n\n\n       Alter Table Persons ADD CONSTRAINT CHK_PersonAge CHECK (Age>=18 AND City=\'Sandnes\');\n\nIt will be parsed as is without errors.\n\nIf you have samples that cause an error - please open the issue (but don\'t forget to add ddl example), I will be glad to fix it.\n\nA lot of statements and output result you can find in tests on the github - https://github.com/xnuinside/simple-ddl-parser/tree/main/tests .\n\nHow to install\n^^^^^^^^^^^^^^\n\n.. code-block:: bash\n\n\n       pip install simple-ddl-parser\n\nHow to use\n----------\n\nExtract additional information from HQL (& other dialects)\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\nIn some dialects like HQL there is a lot of additional information about table like, fore example, is it external table, STORED AS, location & etc. This propertie will be always empty in \'classic\' SQL DB like PostgreSQL or MySQL and this is the reason, why by default this information are \'hidden\'.\nAlso some fields hidden in HQL, because they are simple not exists in HIVE, for example \'deferrable_initially\'\nTo get this \'hql\' specific details about table in output please use \'output_mode\' argument in run() method.\n\nexample:\n\n.. code-block:: python\n\n\n       ddl = """\n       CREATE TABLE IF NOT EXISTS default.salesorderdetail(\n           SalesOrderID int,\n           ProductID int,\n           OrderQty int,\n           LineTotal decimal\n           )\n       PARTITIONED BY (batch_id int, batch_id2 string, batch_32 some_type)\n       LOCATION \'s3://datalake/table_name/v1\'\n       ROW FORMAT DELIMITED\n           FIELDS TERMINATED BY \',\'\n           COLLECTION ITEMS TERMINATED BY \'\\002\'\n           MAP KEYS TERMINATED BY \'\\003\'\n       STORED AS TEXTFILE\n       """\n\n       result = DDLParser(ddl).run(output_mode="hql")\n       print(result)\n\nAnd you will get output with additional keys \'stored_as\', \'location\', \'external\', etc.\n\n.. code-block:: python\n\n\n       # additional keys examples\n     {\n       ...,\n       \'location\': "\'s3://datalake/table_name/v1\'",\n       \'map_keys_terminated_by\': "\'\\\\003\'",\n       \'partitioned_by\': [{\'name\': \'batch_id\', \'size\': None, \'type\': \'int\'},\n                           {\'name\': \'batch_id2\', \'size\': None, \'type\': \'string\'},\n                           {\'name\': \'batch_32\', \'size\': None, \'type\': \'some_type\'}],\n       \'primary_key\': [],\n       \'row_format\': \'DELIMITED\',\n       \'schema\': \'default\',\n       \'stored_as\': \'TEXTFILE\',\n       ... \n     }\n\nIf you run parser with command line add flag \'-o=hql\' or \'--output-mode=hql\' to get the same result.\n\nPossible output_modes: ["mssql", "mysql", "oracle", "hql", "sql", "redshift", "snowflake"]\n\nFrom python code\n^^^^^^^^^^^^^^^^\n\n.. code-block:: python\n\n       from simple_ddl_parser import DDLParser\n\n\n       parse_results = DDLParser("""create table dev.data_sync_history(\n           data_sync_id bigint not null,\n           sync_count bigint not null,\n           sync_mark timestamp  not  null,\n           sync_start timestamp  not null,\n           sync_end timestamp  not null,\n           message varchar(2000) null,\n           primary key (data_sync_id, sync_start)\n       ); """).run()\n\n       print(parse_results)\n\nTo parse from file\n^^^^^^^^^^^^^^^^^^\n\n.. code-block:: python\n\n\n       from simple_ddl_parser import parse_from_file\n\n       result = parse_from_file(\'tests/sql/test_one_statement.sql\')\n       print(result)\n\nFrom command line\n^^^^^^^^^^^^^^^^^\n\nsimple-ddl-parser is installed to environment as command **sdp**\n\n.. code-block:: bash\n\n\n       sdp path_to_ddl_file\n\n       # for example:\n\n       sdp tests/sql/test_two_tables.sql\n\nYou will see the output in **schemas** folder in file with name **test_two_tables_schema.json**\n\nIf you want to have also output in console - use **-v** flag for verbose.\n\n.. code-block:: bash\n\n\n       sdp tests/sql/test_two_tables.sql -v\n\nIf you don\'t want to dump schema in file and just print result to the console, use **--no-dump** flag:\n\n.. code-block:: bash\n\n\n       sdp tests/sql/test_two_tables.sql --no-dump\n\nYou can provide target path where you want to dump result with argument **-t**\\ , **--targer**\\ :\n\n.. code-block:: bash\n\n\n       sdp tests/sql/test_two_tables.sql -t dump_results/\n\nMore details\n^^^^^^^^^^^^\n\n``DDLParser(ddl).run()``\n.run() method contains several arguments, that impact changing output result. As you can saw upper exists argument ``output_mode`` that allow you to set dialect and get more fields in output relative to chosen dialect, for example \'hql\'. Possible output_modes: ["mssql", "mysql", "oracle", "hql", "sql"]\n\nAlso in .run() method exists argument ``group_by_type`` (by default: False). By default output of parser looks like a List with Dicts where each dict == one entitiy from ddl (table, sequence, type, etc). And to understand that is current entity you need to check Dict like: if \'table_name\' in dict - this is a table, if \'type_name\' - this is a type & etc.\n\nTo make work little bit easy you can set group_by_type=True and you will get output already sorted by types, like:\n\n.. code-block:: python\n\n\n       { \n           \'tables\': [all_pasrsed_tables], \n           \'sequences\': [all_pasrsed_sequences], \n           \'types\': [all_pasrsed_types], \n           \'domains\': [all_pasrsed_domains],\n           ...\n       }\n\nFor example:\n\n.. code-block:: python\n\n\n       ddl = """\n       CREATE TYPE "schema--notification"."ContentType" AS\n           ENUM (\'TEXT\',\'MARKDOWN\',\'HTML\');\n           CREATE TABLE "schema--notification"."notification" (\n               content_type "schema--notification"."ContentType"\n           );\n       CREATE SEQUENCE dev.incremental_ids\n           INCREMENT 10\n           START 0\n           MINVALUE 0\n           MAXVALUE 9223372036854775807\n           CACHE 1;\n       """\n\n       result = DDLParser(ddl).run(group_by_type=True)\n\n       # result will be:\n\n       {\'sequences\': [{\'cache\': 1,\n                       \'increment\': 10,\n                       \'maxvalue\': 9223372036854775807,\n                       \'minvalue\': 0,\n                       \'schema\': \'dev\',\n                       \'sequence_name\': \'incremental_ids\',\n                       \'start\': 0}],\n       \'tables\': [{\'alter\': {},\n                   \'checks\': [],\n                   \'columns\': [{\'check\': None,\n                               \'default\': None,\n                               \'name\': \'content_type\',\n                               \'nullable\': True,\n                               \'references\': None,\n                               \'size\': None,\n                               \'type\': \'"schema--notification"."ContentType"\',\n                               \'unique\': False}],\n                   \'index\': [],\n                   \'partitioned_by\': [],\n                   \'primary_key\': [],\n                   \'schema\': \'"schema--notification"\',\n                   \'table_name\': \'"notification"\'}],\n       \'types\': [{\'base_type\': \'ENUM\',\n                   \'properties\': {\'values\': ["\'TEXT\'", "\'MARKDOWN\'", "\'HTML\'"]},\n                   \'schema\': \'"schema--notification"\',\n                   \'type_name\': \'"ContentType"\'}]}\n\nALTER statements\n^^^^^^^^^^^^^^^^\n\nRight now added support only for ALTER statements with FOREIGEIN key\n\nFor example, if in your ddl after table defenitions (create table statements) you have ALTER table statements like this:\n\n.. code-block:: sql\n\n\n   ALTER TABLE "material_attachments" ADD FOREIGN KEY ("material_id", "material_title") REFERENCES "materials" ("id", "title");\n\nThis statements will be parsed and information about them putted inside \'alter\' key in table\'s dict.\nFor example, please check alter statement tests - **tests/test_alter_statements.py**\n\nMore examples & tests\n^^^^^^^^^^^^^^^^^^^^^\n\nYou can find in **tests/** folder.\n\nDump result in json\n^^^^^^^^^^^^^^^^^^^\n\nTo dump result in json use argument .run(dump=True)\n\nYou also can provide a path where you want to have a dumps with schema with argument .run(dump_path=\'folder_that_use_for_dumps/\')\n\nSupported Statements\n--------------------\n\n\n* \n  CREATE TABLE [ IF NOT EXISTS ] + columns defenition, columns attributes: column name + type + type size(for example, varchar(255)), UNIQUE, PRIMARY KEY, DEFAULT, CHECK, NULL/NOT NULL, REFERENCES, ON DELETE, ON UPDATE,  NOT DEFERRABLE, DEFERRABLE INITIALLY, GENERATED ALWAYS, STORED, COLLATE\n\n* \n  STATEMENTS: PRIMARY KEY, CHECK, FOREIGN KEY in table defenitions (in create table();)\n\n* \n  ALTER TABLE STATEMENTS: ADD CHECK (with CONSTRAINT), ADD FOREIGN KEY (with CONSTRAINT), ADD UNIQUE, ADD DEFAULT FOR\n\n* \n  PARTITION BY statement\n\n* \n  CREATE SEQUENCE with words: INCREMENT [BY], START [WITH], MINVALUE, MAXVALUE, CACHE\n\n* \n  CREATE TYPE statement:  AS TABLE, AS ENUM, AS OBJECT, INTERNALLENGTH, INPUT, OUTPUT\n\n* \n  LIKE statement (in this and only in this case to output will be added \'like\' keyword with information about table from that we did like - \'like\': {\'schema\': None, \'table_name\': \'Old_Users\'}).\n\n* \n  TABLESPACE statement\n\n* \n  COMMENT ON statement\n\n* \n  CREATE SCHEMA [IF NOT EXISTS] ... [AUTHORIZATION] ...\n\n* \n  CREATE DOMAIN [AS]\n\n* \n  CREATE [SMALLFILE | BIGFILE] [TEMPORARY] TABLESPACE statement\n\n* \n  CREATE DATABASE + Properties parsing\n\nHQL Dialect statements\n^^^^^^^^^^^^^^^^^^^^^^\n\n\n* PARTITIONED BY statement\n* ROW FORMAT, ROW FORMAT SERDE\n* WITH SERDEPROPERTIES ("input.regex" =  "..some regex..")\n* STORED AS (AVRO, PARQUET, etc), STORED AS INPUTFORMAT, OUTPUTFORMAT\n* COMMENT\n* LOCATION\n* FIELDS TERMINATED BY, LINES TERMINATED BY, COLLECTION ITEMS TERMINATED BY, MAP KEYS TERMINATED BY\n* TBLPROPERTIES (\'parquet.compression\'=\'SNAPPY\' & etc.)\n* SKEWED BY\n\nMySQL\n^^^^^\n\n\n* ON UPDATE in column without reference \n\nMSSQL\n~~~~~\n\n\n* CONSTRAINT [CLUSTERED]... PRIMARY KEY\n* CONSTRAINT ... WITH statement\n* PERIOD FOR SYSTEM_TIME in CREATE TABLE statement\n* ON [PRIMARY] after CREATE TABLE statement (sample in test files test_mssql_specific.py)\n* WITH statement for TABLE properties\n* TEXTIMAGE_ON statement\n* DEFAULT NEXT VALUE FOR in COLUMN DEFAULT\n\nMSSQL / MySQL/ Oracle\n^^^^^^^^^^^^^^^^^^^^^\n\n\n* type IDENTITY statement\n* FOREIGN KEY REFERENCES statement\n* \'max\' specifier in column size\n* CONSTRAINT ... UNIQUE, CONSTRAINT ... CHECK, CONSTRAINT ... FOREIGN KEY, CONSTRAINT ... PRIMARY KEY\n* CREATE CLUSTERED INDEX\n\nOracle\n^^^^^^\n\n\n* ENCRYPT column property [+ NO SALT, SALT, USING]\n* STORAGE column property\n\nAWS Redshift Dialect statements\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n\n* ENCODE column property\n* SORTKEY, DISTSTYLE, DISTKEY, ENCODE table properties\n* \n  CREATE TEMP / TEMPORARY TABLE\n\n* \n  syntax like with LIKE statement:\n\n  ``create temp table tempevent(like event);``\n\nSnowflake Dialect statements\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n\n* CREATE .. CLONE statements for table, database and schema\n* CREATE TABLE .. CLUSTER BY ..\n* CONSTRAINT .. [NOT] ENFORCED \n\nTODO in next Releases (if you don\'t see feature that you need - open the issue)\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n\n\n\n#. Add support for ALTER TABLE ... ADD COLUMN\n#. Add more support for CREATE type IS TABLE (example: CREATE OR REPLACE TYPE budget_tbl_typ IS TABLE OF NUMBER(8,2);\n#. Add support (ignore correctly) ALTER TABLE ... DROP CONSTRAINT ..., ALTER TABLE ... DROP INDEX ...\n\nnon-feature todo\n----------------\n\n\n#. Provide API to get result as Python Object\n#. Add online demo (UI) to parse ddl\n\nThanks for involving & contributions\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\nBig thanks for the involving & contribution with test cases with DDL samples & opening issues goes to:\n\n\n* https://github.com/kukigai , \n* https://github.com/Awalkman90 ,\n* https://github.com/geob3d\n\nChangelog\n---------\n\n**v0.21.1**\nFixies:\n\n\n#. START WITH, INCREMENT BY and CACHE (without value) in sequences now is parsed correctly.\n\n**v0.21.0**\n\nNew Features:\n^^^^^^^^^^^^^\n\n.. code-block::\n\n   ## MSSQL:\n\n   1. Added support for statements: \n       1. PERIOD FOR SYSTEM_TIME in CREATE TABLE statement\n       2. ON [PRIMARY] after CREATE TABLE statement (sample in test files test_mssql_specific.py)\n       3. WITH statement for TABLE properties\n       4. TEXTIMAGE_ON statement\n       5. DEFAULT NEXT VALUE FOR in COLUMN DEFAULT\n\n   2. Added support for separating tables DDL by \'GO\' statement as in output of MSSQL\n   3. Added support for CREATE TYPE as TABLE\n\n\n**v0.20.0**\n\nNew Features:\n^^^^^^^^^^^^^\n\n.. code-block::\n\n   #### Common\n   1. SET statements from DDL scripts now collected as type \'ddl_properties\' (if you use group_by_type=True) and parsed as\n   dicts with 2 keys inside {\'name\': \'property name\', \'value\': \'property value\'}\n\n   #### MySQL\n   2. Added support for MySQL ON UPDATE statements in column (without REFERENCE)\n\n   #### MSSQL\n   3. Added support for CONSTRAINT [CLUSTERED]... PRIMARY KEY for Table definition\n   4. Added support for WITH statement in CONSTRAINT (Table definition)\n\n\n\n**v0.19.9**\n\n\n#. Fixed issue with the weird log - https://github.com/xnuinside/simple-ddl-parser/issues/78.\n\n**v0.19.8**\nFeatures:\n\n.. code-block::\n\n   1. Method `DDLParser(...).run(...)` now get argument json=True if you want to get result as json,\n   but not as Python Object\n\n\nFixes:\n\n.. code-block::\n\n   1. Fixed issue when variables are \'glue\' during Struct parse like previously STRUCT<a ARRAY<STRING>,b BOOL> was\n   extracted like \'STRUCT <aARRAY <STRING>,bBOOL>\', now this issue was fixed and it parsed as is STRUCT < a\n   ARRAY < STRING > ,b BOOL >. Now \'>\' and \'<\' always will be with space near them.\n\n   2. CHECK CONSTRAINT with functions. Fix for https://github.com/xnuinside/simple-ddl-parser/issues/76.\n\n\n\n**v0.19.7**\nFixes:\n\n\n#. Add support for more special symbols to strings - https://github.com/xnuinside/simple-ddl-parser/issues/68\n\nFeatures:\n\n\n#. Added support for HQL statements:\n    STORED AS INPUTFORMAT, OUTPUTFORMAT - https://github.com/xnuinside/simple-ddl-parser/issues/69\n    SKEWED BY\n\n**v0.19.6**\nFixes:\n\n\n#. Fixed issue with PARTITIONED BY multiple columns in HQL - https://github.com/xnuinside/simple-ddl-parser/issues/66\n#. Question symbol \'?\' now handled valid in strings - https://github.com/xnuinside/simple-ddl-parser/issues/64\n#. Fixed issue with escaping symbols & added tests -https://github.com/xnuinside/simple-ddl-parser/issues/63\n\nFeatures:\n\n\n#. Added support for HQL statement TBLPROPERTIES - https://github.com/xnuinside/simple-ddl-parser/issues/65\n\n**v0.19.5**\nFixes:\n\n\n#. Fixed issues with COMMENT statement in column definitions. Add bunch of tests, now they expect working ok.\n\n**v0.19.4**\n\n\n#. Added support for PARTITION BY (previously was only PARTITIONED BY from HQL)\n\n**v0.19.2**\n\n\n#. Added support for ` quotes in column & tables names\n\n**v0.19.1**\nFixes:\n\n\n#. Issue with \'\\t\' reported in https://github.com/xnuinside/simple-ddl-parser/issues/53\n\nFeatures:\n\n\n#. Added base for future BigQuery support: added output_mode="bigquery". Pay attention that there is no schemas in BigQuery, so schemas are Datasets.\n\n**v0.19.0**\n**Features**\n\n\n#. Added support for base Snowflake SQL Dialect.\n   Added new --output-mode=\'snowflake\' (add "clone" key)\n\nAdded support for CREATE .. CLONE with same behaviour as CREATE .. LIKE\nAdded support for CREATE .. CLONE for schemas and database - displayed in output as {"clone": {"from": ... }}\nCREATE TABLE .. CLUSTER BY ..\nCONSTRAINT .. [NOT] ENFORCED (value stored in \'primary_key_enforced\')\n\n\n#. in CREATE DATABASE properties that goes after name like key=value now parsed valid. Check examples in tests\n#. Added support for varchar COLLATE column property\n\n**v0.18.0**\n**Features**\n\n\n#. Added base support fot AWS Redshift SQL dialect. \n   Added support for ENCODE property in column.\n   Added new --output-mode=\'redshift\' that add to column \'encrypt\' property by default.\n   Also add table properties: distkeys, sortkey, diststyle, encode (table level encode), temp.\n\nSupported Redshift statements: SORTKEY, DISTSTYLE, DISTKEY, ENCODE\n\nCREATE TEMP / TEMPORARY TABLE\n\nsyntax like with LIKE statement:\n\ncreate temp table tempevent(like event); \n\n**v0.17.0**\n\n\n#. All dependencies were updated for the latest version.\n#. Added base support for CREATE [BIGFILE | SMALLFILE] [TEMPORARY] TABLESPACE \n#. Added support for create table properties like ``TABLESPACE user_data ENABLE STORAGE IN ROW CHUNK 8K RETENTION CACHE``\n#. Added support for CREATE DATABASE statement\n\n**v0.16.3**\n\n\n#. Fixed issue then using columns names equals some tokens like, for example, ``key`` caused the error. \n   But still words \'foreign\' and \'constraint\' as column names cause the empty result. I hope they rarely used.\n   Will be fixed in next releases.\n\n**v0.16.2**\n\n\n#. Fixed issue with enum in lowercase\n\n**v0.16.0**\n\n\n#. Fixed the issue when NULL column after DEFAULT used as default value.\n#. Added support for generated columns, statatements: AS , GENERATED ALWAYS, STORED in Column Defenitions, in output it placed to key \'generated\'. Keyword \'generated\' showed only if column is generated.\n#. Half of changelogs moved to ARCHIVE_CHANGELOG.txt\n#. Added base support for CREATE DOMAIN statement\n#. Added base support for CREATE SCHEMA [IF NOT EXISTS] ... [AUTHORIZATION] statement, added new type keyword \'schemas\'\n',
    'author': 'Iuliia Volkova',
    'author_email': 'xnuinside@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/xnuinside/simple-ddl-parser',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
